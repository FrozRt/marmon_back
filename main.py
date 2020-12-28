"""Start your application from here."""
import os
import time

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from settings import DEBUG
from database import database
from apps.chat.controllers import chat
from apps.news.controllers import news
from apps.stonks.controllers import stonks


app = FastAPI(debug=DEBUG,
              title='Marmon',
              version='0.1.1',
              docs_url='/docs')


@app.on_event("startup")
async def startup():
    """Async support for connecting to database."""
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """Async support for disconnect from database."""
    await database.disconnect()


@app.middleware("http")
async def exception_middleware(request, call_next):
    """Exception middleware, for handling exception."""
    if not DEBUG:
        try:
            response = await call_next(request)
        except Exception as error:
            status_code = getattr(error, 'status_code', 500)
            response = JSONResponse(content={'detail': 'Server error'}, status_code=status_code)
        return response
    else:
        return await call_next(request)


@app.middleware("http")
async def cors_middleware(request: Request, call_next):
    if request.method == 'OPTIONS':
        response = Response(status_code=204)
    else:
        response = await call_next(request)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE, HEAD, PATCH'
    response.headers['Access-Control-Max-Age'] = '86400'
    return response


@app.middleware("http")
async def process_time_middleware(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Create your routes here.

app.include_router(router=chat, tags=["chats"])
app.include_router(router=news, tags=["news"])
app.include_router(router=stonks, tags=["stonks"])


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

import time

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

import settings
from database import database
from apps.chat.controllers import chat
from apps.news.controllers import news
from apps.profiles.controllers import profiles
from apps.comments.controllers import comments
from apps.stonks.controllers import stonks


app = FastAPI(debug=settings.DEBUG,
              title=settings.APP_TITLE,
              version=settings.VERSION,
              description=settings.APP_DESCRIPTION,
              docs_url=settings.DOCS_URL)


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
    if not settings.DEBUG:
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
app.include_router(router=comments, tags=["comments"])
app.include_router(router=profiles, tags=["profiles"])


if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=False)

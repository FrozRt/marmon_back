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
              title='Simple-construction',
              version='0.1-a',
              docs_url='/docs')


@app.on_event("startup")
async def startup():
    """Async support for connecting to database."""
    await database.connect()


@app.on_event("startup")
async def startup():
    """Async support for connecting to database."""
    await database.connect()
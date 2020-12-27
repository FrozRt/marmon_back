import os
import time


os.chdir('..')

import uvicorn
from apps.settings import DEBUG

app = FastAPI(debug=DEBUG,
              title='Simple-construction',
              version='0.1-a',
              docs_url='/docs')


@app.on_event("startup")
async def startup():
    """Async support for connecting to database."""
    await database.connect()

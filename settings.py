import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


VERSION = os.environ.get("VERSION")
APP_TITLE = os.environ.get("APP_TITLE")
APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION")
DOCS_URL = os.environ.get("DOCS_URL")
DEBUG = os.environ.get("DEBUG")

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")

DATABASE_URL = os.environ.get('DATABASE_URL')
DEFAULT_SCHEMA = 'public'

SECRET_KEY = os.environ.get("SEKRET_KEY")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

AUTH_PREFIX = "Bearer"

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
LOGS_ROOT = os.path.join(BASE_DIR, "logs")

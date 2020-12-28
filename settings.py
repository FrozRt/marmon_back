import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


SECRET_KEY = os.environ.get('SEKRET_KEY')

DEBUG = True
AUTH_PREFIX = 'Bearer'

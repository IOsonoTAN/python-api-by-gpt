import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = True
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = 'my_flask_api'
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

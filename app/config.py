# config.py
class Config:
    DEBUG = True
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = 'my_flask_api'
    CACHE_REDIS_URL = 'redis://localhost:6379/0'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/playground'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

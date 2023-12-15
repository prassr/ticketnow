import os
from flask import Config

base_dir = os.path.abspath(os.path.dirname(".."))


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(base_dir, 'instance','ticketnow.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "45ef9db005a893beb85d8c34a9151a3c08482035976e5835b6725a1c820c3d88"
    CACHE_TYPE = "redis"
    CACHE_REDIS_URL = "redis://localhost:6379/8"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_DEFAULT_TIMEOUT = 300
    JWT_SECRET_KEY = "362d175b8e4e16367ba955f5bad5eb5088c5b57faff2097562a9ff9c2cb4dc94"
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 60 min * 60 sec = 1 hr
    CELERY_RESULT_BACKEND = "redis://localhost:6379/7"

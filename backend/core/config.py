import os
from typing import List
from pydantic import BaseSettings

class STMESettings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite+aiosqlite:///./stme_base.db"
    APP_OPENAPI_URL: str = "/docs"
    APP_ALLOW_ORIGINS: List[str] = ["http://localhost", "http://localhost:8000"]
    APP_ALLOW_METHODS: List[str] = ["get", "post", "update", "delete"]

    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 525600
    API_V1_STR: str = "v1"
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin"
    REDIS_URL: str = "redis://127.0.0.1:6379" 
    CACHE_CAPTCHA_EXPIRE_SECONDS: int = 60 * 5 
    CACHE_CAPTCHA_PREFIX: str = "CAPTCHA_CODE_" 
        

class ProdSettings(STMESettings):

    class Config:
        case_sensitive = True
        env_file = "settings/prod.env"
        env_file_encoding = 'utf-8'



class TestSettings(STMESettings):

    class Config:
        case_sensitive = True
        env_file = "settings/test.env"
        env_file_encoding = 'utf-8'


class DevSettings(STMESettings):

    class Config:
        case_sensitive = True
        env_file = "settings/dev.env"
        env_file_encoding = 'utf-8'


settings = None

env = os.getenv('APP_ENV', 'dev').lower()

if env == 'prod':
    settings = ProdSettings()
elif env == 'test':
    settings = TestSettings()
else:
    settings = DevSettings()
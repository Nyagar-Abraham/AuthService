from typing import ClassVar

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL :str
    JWT_SECRET_KEY :str
    JWT_ALGORITHM :str
    APP_NAME: ClassVar[str] = "Auth Service"

    class Config:
        env_file = ".env"
        extra = "ignore"
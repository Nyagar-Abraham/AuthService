from typing import ClassVar

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY :str
    JWT_ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES :int
    REFRESH_TOKEN_EXPIRE_MINUTES :int
    APP_NAME: ClassVar[str] = "Auth Service"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_HOST:str
    DATABASE_NAME:str
    DATABASE_USER:str
    DATABASE_PASSWORD:str

    class Config:
        env_file = ".env"


settings = Settings()
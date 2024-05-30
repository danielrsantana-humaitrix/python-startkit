import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVER_VERSION: str
    SERVER_PORT: int
    SERVER_LOG_LEVEL: str


current_dir = os.path.dirname(os.path.abspath(__file__))
settings = Settings(_env_file=os.path.join(current_dir, "../.env"))

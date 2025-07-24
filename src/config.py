import os.path
import pathlib
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASEDIR = pathlib.Path(__file__).parent

class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(BASEDIR.as_posix(), '../envs/app.env'), extra='allow')
    url: str = Field(alias="DATABASE_URL")
    echo: bool = True
    time_zone: str = 'Asia/Novosibirsk'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(BASEDIR.as_posix(), '../envs/app.env'), extra='allow')
    departments: List[str] = Field(alias="DEPARTMENTS")
    db_settings: DatabaseSettings = DatabaseSettings()


settings = Settings()

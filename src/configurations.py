import logging
import os
from dataclasses import dataclass

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()


@dataclass
class DBConfig:
    db_name: str = os.getenv('DB_NAME')
    db_host: str = os.getenv('DB_HOST')
    db_username: str = os.getenv('DB_USERNAME')
    db_password: str = os.getenv('DB_PASSWORD')
    db_port: int = os.getenv('DB_PORT')

    db_system: str = os.getenv('DB_SYSTEM')
    db_driver: str = os.getenv('DB_DRIVER')

    def build_url(self) -> str:
        return URL.create(
            drivername=f'{self.db_system}+{self.db_driver}',
            username=self.db_username,
            password=self.db_password,
            host=self.db_host,
            port=int(self.db_port),
            database=self.db_name
        ).render_as_string(hide_password=False)


@dataclass
class BotConfig:
    token: str = os.getenv('BOT_TOKEN')


class Config:
    debug: bool = bool(os.getenv('DEBUG'))
    logging_level: int = int(os.getenv('LOGGING_LEVEL', logging.INFO))

    bot = BotConfig()
    db = DBConfig()


conf = Config()

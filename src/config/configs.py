from pathlib import Path

from .base import BaseSetting

BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseSetting):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str


class RabbitSettings(BaseSetting):
    RABBIT_HOST: str
    RABBIT_USER: str
    RABBIT_PASSWORD: str
    RABBIT_QUEUE: str


rabbit_settings = RabbitSettings()
db_settings = DBSettings()

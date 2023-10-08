from config.app import AppConfig
from config.db import DBConfig
from config.redis import RedisConfig


class Config(
    AppConfig,
    RedisConfig,
    DBConfig,
):
    """
    Application configuration
    """

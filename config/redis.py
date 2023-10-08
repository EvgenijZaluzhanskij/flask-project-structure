import os


class RedisConfig:
    REDIS_URI = os.getenv('REDIS_URI', 'redis://localhost')

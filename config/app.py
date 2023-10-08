import os


class AppConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_key')

import os


class DBConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('DB', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

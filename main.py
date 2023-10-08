from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app(cfg):
    app = Flask(__name__)
    app.config.from_object(cfg)

    return app


def create_db(app):
    db = SQLAlchemy(app)
    _ = Migrate(app, db)
    return db

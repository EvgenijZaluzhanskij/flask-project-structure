from config import config
from main import create_app, create_db


app = create_app(config.Config)
db = create_db(app)

from . import views
from .repositories.db import models

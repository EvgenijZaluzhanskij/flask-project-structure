from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    middle_name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)

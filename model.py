
from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    email = db.Column(db.String(40))
    password = db.Column(db.String(200))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

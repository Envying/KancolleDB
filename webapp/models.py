from webapp import db
from flask_login import UserMixin

# SQLAchemy model

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=False)
    ship_class = db.Column(db.String(20), index=True, nullable=False)

def __init__(self, name, ship_class):
   self.name = name
   self.ship_class = ship_class

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    tokens = db.Column(db.Text)

def __init__(self, email, name, avatar, tokens):
   self.email = email
   self.name = name
   self.avatar = avatar
   self.tokens = tokens

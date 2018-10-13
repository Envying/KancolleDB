from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from webapp import db


# SQLAchemy model
class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    ship_class = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "Ship('{self.name}', '{self.ship_class}')"

ships = [
	{
		'name': 'Test_name',
		'ship_class': "Test_class"
	}
]
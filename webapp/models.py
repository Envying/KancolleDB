from webapp import db

# SQLAchemy model

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=False)
    ship_class = db.Column(db.String(20), index=True, nullable=False)

def __init__(self, name, ship_class):
   self.name = name
   self.ship_class = ship_class
from webapp import db

# SQLAchemy model

class Ship(db.Model):
	__tablename__ = "ship"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), index=True, nullable=False)
	ship_class = db.Column(db.String(20), index=True, nullable=False)

	def __init__(self, name, ship_class):
		self.name = name
		self.ship_class = ship_class

class FleetComposition(db.Model):
	__tablename__ = "fleet_composition"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), index=True, nullable=False)
	ship_class = db.Column(db.String(20), index=True, nullable=False)
	name2 = db.Column(db.String(20), index=True, nullable=False)
	ship_class2 = db.Column(db.String(20), index=True, nullable=False)
	name3 = db.Column(db.String(20), index=True, nullable=False)
	ship_class3 = db.Column(db.String(20), index=True, nullable=False)
	name4 = db.Column(db.String(20), index=True, nullable=False)
	ship_class4 = db.Column(db.String(20), index=True, nullable=False)
	name5 = db.Column(db.String(20), index=True, nullable=False)
	ship_class5 = db.Column(db.String(20), index=True, nullable=False)
	name6 = db.Column(db.String(20), index=True, nullable=False)
	ship_class6 = db.Column(db.String(20), index=True, nullable=False)
	world_map = db.Column(db.String(20), index=True, nullable=True)

	def __init__(self, name, ship_class, name2, ship_class2, name3, ship_class3, 
		name4, ship_class4, name5, ship_class5, name6, ship_class6, world_map):
		self.name = name
		self.ship_class = ship_class
		self.name2 = name2
		self.ship_class2 = ship_class2
		self.name3 = name3
		self.ship_class3 = ship_class3
		self.name4 = name4
		self.ship_class4 = ship_class4
		self.name5 = name5
		self.ship_class5 = ship_class5
		self.name6 = name6
		self.ship_class6 = ship_class6
		self.world_map = world_map

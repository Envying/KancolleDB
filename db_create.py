import csv
import MySQLdb
from webapp import db

# For Admin use only

# Connect to our database
db = MySQLdb.connect("127.0.0.1", "root", "kancolledbpw", "admin")
cur = db.cursor()

# Read data from local file and add to ship database table
def loadShipDatabase():
	insert_statement = (
				"INSERT INTO ship (name, ship_class, world_1_1, world_1_2) "
				"VALUES (%s, %s, 0, 0)"
				)

	with open('webapp/static/shiplist.csv', 'rU') as csvDataFile:
		csvReader = csv.reader(csvDataFile, dialect=csv.excel)
		headers = next(csvReader)
		for row in csvReader:
			cur.execute(insert_statement, row)
			db.commit()

# Delete all rows from ship database
def deleteShipDatabase():
	cur.execute("DROP TABLE ship")
	db.commit()

# Create fleet composition database
def createFleetCompositionDatabase():
	insert_statement = (
				"CREATE TABLE fleet_composition (id int, name varchar(20), ship_class varchar(20), name2 varchar(20), ship_class2 varchar(20), "
				"name3 varchar(20), ship_class3 varchar(20), name4 varchar(20), ship_class4 varchar(20), name5 varchar(20), ship_class5 varchar(20), "
				"name6 varchar(20), ship_class6 varchar(20), world_map varchar(20))"
				)
	cur.execute(insert_statement)
	db.commit()

# Delete all rows from fleet composition database
def deleteFleetCompositionDatabase():
	cur.execute("DROP TABLE fleet_composition")
	db.commit()

# Create ship usage database
def createShipUsageDatabase():
	insert_statement = (
				"INSERT INTO ship_usage (name, world_1_1, world_1_2) "
				"VALUES (%s, 0, 0)"
				)

	with open('webapp/static/shiplist.csv', 'rU') as csvDataFile:
		csvReader = csv.reader(csvDataFile, dialect=csv.excel)
		headers = next(csvReader)
		for row in csvReader:
			cur.execute(insert_statement, row[0])
			db.commit()

# Delete all rows from fleet composition database
def deleteShipUsageDatabase():
	cur.execute("DROP TABLE ship_usage")
	db.commit()

<<<<<<< HEAD
# db.create_all()

# Delete User table
def deleteUserDatabase():
	cur.execute("DROP TABLE user")
	db.commit()

# pre create the User table
def createUserDatabase():
	insert_statement = (
				"CREATE TABLE user (id int, email varchar(100), name varchar(100), avatar varchar(100), tokens Text)) "
				)
	cur.execute(insert_statement)
	db.commit()

# call the following methods to delete or create the user table
# deleteUserDatabase()
# createUserDatabase()
=======
# Run from webapp import db
# db.create_all()
>>>>>>> ac3d3b42e26bd81bbc86837172e3baef586d87ba

import csv
import MySQLdb
from webapp import db

# Connect to our database
# db = MySQLdb.connect("127.0.0.1", "root", "kancolledbpw", "admin")
# cur = db.cursor()

# Read data from local file and add to ship database table
def loadShipDatabase():
	insert_statement = (
				"INSERT INTO ship (name, ship_class) "
				"VALUES (%s, %s)"
				)

	with open('webapp/static/shiplist.csv', 'rU') as csvDataFile:
		csvReader = csv.reader(csvDataFile, dialect=csv.excel)
		headers = next(csvReader)
		for row in csvReader:
			name = row[0]
			ship_class = row[1]

			cur.execute(insert_statement, row)
			db.commit()

# Delete all rows from ship database
def deleteShipDatabase():
	cur.execute("""truncate table ship """)
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

# Some if statement to check if changes made to csv vs database
# if true recreate db else do nothing

# db.create_all()
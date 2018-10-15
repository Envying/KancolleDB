import csv
import MySQLdb
from webapp import db

# Connect to our database
db = MySQLdb.connect("127.0.0.1", "root", "kancolledbpw", "admin")
cur = db.cursor()

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
	cur.execute("DROP TABLE ship")
	db.commit()

# Some if statement to check if changes made to csv vs database
# if true recreate db else do nothing

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

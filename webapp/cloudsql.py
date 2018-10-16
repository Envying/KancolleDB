import os
import MySQLdb
import webapp

CLOUDSQL_CONNECTION_NAME = 'kancolledb-project:australia-southeast1:kancolle-mysql'
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = 'kancolledbpw'
CLOUDSQL_INSTANCE = 'admin'

# The following code checks whether we are connected to Google or Localhost
def gen_connection():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        conn_template = 'mysql+mysqldb://%s:%s@localhost/%s?unix_socket=/cloudsql/%s'
        return conn_template % (CLOUDSQL_USER, CLOUDSQL_PASSWORD, CLOUDSQL_INSTANCE, CLOUDSQL_CONNECTION_NAME)
    else:
        return 'mysql://root:kancolledbpw@127.0.0.1:3306/admin'

# Connec to the GAE SQL or Local SQL
def connect_to_cloudsql():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db_connection = MySQLdb.connect(
                        unix_socket=cloudsql_unix_socket,
                        user=CLOUDSQL_USER,
                        passwd=CLOUDSQL_PASSWORD,
                        db=CLOUDSQL_INSTANCE)
    else:
        db_connection = MySQLdb.connect(
                       host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD, db=CLOUDSQL_INSTANCE)
    return db_connection

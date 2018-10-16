import os
import MySQLdb

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
        conn_template = 'mysql://%s:%s@127.0.0.1:3306/%s'
        return conn_template % (CLOUDSQL_USER, CLOUDSQL_PASSWORD, CLOUDSQL_INSTANCE)

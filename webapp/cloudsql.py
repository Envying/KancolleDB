import os
import MySQLdb
import webapp

CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')
CLOUDSQL_INSTANCE = 'admin'

# The following code checks whether we are connected to Google or Localhost
def gen_connection():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        conn_template = 'mysql+mysqldb://%s:%s@localhost/%s?unix_socket=/cloudsql/%s'
        return conn_template % (CLOUDSQL_USER, CLOUDSQL_PASSWORD, CLOUDSQL_INSTANCE, CLOUDSQL_CONNECTION_NAME)
    else:
        return 'mysql://root:kancolledbpw@127.0.0.1:3306/admin'

def connect_to_cloudsql():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD,
            db=CLOUDSQL_INSTANCE)
    else:
        db = MySQLdb.connect(
            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD, db=CLOUDSQL_INSTANCE)
    return db

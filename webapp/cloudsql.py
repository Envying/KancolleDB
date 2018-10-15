import os

class SQL:
    SQL_CONNECTION_NAME = 'kancolledb-project:australia-southeast1:kancolle-mysql'
    SQL_USER = 'root'
    SQL_PASSWORD = 'kancolledbpw'
    SQL_INSTANCE = 'admin'

# The following code checks whether we are connected to Google or Localhost
def gen_connection():
    if not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        conn_template = 'mysql://%s:%s@127.0.0.1:3306/%s'
        return conn_template % (SQL.SQL_USER, SQL.SQL_PASSWORD, SQL.SQL_INSTANCE)
    else:
        conn_template = 'mysql+mysqldb://%s:%s@localhost/%s?unix_socket=/cloudsql/%s'
        return conn_template % (SQL.SQL_USER, SQL.SQL_PASSWORD, SQL.SQL_INSTANCE, SQL.SQL_CONNECTION_NAME)

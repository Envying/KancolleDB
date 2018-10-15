import os

PROJECT_ID = 'knacolledb-project'
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = 'knacolledbpw'
CLOUDSQL_DATABASE = 'admin'
CLOUDSQL_CONNECTION_NAME = 'kancolledb-project:australia-southeast1:kancolle-mysql'

# Using Local MySQL
LOCAL_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@127.0.0.1:3306/{database}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE)

# Using CloudSQL
LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@localhost/{database}'
    '?unix_socket=/cloudsql/{connection_name}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME)

# Checks which environemnt it is on
if os.environ.get('GAE_INSTANCE'):
    SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
    SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI

# oAuth2
GOOGLE_OAUTH2_CLIENT_ID = \
    'your-client-id'
GOOGLE_OAUTH2_CLIENT_SECRET = 'your-client-secret'

import os

db_user=os.environ.get('MARIADB_USER_ID')
db_password=os.environ.get('MARIADB_PASSWORD')
host=os.environ.get('MARIADB_HOST')
port=int(os.environ.get('MARIADB_PORT'))
database=os.environ.get('MARIADB_DATABASE')
test=False
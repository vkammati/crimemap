import mariadb
import sys
import dbconfig

def database_setup():
    try:
        conn = mariadb.connect(
            user=dbconfig.db_user,
            password=dbconfig.db_password,
            host=dbconfig.host,
            port=dbconfig.port,
            database=dbconfig.database
        )
    except mariadb.Error as e:
        print("Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    try:
        with conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
                        id int NOT NULL AUTO_INCREMENT,
                        latitude FLOAT(10,6),
                        longitude FLOAT(10,6),
                        date DATETIME,
                        category VARCHAR(50),
                        description VARCHAR(1000),
                        updated_at TIMESTAMP,
                        PRIMARY KEY (id)
                        )"""
            cursor.execute(sql);
        conn.commit()
    finally:
        conn.close()
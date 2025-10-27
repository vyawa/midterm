import mysql.connector
import json

class MySQLPersistenceWrapper:
    def __init__(self):
        # Load database config
        cfg = json.load(open("config/app.json"))
        self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            **cfg["database"]
        )

    def test_connection(self):
        """Check if connection works."""
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT DATABASE();")
        print("Connected to:", cursor.fetchone()[0])
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    db = MySQLPersistenceWrapper()
    db.test_connection()

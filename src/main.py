
from src.persistence.mysql_persistence_wrapper import MySQLPersistenceWrapper

def main():
    print("Connecting to database...")
    db = MySQLPersistenceWrapper()


    cnx = db.cnxpool.get_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM datasets;")
    rows = cursor.fetchall()

    if rows:
        print("\nDatasets:")
        for row in rows:
            print(f"- {row['dataset_id']}: {row['dataset_name']}")
    else:
        print("\nNo data found in datasets table.")

    cursor.close()
    cnx.close()
    print("\nDone.")


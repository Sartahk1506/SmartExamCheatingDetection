from Database.db_connection import DatabaseManager

db = DatabaseManager()

if db.connect():
    print("Database Connected Successfully")
else:
    print("Connection Failed")
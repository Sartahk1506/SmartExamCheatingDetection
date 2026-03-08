import mysql.connector

class DatabaseManager:
    def __init__(self, host="localhost", user="root", password="Sarthak@321", database="smart_exam_monitoring"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if connection.is_connected():
                print("Connected to MySQL database")
                return True
            else:
                print("Connection failed")
                return False

        except Exception as e:
            print("Database Error:", e)
            return False
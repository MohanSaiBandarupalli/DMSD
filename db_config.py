import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bms@6700",
        database="rentcardb",
        port=3306

    )

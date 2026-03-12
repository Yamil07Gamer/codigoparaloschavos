import mysql.connector

def get_db_connection():
    config = {
        'user': 'admin',
        'password': '1234',
        'host': 'localhost',
        'database': 'taller_db'
    }
    return mysql.connector.connect(**config)
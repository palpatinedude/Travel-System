import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ceidstar2802!!',
            database='odysseyDB'
        )
        if connection.is_connected():
            print("Connection to MySQL database established")
            return connection
    except Error as e:
        print(f"Error: {e}")

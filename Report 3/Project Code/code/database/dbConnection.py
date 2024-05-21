import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ceidstar2802!!',
            database='odyssey'
        )
        if connection.is_connected():
            print("Connection to MySQL database established")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
'''
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")
'''

import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Create a database connection to the MySQL database """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='4655',
            database='odyssey'
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    """ Close the database connection """
    if connection.is_connected():
        connection.close()
        print("Database connection closed")
import sys
# sys.path.append('../database/')
# sys.path.append('../classes/')
from db_connector import create_connection
import config

def authenticate(username, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            config.current_user = user  # save the user information
            return True
        else:
            print("No user found with the provided credentials.")
            return False
    return False
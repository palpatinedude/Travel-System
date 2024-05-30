import sys
sys.path.append('Report 4/Project Code/Code/functions')
sys.path.append('Report 4/Project Code/Code/classes')
sys.path.append('Report 4/Project Code/CodeGUI')
from db_connector import create_connection
import config
from allClasses import User

# function to authenticate user login
def authenticate(username, password):
    connection = create_connection()
    user_id = None
    user = None
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT user_id FROM User WHERE username = %s AND password = %s", (username, password))
                result = cursor.fetchone()
                if result:
                   user_id = result[0]
                   print(user_id)
                   user = User(user_id=user_id)
                   config.current_user = user  # save the user information
                   print(user)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()

    return user_id
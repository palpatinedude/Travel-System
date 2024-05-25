import sys
sys.path.append('../database/')
sys.path.append('../classes/')
from dbConnection import create_connection
from user import User

# function to authenticate user login
def authenticate(username, password):
    connection = create_connection()
    user_id = None
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT user_id FROM User WHERE username = %s AND password = %s", (username, password))
                result = cursor.fetchone()
                if result:
                   user_id = result[0]
                   user = User(user_id=user_id)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()
    

    return user_id is not None, user_id

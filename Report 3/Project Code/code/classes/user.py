import sys
sys.path.append('../database/') 
from dbConnection import create_connection

class User:
    def __init__(self, user_id=None, username=None, name=None, lastname=None, email=None, password=None, role=None, country_id=None, city_id=None, membership_id=None):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role = role
        self.country_id = country_id
        self.city_id = city_id
        self.membership_id = membership_id

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        if self.user_id is None:
            query = """INSERT INTO User (username, name, lastname, email, password, role, country_id, city_id, membership_id) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (self.username, self.name, self.lastname, self.email, self.password, self.role, self.country_id, self.city_id, self.membership_id)
            cursor.execute(query, values)
            self.user_id = cursor.lastrowid
            print(self.user_id)
        else:
            query = """UPDATE User SET username=%s, name=%s, lastname=%s, email=%s, password=%s, role=%s, country_id=%s, city_id=%s, membership_id=%s 
                       WHERE user_id=%s"""
            values = (self.username, self.name, self.lastname, self.email, self.password, self.role, self.country_id, self.city_id, self.membership_id, self.user_id)
            cursor.execute(query, values)
        connection.commit()
        cursor.close()

    def delete(self):
        if self.user_id is not None:
            connection = create_connection()
            cursor = connection.cursor()
            query = "DELETE FROM User WHERE user_id = %s"
            cursor.execute(query, (self.user_id,))
            connection.commit()
            cursor.close()
            self.user_id = None

    @classmethod
    def get_by_id(cls, user_id):
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return cls(**row)
        return None

    @staticmethod
    def check_username_existence(username):
        connection = create_connection()

        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM User WHERE username = %s", (username,))
                    count = cursor.fetchone()[0]
                    if count > 0:
                        return True  
                    return False  
            except Exception as e:
                print(f"Database error: {e}")
                return True  
            finally:
                connection.close()
        else:
            print("Connection to the database failed.")
            return True 

    @staticmethod
    def check_email_existence(email):
        connection = create_connection()

        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM User WHERE email = %s", (email,))
                    count = cursor.fetchone()[0]
                    if count > 0:
                        return True  
                    else:
                        return False  
            except Exception as e:
                print(f"Database error: {e}")
                return True 
            finally:
                connection.close()
        else:
            print("Connection to the database failed.")
            return True     

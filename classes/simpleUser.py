import sys
sys.path.append('../database/')
from db_connector import create_connection
from beneficiary import Beneficiary

class SimpleUser(Beneficiary):
    def __init__(self, user_id=None, beneficiary_type=None, bistory=None, preferences=None):
        super().__init__(user_id=user_id, beneficiary_type=beneficiary_type)
        self.bistory = bistory
        self.preferences = preferences


    def save(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO SimpleUser (beneficiary_id, bistory, preferences) VALUES (%s, %s, %s)",
                               (self.beneficiary_id, self.bistory, self.preferences))
                self.user_id = cursor.lastrowid
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()


    @staticmethod
    def update(user_id, bistory=None, preferences=None):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                if bistory is not None and preferences is not None:
                    cursor.execute("UPDATE SimpleUser SET bistory = %s, preferences = %s WHERE user_id = %s",
                                   (bistory, preferences, user_id))
                    connection.commit()
                    print("SimpleUser information updated successfully!")
                else:
                    print("Both bistory and preferences must be provided to update SimpleUser.")
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()
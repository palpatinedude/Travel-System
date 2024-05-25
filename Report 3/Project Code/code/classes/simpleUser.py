import sys
sys.path.append('../database/')
from dbConnection import create_connection

class SimpleUser:
    def __init__(self, user_id=None, beneficiary_id=None, history=None, preferences=None):
        self.user_id = user_id
        self.beneficiary_id = beneficiary_id
        self.history = history
        self.preferences = preferences

    def save(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO SimpleUser (beneficiary_id, history, preferences) VALUES (%s, %s, %s)",
                               (self.beneficiary_id, self.history, self.preferences))
                self.user_id = cursor.lastrowid
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()
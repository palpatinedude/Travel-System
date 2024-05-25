import sys
sys.path.append('../database/')
from dbConnection import create_connection

class BusinessPartner:
    def __init__(self, user_id, tax_code, registration_number, website, description):
        self.user_id = user_id
        self.tax_code = tax_code
        self.registration_number = registration_number
        self.website = website
        self.description = description

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            query = """
            INSERT INTO BusinessPartner (user_id, tax_code, registration_number, website, description)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (self.user_id, self.tax_code, self.registration_number, self.website, self.description))
            connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Database Error: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()
            connection.close()
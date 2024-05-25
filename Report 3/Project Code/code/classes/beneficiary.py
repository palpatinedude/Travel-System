import sys
sys.path.append('../database/')
from dbConnection import create_connection

class Beneficiary:
    def __init__(self, user_id, beneficiary_type, date_of_birth=None, address=None, contact_number=None):
        self.user_id = user_id
        self.beneficiary_type = beneficiary_type
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_number = contact_number

    def save(self):
        connection = create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    query = """
                    INSERT INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (self.user_id, self.beneficiary_type, self.date_of_birth, self.address, self.contact_number))
                    connection.commit()
                    return True
            except Exception as e:
                print(f"Database error: {e}")
                return False
            finally:
                connection.close()
        else:
            print("Connection to the database failed.")
            return False

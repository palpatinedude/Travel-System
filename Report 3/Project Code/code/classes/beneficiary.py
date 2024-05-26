import sys
sys.path.append('../database/')
from dbConnection import create_connection
from user import User

class Beneficiary(User):
    def __init__(self, user_id, beneficiary_type, date_of_birth=None, address=None, contact_number=None):
        super().__init__(user_id=user_id)
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

    @staticmethod
    def getRoleID(beneficiary_id):
        connection = create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    query = "SELECT beneficiary_type FROM Beneficiary WHERE beneficiary_id = %s"
                    cursor.execute(query, (beneficiary_id,))
                    result = cursor.fetchone()
                    if result:
                          return result[0]
                    else:
                        return None
            except Exception as e:
                print(f"Database error: {e}")
                return None
            finally:
                connection.close()
        else:
            print("Connection to the database failed.")
            return None    

    @staticmethod
    def get_id_by_beneficiary_id(beneficiary_id):
        connection = create_connection()  
        if connection:
            try:
                with connection.cursor() as cursor:
                    query = "SELECT user_id FROM Beneficiary WHERE beneficiary_id = %s"
                    cursor.execute(query, (beneficiary_id,))
                    result = cursor.fetchone()
                    if result:
                        return result[0]
                    else:
                        return None
            except Exception as e:
                print(f"Database error: {e}")
                return None
            finally:
                connection.close()
        else:
            print("Connection to the database failed.")
            return None            

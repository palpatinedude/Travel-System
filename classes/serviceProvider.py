import sys
sys.path.append('../database/')
from db_connector import create_connection
from beneficiary import Beneficiary    

class ServiceProvider(Beneficiary):
     def __init__(self, user_id=None, beneficiary_type=None, languages_spoken=None, specialties=None, certifications=None):
      super().__init__(user_id=user_id, beneficiary_type=beneficiary_type)
      self.languages_spoken = languages_spoken
      self.specialties = specialties
      self.certifications = certifications

      def save(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO ServiceProvider (beneficiary_id, languages_spoken, specialties, certifications) VALUES (%s, %s, %s, %s)",
                               (self.beneficiary_id, self.languages_spoken, self.specialties, self.certifications))
                self.provider_id = cursor.lastrowid
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()

      @staticmethod
      def update(user_id, certifications=None, specialities=None, languages_spoken=None):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                if certifications is not None and specialities is not None and languages_spoken is not None:
                    cursor.execute("UPDATE ServiceProvider SET certifications = %s, specialties = %s, languages_spoken = %s WHERE user_id = %s",
                                   (certifications, specialities, languages_spoken, user_id))
                    connection.commit()
                    print("ServiceProvider information updated successfully!")
                else:
                    print("All fields (certifications, specialities, languages_spoken) must be provided to update ServiceProvider.")
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()
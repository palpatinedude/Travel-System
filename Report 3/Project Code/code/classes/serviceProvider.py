import sys
sys.path.append('../database/')
from dbConnection import create_connection

class ServiceProvider:
    def __init__(self, provider_id=None, beneficiary_id=None, languages_spoken=None, specialties=None, certifications=None):
        self.provider_id = provider_id
        self.beneficiary_id = beneficiary_id
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

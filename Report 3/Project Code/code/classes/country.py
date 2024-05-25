import sys
sys.path.append('../database/')
from dbConnection import create_connection

class Country:
    def __init__(self, country_id=None, country_name=None, continent=None, currency=None):
        self.country_id = country_id
        self.country_name = country_name
        self.continent = continent
        self.currency = currency

    def save(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Country (country_name, continent, currency) VALUES (%s, %s, %s)",
                               (self.country_name, self.continent, self.currency))
                self.country_id = cursor.lastrowid
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()

    def update(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Country SET country_name=%s, continent=%s, currency=%s WHERE country_id=%s",
                               (self.country_name, self.continent, self.currency, self.country_id))
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()

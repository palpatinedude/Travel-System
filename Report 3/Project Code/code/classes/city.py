import sys
sys.path.append('../database/')
from dbConnection import create_connection

class City:
    def __init__(self, city_id=None, city_name=None, country_id=None, latitude=None, longitude=None):
        self.city_id = city_id
        self.city_name = city_name
        self.country_id = country_id
        self.latitude = latitude
        self.longitude = longitude

    def save(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO City (city_name, country_id, latitude, longitude) VALUES (%s, %s, %s, %s)",
                               (self.city_name, self.country_id, self.latitude, self.longitude))
                self.city_id = cursor.lastrowid
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
                cursor.execute("UPDATE City SET city_name=%s, country_id=%s, latitude=%s, longitude=%s WHERE city_id=%s",
                               (self.city_name, self.country_id, self.latitude, self.longitude, self.city_id))
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()


class Country:
    def __init__(self, country_id=None, country_name=None, continent=None, currency=None):
        self.country_id = country_id
        self.country_name = country_name
        self.continent = continent
        self.currency = currency

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO Country (country_name, continent, currency) 
                           VALUES (%s, %s, %s)"""
                values = (self.country_name, self.continent, self.currency)
                cursor.execute(query, values)
                print("Country saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE Country 
                           SET country_name = %s, continent = %s, currency = %s
                           WHERE country_id = %s"""
                values = (self.country_name, self.continent, self.currency, self.country_id)
                cursor.execute(query, values)
                print("Country updated successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

class City:
    def __init__(self, city_id=None, city_name=None, country_id=None, latitude=None, longitude=None):
        self.city_id = city_id
        self.city_name = city_name
        self.country_id = country_id
        self.latitude = latitude
        self.longitude = longitude

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO City (city_name, country_id, latitude, longitude) 
                           VALUES (%s, %s, %s, %s)"""
                values = (self.city_name, self.country_id, self.latitude, self.longitude)
                cursor.execute(query, values)
                print("City saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE City 
                           SET city_name = %s, country_id = %s, latitude = %s, longitude = %s
                           WHERE city_id = %s"""
                values = (self.city_name, self.country_id, self.latitude, self.longitude, self.city_id)
                cursor.execute(query, values)
                print("City updated successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")
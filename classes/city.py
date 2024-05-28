import sys
sys.path.append('GUI')
sys.path.append('database')
from db_connector import create_connection

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

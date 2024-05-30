import sys
sys.path.append('../database/')
from dbConnection import create_connection

class Points:
    def __init__(self, points_id=None, card_id=None, points=None, available_coupons=None):
        self.points_id = points_id
        self.card_id = card_id
        self.points = points
        self.available_coupons = available_coupons

    def save(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Points (card_id, points, available_coupons) VALUES (%s, %s, %s)",
                               (self.card_id, self.points, self.available_coupons))
                self.points_id = cursor.lastrowid
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
                cursor.execute("UPDATE Points SET points = %s, available_coupons = %s WHERE points_id = %s",
                               (self.points, self.available_coupons, self.points_id))
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()

    def getPoints(self, beneficiary_id):
        connection = create_connection()  
        points = None
        if connection:
            try:
                with connection.cursor() as cursor:
                    # retrieve points for the beneficiary
                    cursor.execute("SELECT points FROM Points WHERE card_id IN (SELECT card_id FROM Card WHERE beneficiary_id = %s)", (beneficiary_id,))
                    points = cursor.fetchone()  
            except Exception as e:
                print(f"Error: {e}")
            finally:
                connection.close()  
        return points        



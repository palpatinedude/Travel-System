import sys
sys.path.append('../database/')
from dbConnection import create_connection

class Card:
    def __init__(self, card_id=None, beneficiary_id=None, cardnumber=None, barcode=None, expiration_date=None):
        self.card_id = card_id
        self.beneficiary_id = beneficiary_id
        self.cardnumber = cardnumber
        self.barcode = barcode
        self.expiration_date = expiration_date

    def save(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Card (beneficiary_id, cardnumber, barcode, expiration_date) VALUES (%s, %s, %s, %s)",
                               (self.beneficiary_id, self.cardnumber, self.barcode, self.expiration_date))
                self.card_id = cursor.lastrowid
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()
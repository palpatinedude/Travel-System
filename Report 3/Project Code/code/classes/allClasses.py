import sys
from dbConnection import create_connection

class User:
    def __init__(self, user_id=None, username=None, name=None, lastname=None, email=None, password=None, role=None, country_id=None, city_id=None, membership_id=None):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role = role
        self.country_id = country_id
        self.city_id = city_id
        self.membership_id = membership_id

    def save(self):
      try:
        with create_connection() as connection:
            cursor = connection.cursor()
            if self.user_id is None:
                query = """INSERT INTO User (username, name, lastname, email, password, role, country_id, city_id, membership_id) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (self.username, self.name, self.lastname, self.email, self.password, self.role, self.country_id, self.city_id, self.membership_id)
                cursor.execute(query, values)
                self.user_id = cursor.lastrowid
                print("User saved successfully!")
                connection.commit()
            else:
                print("To update an existing user, please use the update() method.")
      except Exception as e:
        print(f"Error: {e}")    

    @staticmethod
    def update(user_id, username, name, lastname, email, password, role, country_id, city_id, membership_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE User SET username=%s, name=%s, lastname=%s, email=%s, password=%s, role=%s, country_id=%s, city_id=%s, membership_id=%s 
                           WHERE user_id=%s"""
                values = (username, name, lastname, email, password, role, country_id, city_id, membership_id, user_id)
                cursor.execute(query, values)
                connection.commit()
                print("User information updated successfully!")
        except Exception as e:
            print(f"Error: {e}")

    @classmethod
    def get_by_id(cls, user_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM User WHERE user_id = %s"
                cursor.execute(query, (user_id,))
                row = cursor.fetchone()
                if row:
                    return cls(*row)
        except Exception as e:
            print(f"Error: {e}")
        return None

    @staticmethod
    def check_username_existence(username):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM User WHERE username = %s", (username,))
                count = cursor.fetchone()[0]
                return count > 0
        except Exception as e:
            print(f"Error: {e}")
            return True  

    @staticmethod
    def check_email_existence(email):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM User WHERE email = %s", (email,))
                count = cursor.fetchone()[0]
                return count > 0
        except Exception as e:
            print(f"Error: {e}")
            return True  


class BusinessPartner(User):
    def __init__(self, user_id=None, tax_code=None, registration_number=None, website=None, description=None):
        super().__init__(user_id=user_id)
        self.tax_code = tax_code
        self.registration_number = registration_number
        self.website = website
        self.description = description

    def save(self):
        try:
            super().save()  # Save user first
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO BusinessPartner (user_id, tax_code, registration_number, website, description) 
                           VALUES (%s, %s, %s, %s, %s)"""
                values = (self.user_id, self.tax_code, self.registration_number, self.website, self.description)
                cursor.execute(query, values)
                print("Business partner saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")


class Admin(User):
    def __init__(self, user_id=None, role=None, phone_number=None, status='active', last_login=None, creation_date=None, notes=None, profile_picture=None):
        super().__init__(user_id=user_id)
        self.role = role
        self.phone_number = phone_number
        self.status = status
        self.last_login = last_login
        self.creation_date = creation_date
        self.notes = notes
        self.profile_picture = profile_picture

    def save(self):
        try:
            super().save()  
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO Admin (user_id, role, phone_number, status, last_login, creation_date, notes, profile_picture) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (self.user_id, self.role, self.phone_number, self.status, self.last_login, self.creation_date, self.notes, self.profile_picture)
                cursor.execute(query, values)
                print("Admin saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")


class Beneficiary(User):
    def __init__(self, user_id=None, beneficiary_type=None, date_of_birth=None, address=None, contact_number=None):
        super().__init__(user_id=user_id)
        self.beneficiary_type = beneficiary_type
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_number = contact_number

    def save(self):
        try:
            super().save() 
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number) 
                           VALUES (%s, %s, %s, %s, %s)"""
                values = (self.user_id, self.beneficiary_type, self.date_of_birth, self.address, self.contact_number)
                cursor.execute(query, values)
                print("Beneficiary saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    @classmethod
    def get_by_id(cls, user_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM Beneficiary WHERE user_id = %s"
                cursor.execute(query, (user_id,))
                row = cursor.fetchone()
                if row:
                    beneficiary_data = {
                        'user_id': row[0],
                        'beneficiary_type': row[1],
                        'date_of_birth': row[2],
                        'address': row[3],
                        'contact_number': row[4]
                    }
                    return cls(**beneficiary_data)
        except Exception as e:
            print(f"Error: {e}")
        return None

    @staticmethod
    def get_role_id(beneficiary_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
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

    @staticmethod
    def get_id_by_beneficiary_id(beneficiary_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
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

    def isSharing(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = "SELECT location_status FROM Beneficiary WHERE user_id = %s"
                cursor.execute(query, (self.user_id,))
                result = cursor.fetchone()
                if result:
                    return result[0] == 'Active'
                else:
                    return False
        except Exception as e:
            print(f"Database error: {e}")
            return False        

class SimpleUser(Beneficiary):
    def __init__(self, user_id=None, history=None, preferences=None, **kwargs):
        super().__init__(user_id=user_id, beneficiary_type='Simple User', **kwargs)
        self.history = history
        self.preferences = preferences

    def save(self):
        try:
            super().save() 
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO SimpleUser (beneficiary_id, history, preferences) 
                           VALUES (%s, %s, %s)"""
                values = (self.beneficiary_id, self.history, self.preferences)
                cursor.execute(query, values)
                print("SimpleUser saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            super().update() 
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE SimpleUser 
                           SET history = %s, preferences = %s 
                           WHERE beneficiary_id = %s"""
                values = (self.history, self.preferences, self.beneficiary_id)
                cursor.execute(query, values)
                print("SimpleUser updated successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")


class ServiceProvider(Beneficiary):
    def __init__(self, user_id=None, languages_spoken=None, specialties=None, certifications=None, **kwargs):
        super().__init__(user_id=user_id, beneficiary_type='Service Provider', **kwargs)
        self.languages_spoken = languages_spoken
        self.specialties = specialties
        self.certifications = certifications

    def save(self):
        try:
            super().save() 
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO ServiceProvider (beneficiary_id, languages_spoken, specialties, certifications) 
                           VALUES (%s, %s, %s, %s)"""
                values = (self.beneficiary_id, self.languages_spoken, self.specialties, self.certifications)
                cursor.execute(query, values)
                print("ServiceProvider saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            super().update() 
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE ServiceProvider 
                           SET languages_spoken = %s, specialties = %s, certifications = %s 
                           WHERE beneficiary_id = %s"""
                values = (self.languages_spoken, self.specialties, self.certifications, self.beneficiary_id)
                cursor.execute(query, values)
                print("ServiceProvider updated successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

class Membership:
    def __init__(self, membership_type=None, duration=None, membership_status=None, description=None, created_date=None, membership_id=None):
        self.membership_id = membership_id
        self.membership_type = membership_type
        self.duration = duration
        self.membership_status = membership_status
        self.description = description
        self.created_date = created_date

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO Membership (membership_type, duration, membership_status, description, created_date) 
                           VALUES (%s, %s, %s, %s, %s)"""
                values = (self.membership_type, self.duration, self.membership_status, self.description, self.created_date)
                cursor.execute(query, values)
                print("Membership saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE Membership 
                           SET membership_type = %s, duration = %s, membership_status = %s, description = %s, created_date = %s
                           WHERE membership_id = %s"""
                values = (self.membership_type, self.duration, self.membership_status, self.description, self.created_date, self.membership_id)
                cursor.execute(query, values)
                print("Membership updated successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")


class Card:
    def __init__(self, beneficiary_id=None, cardnumber=None, barcode=None, expiration_date=None, card_id=None):
        self.card_id = card_id
        self.beneficiary_id = beneficiary_id
        self.cardnumber = cardnumber
        self.barcode = barcode
        self.expiration_date = expiration_date

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO Card (beneficiary_id, cardnumber, barcode, expiration_date) 
                           VALUES (%s, %s, %s, %s)"""
                values = (self.beneficiary_id, self.cardnumber, self.barcode, self.expiration_date)
                cursor.execute(query, values)
                print("Card saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")



class Points:
    def __init__(self, card_id=None, points=None, available_coupons=None, points_id=None):
        self.points_id = points_id
        self.card_id = card_id
        self.points = points
        self.available_coupons = available_coupons

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO Points (card_id, points, available_coupons) 
                           VALUES (%s, %s, %s)"""
                values = (self.card_id, self.points, self.available_coupons)
                cursor.execute(query, values)
                print("Points saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE Points 
                           SET points = %s, available_coupons = %s 
                           WHERE card_id = %s"""
                values = (self.points, self.available_coupons, self.card_id)
                cursor.execute(query, values)
                print("Points updated successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def getPoints(card_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = "SELECT points FROM Points WHERE card_id = %s"
                cursor.execute(query, (card_id,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return None
        except Exception as e:
            print(f"Error: {e}")
            return None


class PointsHistory:
    def __init__(self, points_id=None, transaction_type=None, points_change=None, transaction_date=None, business_id=None, transaction_id=None):
        self.transaction_id = transaction_id
        self.points_id = points_id
        self.transaction_type = transaction_type
        self.points_change = points_change
        self.transaction_date = transaction_date
        self.business_id = business_id

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO PointsHistory (points_id, transaction_type, points_change, transaction_date, business_id) 
                           VALUES (%s, %s, %s, %s, %s)"""
                values = (self.points_id, self.transaction_type, self.points_change, self.transaction_date, self.business_id)
                cursor.execute(query, values)
                print("PointsHistory saved successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE PointsHistory 
                           SET points_id = %s, transaction_type = %s, points_change = %s, transaction_date = %s, business_id = %s
                           WHERE transaction_id = %s"""
                values = (self.points_id, self.transaction_type, self.points_change, self.transaction_date, self.business_id, self.transaction_id)
                cursor.execute(query, values)
                print("PointsHistory updated successfully!")
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def getHistory(points_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM PointsHistory WHERE points_id = %s ORDER BY transaction_date"
                cursor.execute(query, (points_id,))
                result = cursor.fetchall()
                history = []
                for row in result:
                    history.append({
                        'transaction_id': row[0],
                        'points_id': row[1],
                        'transaction_type': row[2],
                        'points_change': row[3],
                        'transaction_date': row[4],
                        'business_id': row[5]
                    })
                return history
        except Exception as e:
            print(f"Error: {e}")
            return None


    def getBusinessName(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = "SELECT business_name FROM Business WHERE business_id = %s"
                cursor.execute(query, (self.business_id,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return None
        except Exception as e:
            print(f"Error: {e}")
            return None 
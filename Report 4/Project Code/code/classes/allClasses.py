import sys
from dbConnection import create_connection

class User:
    def __init__(self, user_id=None, username=None, name=None, lastname=None, email=None, password=None, role=None, country_id=None, city_id=None):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role = role
        self.country_id = country_id
        self.city_id = city_id


    def save(self):
      try:
        with create_connection() as connection:
            cursor = connection.cursor()
            if self.user_id is None:
                query = """INSERT INTO User (username, name, lastname, email, password, role, country_id, city_id) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (self.username, self.name, self.lastname, self.email, self.password, self.role, self.country_id, self.city_id)
                cursor.execute(query, values)
                self.user_id = cursor.lastrowid
                print("User saved successfully!")
                connection.commit()
            else:
                print("To update an existing user, please use the update() method.")
      except Exception as e:
        print(f"Error: {e}")    


    def update(self, username=None, password=None):
       try:
           with create_connection() as connection:
               cursor = connection.cursor()
               query = """UPDATE User SET username=%s, password=%s WHERE user_id=%s"""
               values = (username, password, self.user_id)
               cursor.execute(query, values)
               connection.commit()
               print("Username and password updated successfully!")
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


class Beneficiary:
    def __init__(self, beneficiary_id=None, user_id=None, beneficiary_type=None, date_of_birth=None, address=None, contact_number=None, location_status='Inactive', membership_id=None):
        self.beneficiary_id = beneficiary_id
        self.user_id = user_id
        self.beneficiary_type = beneficiary_type
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_number = contact_number
        self.location_status = location_status
        self.membership_id = membership_id

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """
                INSERT INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number, location_status, membership_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values = (self.user_id, self.beneficiary_type, self.date_of_birth, self.address, self.contact_number, self.location_status, self.membership_id)
                cursor.execute(query, values)
                connection.commit()
                self.beneficiary_id = cursor.lastrowid
                print("Beneficiary saved successfully!")
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
                    return cls(
                        beneficiary_id=row[0], 
                        user_id=row[1], 
                        beneficiary_type=row[2], 
                        date_of_birth=row[3], 
                        address=row[4], 
                        contact_number=row[5], 
                        location_status=row[6], 
                        membership_id=row[7]
                    )
        except Exception as e:
            print(f"Error: {e}")
        return None

    def update(self, date_of_birth=None, address=None, contact_number=None, location_status=None, beneficiary_id=None):
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if address is not None:
            self.address = address
        if contact_number is not None:
            self.contact_number = contact_number
        if location_status is not None:
            self.location_status = location_status
       
        try:
          with create_connection() as connection:
              cursor = connection.cursor()
              query = """
              UPDATE Beneficiary 
              SET date_of_birth = %s, address = %s, contact_number = %s, location_status = %s
              WHERE beneficiary_id = %s
              """
              values = (self.date_of_birth, self.address, self.contact_number, self.location_status, self.beneficiary_id)
              
              print("Before executing query")
              print(self.date_of_birth, self.address, self.contact_number, self.location_status, self.beneficiary_id)
              cursor.execute(query, values)
              print("After executing query")
              
              connection.commit()
              print("Beneficiary updated successfully!")
        except Exception as e:
              print(f"Error: {e}")

    def updateMemberID(self, membership_id):
      try:
        with create_connection() as connection:
            cursor = connection.cursor()
            query = """
            UPDATE Beneficiary 
            SET membership_id = %s
            WHERE beneficiary_id = %s
            """
            values = (membership_id, self.beneficiary_id)

            cursor.execute(query, values)
            connection.commit()
            print("Membership ID updated successfully!")
      except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def getRoleID(beneficiary_id):
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
    def __init__(self, beneficiary_id=None, bistory=None, preferences=None):
        super().__init__(beneficiary_id=beneficiary_id, beneficiary_type='Simple User')
        self.bistory = bistory
        self.preferences = preferences

    def save(self):
        try:
            #super().save() 
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO SimpleUser (beneficiary_id, bistory, preferences) 
                           VALUES (%s, %s, %s)"""
                values = (self.beneficiary_id, self.bistory, self.preferences)
                cursor.execute(query, values)
               # self.beneficiary_id = cursor.lastrowid
                print("SimpleUser saved successfully!")
                connection.commit()
                sel
        except Exception as e:
            print(f"Error: {e}")

    def update(self,beneficiary_id ,bistory=None, preferences=None):
      try:
          with create_connection() as connection:
              print("Before executing query")
              print(self.beneficiary_id)
              cursor = connection.cursor()
              query = """UPDATE SimpleUser 
                         SET bistory = %s, preferences = %s 
                         WHERE beneficiary_id = %s"""
              values = (bistory, preferences, beneficiary_id)
              cursor.execute(query, values)
              print("SimpleUser updated successfully!")
              connection.commit()
      except Exception as e:
          print(f"Error: {e}")

    @classmethod
    def get_by_id(cls, beneficiary_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM SimpleUser WHERE beneficiary_id = %s"
                cursor.execute(query, (beneficiary_id,))
                row = cursor.fetchone()
                if row:
                    return cls(
                        beneficiary_id=row[0], 
                        bistory=row[1], 
                        preferences=row[2]
                    )
        except Exception as e:
            print(f"Error: {e}")
        return None

class ServiceProvider(Beneficiary):
    def __init__(self, beneficiary_id=None, provider_id=None, languages_spoken=None, specialties=None, certifications=None):
        super().__init__(beneficiary_id=beneficiary_id, user_id=user_id, beneficiary_type='Service Provider')
        self.languages_spoken = languages_spoken
        self.specialties = specialties
        self.certifications = certifications

    def save(self):
        try:
        #    super().save() 
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

    def update(self, language_spoken=None, specialties=None, certifications=None):
      try:
          with create_connection() as connection:
              cursor = connection.cursor()
              query = """
              UPDATE ServiceProvider 
              SET language_spoken = %s, specialties = %s, certifications = %s
              WHERE beneficiary_id = %s
              """
              values = (language_spoken, specialties, certifications, self.beneficiary_id)
              cursor.execute(query, values)
              print("ServiceProvider updated successfully!")
              connection.commit() 
      except Exception as e:
          print(f"Error: {e}")    
          return None


    @classmethod
    def get_by_id(cls, beneficiary_id):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM ServiceProvider WHERE beneficiary_id = %s"
                cursor.execute(query, (beneficiary_id,))
                row = cursor.fetchone()
                if row:
                    return cls(
                        beneficiary_id=row[0], 
                        languages_spoken=row[1], 
                        specialties=row[2],
                        certifications=row[3]
                    )
        except Exception as e:
            print(f"Error: {e}")
        return None    


class Membership:
    def __init__(self ,membership_type=None, duration=None, membership_status=None,  created_date=None, membership_id=None):
        self.membership_id = membership_id
        self.membership_type = membership_type
        self.duration = duration
        self.membership_status = membership_status
        self.created_date = created_date

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """INSERT INTO Membership (membership_type, duration, membership_status, created_date) 
                           VALUES (%s, %s, %s, %s)"""
                values = (self.membership_type, self.duration, self.membership_status, self.created_date)
                cursor.execute(query, values)
                connection.commit()
                self.membership_id = cursor.lastrowid
                print("Membership saved successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """UPDATE Membership 
                           SET membership_type = %s, duration = %s, membership_status = %s, created_date = %s
                           WHERE membership_id = %s"""
                values = (self.membership_type, self.duration, self.membership_status, self.created_date, self.membership_id)
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
                connection.commit()
                self.card_id = cursor.lastrowid
                print(self.card_id)
                print("Card saved successfully!")
        except Exception as e:
            print(f"Error: {e}")



class Points:
    def __init__(self,card_id=None, points=None, available_coupons=None, points_id=None):
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
    def __init__(self,points_id=None, transaction_type=None, points_change=None, transaction_date=None, business_id=None, transaction_id=None):
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

class Business:
    def __init__(self, partner_id, business_name, business_type, advertisement_details, price, country_id, city_id):
        self.partner_id = partner_id
        self.business_name = business_name
        self.business_type = business_type
        self.advertisement_details = advertisement_details
        self.price = price
        self.country_id = country_id
        self.city_id = city_id

    def save(self):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            sql = "INSERT INTO Business (partner_id, business_name, business_type, advertisement_details, price, country_id, city_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (self.partner_id, self.business_name, self.business_type, self.advertisement_details, self.price, self.country_id, self.city_id)
            cursor.execute(sql, val)

            conn.commit()
            print("Business saved successfully")

        except mysql.connector.Error as error:
            print("Failed to save business: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

class Market(Business):
    def __init__(self, partner_id, business_name, advertisement_details, price, country_id, city_id, market_type, market_specific_attribute):
        super().__init__(partner_id, business_name, 'Market', advertisement_details, price, country_id, city_id)
        self.market_type = market_type
        self.market_specific_attribute = market_specific_attribute

    def save(self):
        #super().save()
        try:
            conn = create_connection()
            cursor = conn.cursor()

            sql = "INSERT INTO Market (business_id, market_type, market_specific_attribute) VALUES (%s, %s, %s)"
            val = (self.business_id, self.market_type, self.market_specific_attribute)
            cursor.execute(sql, val)

            conn.commit()
            print("Market saved successfully")

        except mysql.connector.Error as error:
            print("Failed to save market: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        
    def display_attributes(self):
        return f"Market Type: {self.market_type}\nMarket Specific Attribute: {self.market_specific_attribute}"
        


    @staticmethod
    def get_all():
        markets = []
        try:
            conn = create_connection()
            cursor = conn.cursor(dictionary=True)

            sql = "SELECT * FROM Market INNER JOIN Business ON Market.business_id = Business.business_id"
            cursor.execute(sql)

            for row in cursor.fetchall():
                markets.append(Market(
                    partner_id=row['partner_id'],
                    business_name=row['business_name'],
                    advertisement_details=row['advertisement_details'],
                    price=row['price'],
                    country_id=row['country_id'],
                    city_id=row['city_id'],
                    market_type=row['market_type'],
                    market_specific_attribute=row['market_specific_attribute']
                ))

        except mysql.connector.Error as error:
            print("Failed to retrieve markets: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        return markets

class FoodAndBeverage(Business):
    def __init__(self, partner_id, business_name, advertisement_details, price, country_id, city_id, food_type, food_beverage_specific_attribute):
        super().__init__(partner_id, business_name, 'Food and Beverage', advertisement_details, price, country_id, city_id)
        self.food_type = food_type
        self.food_beverage_specific_attribute = food_beverage_specific_attribute

    def save(self):
        #super().save()
        try:
            conn = create_connection()
            cursor = conn.cursor()

            sql = "INSERT INTO FoodAndBeverage (business_id, food_type, food_beverage_specific_attribute) VALUES (%s, %s, %s)"
            val = (self.business_id, self.food_type, self.food_beverage_specific_attribute)
            cursor.execute(sql, val)

            conn.commit()
            print("Food and Beverage saved successfully")

        except mysql.connector.Error as error:
            print("Failed to save Food and Beverage: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def display_attributes(self):
        return f"Food Type: {self.food_type}\nFood and Beverage Specific Attribute: {self.food_beverage_specific_attribute}"

    @staticmethod
    def get_all():
        food_and_beverages = []
        try:
            conn = create_connection()
            cursor = conn.cursor(dictionary=True)

            sql = "SELECT * FROM FoodAndBeverage INNER JOIN Business ON FoodAndBeverage.business_id = Business.business_id"
            cursor.execute(sql)

            for row in cursor.fetchall():
                food_and_beverages.append(FoodAndBeverage(
                    partner_id=row['partner_id'],
                    business_name=row['business_name'],
                    advertisement_details=row['advertisement_details'],
                    price=row['price'],
                    country_id=row['country_id'],
                    city_id=row['city_id'],
                    food_type=row['food_type'],
                    food_beverage_specific_attribute=row['food_beverage_specific_attribute']
                ))

        except mysql.connector.Error as error:
            print("Failed to retrieve food and beverages: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        return food_and_beverages

class Hotels(Business):
    def __init__(self, partner_id, business_name, advertisement_details, price, country_id, city_id, hotel_filters, hotel_stars, hotel_floors, hotel_specific_attribute):
        super().__init__(partner_id, business_name, 'Hotels', advertisement_details, price, country_id, city_id)
        self.hotel_filters = hotel_filters
        self.hotel_stars = hotel_stars
        self.hotel_floors = hotel_floors
        self.hotel_specific_attribute = hotel_specific_attribute

    def save(self):
       # super().save()
        try:
            conn = create_connection()
            cursor = conn.cursor()

            sql = "INSERT INTO Hotels (business_id, hotel_filters, hotel_stars, hotel_floors, hotel_specific_attribute) VALUES (%s, %s, %s, %s, %s)"
            val = (self.business_id, self.hotel_filters, self.hotel_stars, self.hotel_floors, self.hotel_specific_attribute)
            cursor.execute(sql, val)

            conn.commit()
            print("Hotels saved successfully")

        except mysql.connector.Error as error:
            print("Failed to save Hotels: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def display_attributes(self):
        return f"Hotel Filters: {self.hotel_filters}\nHotel Stars: {self.hotel_stars}\nHotel Floors: {self.hotel_floors}\nHotel Specific Attribute: {self.hotel_specific_attribute}"

    @staticmethod
    def get_all():
        hotels = []
        try:
            conn = create_connection()
            cursor = conn.cursor(dictionary=True)

            sql = "SELECT * FROM Hotels INNER JOIN Business ON Hotels.business_id = Business.business_id"
            cursor.execute(sql)

            for row in cursor.fetchall():
                hotels.append(Hotels(
                    partner_id=row['partner_id'],
                    business_name=row['business_name'],
                    advertisement_details=row['advertisement_details'],
                    price=row['price'],
                    country_id=row['country_id'],
                    city_id=row['city_id'],
                    hotel_filters=row['hotel_filters'],
                    hotel_stars=row['hotel_stars'],
                    hotel_floors=row['hotel_floors'],
                    hotel_specific_attribute=row['hotel_specific_attribute']
                ))

        except mysql.connector.Error as error:
            print("Failed to retrieve hotels: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        return hotels

class Bars(Business):
    def __init__(self, partner_id, business_name, advertisement_details, price, country_id, city_id, age_boundary, bar_type, bar_specific_attribute):
        super().__init__(partner_id, business_name, 'Bars', advertisement_details, price, country_id, city_id)
        self.age_boundary = age_boundary
        self.bar_type = bar_type
        self.bar_specific_attribute = bar_specific_attribute

    def save(self):
       # super().save()
        try:
            conn = create_connection()
            cursor = conn.cursor()

            sql = "INSERT INTO Bars (business_id, age_boundary, bar_type, bar_specific_attribute) VALUES (%s, %s, %s, %s)"
            val = (self.business_id, self.age_boundary, self.bar_type, self.bar_specific_attribute)
            cursor.execute(sql, val)

            conn.commit()
            print("Bars saved successfully")

        except mysql.connector.Error as error:
            print("Failed to save Bars: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()    

    def display_attributes(self):
        return f"Age Boundary: {self.age_boundary}\nBar Type: {self.bar_type}\nBar Specific Attribute: {self.bar_specific_attribute}"                    

    @staticmethod
    def get_all():
        bars = []
        try:
            conn = create_connection()
            cursor = conn.cursor(dictionary=True)

            sql = "SELECT * FROM Bars INNER JOIN Business ON Bars.business_id = Business.business_id"
            cursor.execute(sql)

            for row in cursor.fetchall():
                bars.append(Bars(
                    partner_id=row['partner_id'],
                    business_name=row['business_name'],
                    advertisement_details=row['advertisement_details'],
                    price=row['price'],
                    country_id=row['country_id'],
                    city_id=row['city_id'],
                    age_boundary=row['age_boundary'],
                    bar_type=row['bar_type'],
                    bar_specific_attribute=row['bar_specific_attribute']
                ))

        except mysql.connector.Error as error:
            print("Failed to retrieve bars: {}".format(error))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        return bars

class Service:
    def __init__(self, provider_id, description, service_name, country_id, city_id):
        self.provider_id = provider_id
        self.description = description
        self.service_name = service_name
        self.country_id = country_id
        self.city_id = city_id

    def save(self):
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """
                INSERT INTO Service (provider_id, description, service_name, country_id, city_id)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (self.provider_id, self.description, self.service_name, self.country_id, self.city_id)
                cursor.execute(query, values)
                connection.commit()
                self.service_id = cursor.lastrowid
                print("Service saved successfully!")
        except Exception as e:
            print(f"Error: {e}")

class Accommodation(Service):
    def __init__(self, provider_id, description, service_name, country_id, city_id, num_rooms, facilities):
        super().__init__(provider_id, description, service_name, country_id, city_id)
        self.num_rooms = num_rooms
        self.facilities = facilities

    def save(self):
       # super().save()
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """
                INSERT INTO Accommodation (service_id, num_rooms, facilities)
                VALUES (%s, %s, %s)
                """
                values = (self.service_id, self.num_rooms, self.facilities)
                cursor.execute(query, values)
                connection.commit()
                print("Accommodation saved successfully!")
        except Exception as e:
            print(f"Error: {e}")

class Car(Service):
    def __init__(self, provider_id, description, service_name, country_id, city_id, car_model, year_of_manufacture, car_type, rental_rate):
        super().__init__(provider_id, description, service_name, country_id, city_id)
        self.car_model = car_model
        self.year_of_manufacture = year_of_manufacture
        self.car_type = car_type
        self.rental_rate = rental_rate

    def save(self):
        #super().save()
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """
                INSERT INTO Car (service_id, car_model, year_of_manufacture, car_type, rental_rate)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (self.service_id, self.car_model, self.year_of_manufacture, self.car_type, self.rental_rate)
                cursor.execute(query, values)
                connection.commit()
                print("Car saved successfully!")
        except Exception as e:
            print(f"Error: {e}")

class Activity(Service):
    def __init__(self, provider_id, description, service_name, country_id, city_id, activity_name, age_requirement, duration_hours, activity_description):
        super().__init__(provider_id, description, service_name, country_id, city_id)
        self.activity_name = activity_name
        self.age_requirement = age_requirement
        self.duration_hours = duration_hours
        self.activity_description = activity_description

    def save(self):
      #  super().save()
        try:
            with create_connection() as connection:
                cursor = connection.cursor()
                query = """
                INSERT INTO Activity (service_id, activity_name, age_requirement, duration_hours, activity_description)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (self.service_id, self.activity_name, self.age_requirement, self.duration_hours, self.activity_description)
                cursor.execute(query, values)
                connection.commit()
                print("Activity saved successfully!")
        except Exception as e:
            print(f"Error: {e}")                

class Service:
    def __init__(self, provider_id, description, service_name, country_id, city_id):
        self.provider_id = provider_id
        self.description = description
        self.service_name = service_name
        self.country_id = country_id
        self.city_id = city_id

    def save(self):
        try:
            with create_connection() as conn:
                cursor = conn.cursor()

                sql = "INSERT INTO Service (provider_id, description, service_name, country_id, city_id) VALUES (%s, %s, %s, %s, %s)"
                val = (self.provider_id, self.description, self.service_name, self.country_id, self.city_id)
                cursor.execute(sql, val)
                self.service_id = cursor.lastrowid  

                conn.commit()
                print(f"{self.service_name} saved successfully")

        except mysql.connector.Error as error:
            print(f"Failed to save {self.service_name}: {error}")

    @staticmethod
    def get_all():
        services = []
        try:
            with create_connection() as conn:
                cursor = conn.cursor(dictionary=True)

                sql = "SELECT * FROM Service"
                cursor.execute(sql)

                for row in cursor.fetchall():
                    services.append(Service(
                        provider_id=row['provider_id'],
                        description=row['description'],
                        service_name=row['service_name'],
                        country_id=row['country_id'],
                        city_id=row['city_id']
                    ))

        except mysql.connector.Error as error:
            print(f"Failed to retrieve services: {error}")

        return services

class Accommodation(Service):
    def __init__(self, provider_id, description, service_name, country_id, city_id, num_rooms, facilities):
        super().__init__(provider_id, description, service_name, country_id, city_id)
        self.num_rooms = num_rooms
        self.facilities = facilities

    def save(self):
       # super().save()
        try:
            with create_connection() as conn:
                cursor = conn.cursor()

                sql = "INSERT INTO Accommodation (service_id, num_rooms, facilities) VALUES (%s, %s, %s)"
                val = (self.service_id, self.num_rooms, self.facilities)
                cursor.execute(sql, val)

                conn.commit()
                print("Accommodation saved successfully")

        except mysql.connector.Error as error:
            print(f"Failed to save accommodation: {error}")

    @staticmethod
    def get_all():
        accommodations = []
        try:
            with create_connection() as conn:
                cursor = conn.cursor(dictionary=True)

                sql = "SELECT * FROM Accommodation INNER JOIN Service ON Accommodation.service_id = Service.provider_service_id"
                cursor.execute(sql)

                for row in cursor.fetchall():
                    accommodations.append(Accommodation(
                        provider_id=row['provider_id'],
                        description=row['description'],
                        service_name=row['service_name'],
                        country_id=row['country_id'],
                        city_id=row['city_id'],
                        num_rooms=row['num_rooms'],
                        facilities=row['facilities']
                    ))

        except mysql.connector.Error as error:
            print(f"Failed to retrieve accommodations: {error}")

        return accommodations

class Car(Service):
    def __init__(self, provider_id, description, service_name, country_id, city_id, car_model, year_of_manufacture, car_type, rental_rate):
        super().__init__(provider_id, description, service_name, country_id, city_id)
        self.car_model = car_model
        self.year_of_manufacture = year_of_manufacture
        self.car_type = car_type
        self.rental_rate = rental_rate

    def save(self):
       # super().save()
        try:
            with create_connection() as conn:
                cursor = conn.cursor()

                sql = "INSERT INTO Car (service_id, car_model, year_of_manufacture, car_type, rental_rate) VALUES (%s, %s, %s, %s, %s)"
                val = (self.service_id, self.car_model, self.year_of_manufacture, self.car_type, self.rental_rate)
                cursor.execute(sql, val)

                conn.commit()
                print("Car saved successfully")

        except mysql.connector.Error as error:
            print(f"Failed to save car: {error}")

    @staticmethod
    def get_all():
        cars = []
        try:
            with create_connection() as conn:
                cursor = conn.cursor(dictionary=True)

                sql = "SELECT * FROM Car INNER JOIN Service ON Car.service_id = Service.provider_service_id"
                cursor.execute(sql)

                for row in cursor.fetchall():
                    cars.append(Car(
                        provider_id=row['provider_id'],
                        description=row['description'],
                        service_name=row['service_name'],
                        country_id=row['country_id'],
                        city_id=row['city_id'],
                        car_model=row['car_model'],
                        year_of_manufacture=row['year_of_manufacture'],
                        car_type=row['car_type'],
                        rental_rate=row['rental_rate']
                    ))

        except mysql.connector.Error as error:
            print(f"Failed to retrieve cars: {error}")

        return cars

class Activity(Service):
    def __init__(self, provider_id, description, service_name, country_id, city_id, activity_name, age_requirement, duration_hours, activity_description):
        super().__init__(provider_id, description, service_name, country_id, city_id)
        self.activity_name = activity_name
        self.age_requirement = age_requirement
        self.duration_hours = duration_hours
        self.activity_description = activity_description

    def save(self):
      #  super().save()
        try:
            with create_connection() as conn:
                cursor = conn.cursor()

                sql = "INSERT INTO Activity (service_id, activity_name, age_requirement, duration_hours, activity_description) VALUES (%s, %s, %s, %s, %s)"
                val = (self.service_id, self.activity_name, self.age_requirement, self.duration_hours, self.activity_description)
                cursor.execute(sql, val)

                conn.commit()
                print("Activity saved successfully")

        except mysql.connector.Error as error:
            print(f"Failed to save activity: {error}")

    @staticmethod
    def get_all():
        activities = []
        try:
            with create_connection() as conn:
                cursor = conn.cursor(dictionary=True)

                sql = "SELECT * FROM Activity INNER JOIN Service ON Activity.service_id = Service.provider_service_id"
                cursor.execute(sql)

                for row in cursor.fetchall():
                    activities.append(Activity(
                        provider_id=row['provider_id'],
                        description=row['description'],
                        service_name=row['service_name'],
                        country_id=row['country_id'],
                        city_id=row['city_id'],
                        activity_name=row['activity_name'],
                        age_requirement=row['age_requirement'],
                        duration_hours=row['duration_hours'],
                        activity_description=row['activity_description']
                    ))

        except mysql.connector.Error as error:
            print(f"Failed to retrieve activities: {error}")

        return activities            
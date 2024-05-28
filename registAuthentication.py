import sys
from db_connector import create_connection
import mysql.connector
from mysql.connector import Error
# from user import User
# from beneficiary import Beneficiary
# from businessPartner import BusinessPartner
# from country import Country
# from city import City

# def check_location_existence(location):
#     try:
#         country, city = location.split(', ')
#     except ValueError:
#         print("Invalid location format. It should be 'Country, City'.")
#         return None, None

#     connection = create_connection()

#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 # check if the country exists
#                 cursor.execute("SELECT country_id FROM Country WHERE country_name = %s", (country,))
#                 country_result = cursor.fetchone()
#                 if not country_result:
#                     # if the country doesn't exist, insert it
#                     cursor.execute("INSERT INTO Country (country_name) VALUES (%s)", (country,))
#                     connection.commit()
#                     country_id = cursor.lastrowid
#                 else:
#                     country_id = country_result[0]

#                 # check if the city exists
#                 cursor.execute("SELECT city_id FROM City WHERE city_name = %s AND country_id = %s", (city, country_id))
#                 city_result = cursor.fetchone()
#                 if not city_result:
#                     # if the city doesn't exist, insert it
#                     cursor.execute("INSERT INTO City (city_name, country_id) VALUES (%s, %s)", (city, country_id))
#                     connection.commit()
#                     city_id = cursor.lastrowid
#                 else:
#                     city_id = city_result[0]

#                 return country_id, city_id
#         except Error as e:
#             print(f"Database error: {e}")
#             return None, None
#         finally:
#             connection.close()
#     else:
#         print("Connection to the database failed.")
#         return None, None

# def registerUser(username, name, lastname, email, password, role, location, date_of_birth=None, address=None, contact_number=None):
#     print("Register button clicked")
#     country_id, city_id = check_location_existence(location)

#     if country_id is None or city_id is None:
#         return False, None  

#     role_mapping = {
#         "Service Provider": "beneficiary",
#         "Simple User": "beneficiary",
#         "Business Partner": "partner"
#     }

#     mapped_role = role_mapping.get(role, "beneficiary")  
#     connection = create_connection()

#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 hashed_password = password  # ideally, this should be hashed 

#                 user_query = """
#                 INSERT INTO User (username, name, lastname, email, password, role, country_id, city_id)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#                 """
#                 cursor.execute(user_query, (username, name, lastname, email, hashed_password, mapped_role, country_id, city_id))
#                 connection.commit()

#                 user_id = cursor.lastrowid
#                 print(f"User ID: {user_id}")
#                 print(role)
#                 if role in ["Simple User", "Service Provider"]:
#                     beneficiary_query = """
#                     INSERT INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number)
#                     VALUES (%s, %s, %s, %s, %s)
#                     """
#                     cursor.execute(beneficiary_query, (user_id, role, date_of_birth, address, contact_number))
#                     connection.commit()
#                 elif role == "Business Partner":
#                     business_partner_query = """
#                     INSERT INTO BusinessPartner (user_id)
#                     VALUES (%s)
#                     """
#                     cursor.execute(business_partner_query, (user_id,))
#                     connection.commit()
#                 print(f"User ID: {user_id}")
#                 print("User registered successfully.")
#                 return True, user_id  # return True for success and the user_id
#         except Error as e:
#             print(f"Database error: {e}")
#             return False, None  
#         finally:
#             connection.close()
#     else:
#         print("Connection to the database failed.")
#         return False, None  

# def check_username_existence(username):
#     connection = create_connection()

#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT COUNT(*) FROM User WHERE username = %s", (username,))
#                 count = cursor.fetchone()[0]
#                 if count > 0:
#                     return True  
#                 return False  
#         except Error as e:
#             print(f"Database error: {e}")
#             return True  
#         finally:
#             connection.close()
#     else:
#         print("Connection to the database failed.")
#         return True 

# def check_email_existence(email):
#     connection = create_connection()

#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT COUNT(*) FROM User WHERE email = %s", (email,))
#                 count = cursor.fetchone()[0]
#                 if count > 0:
#                     return True  
#                 else:
#                     return False  
#         except Error as e:
#             print(f"Database error: {e}")
#             return True 
#         finally:
#             connection.close()
#     else:
#         print("Connection to the database failed.")
#         return True 

def check_location_existence(location):
    try:
        country_name, city_name = location.split(', ')
    except ValueError:
        print("Invalid location format. It should be 'Country, City'.")
        return None, None

    connection = create_connection()

    if connection:
        try:
            with connection.cursor() as cursor:
                # check if the country exists
                cursor.execute("SELECT country_id FROM Country WHERE country_name = %s", (country_name,))
                country_result = cursor.fetchone()
                if not country_result:
                    #  country doesn't exist, insert it
                    country_obj = Country(country_name=country_name)
                    country_obj.save()
                    country_id = country_obj.country_id
                    print(f"Inserted new country. Country ID: {country_id}")
                else:
                    country_id = country_result[0]
                    print(f"Country exists. Country ID: {country_id}")

                # check if the city exists
                cursor.execute("SELECT city_id FROM City WHERE city_name = %s AND country_id = %s", (city_name, country_id))
                city_result = cursor.fetchone()
                if not city_result:
                    # The city doesn't exist, insert it
                    city_obj = City(city_name=city_name, country_id=country_id)
                    city_obj.save()
                    city_id = city_obj.city_id
                    print(f"Inserted new city. City ID: {city_id}")
                else:
                    city_id = city_result[0]
                    print(f"City exists. City ID: {city_id}")

                return country_id, city_id
        except Exception as e:
            print(f"Database error: {e}")
            return None, None
        finally:
            connection.close()
    else:
        print("Connection to the database failed.")
        return None, None

def registerUser(username, name, lastname, email, password, role, location):
    print("Register button clicked")
    country_id, city_id = check_location_existence(location)
    print(country_id, city_id)

    if country_id is None or city_id is None:
        return False, None  

    role_mapping = {
        "Service Provider": "beneficiary",
        "Simple User": "beneficiary",
        "Business Partner": "partner"
    }

    mapped_role = role_mapping.get(role, "beneficiary")  
    connection = create_connection()

    if connection:
        try:
            with connection.cursor() as cursor:
                hashed_password = password  # ideally, this should be hashed 

                # create a user object and save it to the database
               
                user = User(username=username, name=name,lastname=lastname, email=email, password=hashed_password, role=mapped_role,country_id=country_id, city_id=city_id)
                user.save()
                user_id = user.user_id

                print(f"User ID: {user_id}")
                print(role)
                if role in ["Simple User", "Service Provider"]:
                    # create a beneficiary object and save it to the database
                    beneficiary = Beneficiary(user_id=user_id, beneficiary_type=role)
                    beneficiary.save()
                elif role == "Business Partner":
                    # create a businessPartner object and save it to the database
                    business_partner = BusinessPartner(user_id)
                    business_partner.save()

                print("User registered successfully.")
                return True, user_id  # return true for success and the user_id
        except Exception as e:
            print(f"Database error: {e}")
            return False, None  
        finally:
            connection.close()
    else:
        print("Connection to the database failed.")
        return False, None  
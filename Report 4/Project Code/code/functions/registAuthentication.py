import sys
sys.path.append('../database/')
sys.path.append('../classes/')
from dbConnection import create_connection
from allClasses import User, Country, City, Beneficiary, BusinessPartner

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


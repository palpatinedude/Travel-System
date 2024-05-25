from dbConnection import create_connection

# function to retrieve points for a beneficiary from the database
def getPoints(beneficiary_id):
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
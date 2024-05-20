import sys,os
import mysql.connector
from models import Review, Response, User

# #connect to MySQL
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# passwd="4655",
# database="od"
# )

# #check if connection is established         #testing 
# if (mydb):
#     print("Connection Successful")
# else:
#     print("Connection Unsuccessful")

# #creating a cursor object using the cursor() method
# mycursor = mydb.cursor() #cursor object which is used to interact with the database

########################################################################################################

def main():
    # Step 1: Create a new review
    review = Review(reviewer_id=1, reviewee_id=2, rating=5, review_text="Great service!")
    review.save()

    # Ensure the review is saved and has a valid ID
    if review.review_id:
        # Step 2: Retrieve and print all reviews
        reviews = Review.get_all()
        for rev in reviews:
            print(vars(rev))

        # Step 3: Update the review
        review.rating = 4
        review.save()

        # Step 4: Delete the review
        review.delete()
        for rev in reviews:
            print(vars(rev))

    #     # Step 5: Create a new response to the saved review
        response = Response(review_id=4, replier_id=2, reply_text="Thank you for your feedback reviewer 4! :)")
        response.save()

    #     # Step 6: Retrieve and print all responses
        responses = Response.get_all()
        for res in responses:
            print(vars(res))

    #     # Step 7: Update the response
        response.reply_text = "Thank you very much for your feedback! hihi"
        response.save()

    #     # Step 8: Delete the response
    #     response.delete()
    # else:
    #     print("Failed to create a review. Cannot proceed with creating a response.")

if __name__ == "__main__":
    main()


import sys,os
import mysql.connector
from models import Review, Response, User, ChatMessage, FriendRequest, Beneficiary

def main():
    # Assuming user1 and user2 already exist in the database with their respective user IDs

    # Retrieve user1 and user2 from the database based on their usernames
    user1 = User.get_by_username("robert_brown")
    user2 = User.get_by_username("mary_smith")

    if user1 and user2:  # Check if both users were successfully retrieved
        # Check if both users are beneficiaries
        beneficiary1 = Beneficiary.get_by_user_id(user1.user_id)
        beneficiary2 = Beneficiary.get_by_user_id(user2.user_id)
    
        if beneficiary1 and beneficiary2:  # Check if both users are beneficiaries
            # Send a friend request from user1 to user2
            friend_request = FriendRequest(user1_id=user1.user_id, user2_id=user2.user_id)
            friend_request.save()
            print(f"Friend request sent from user: {user1.username} to user: {user2.username}")

            # Retrieve the friend request by its ID
            retrieved_request = FriendRequest.get_by_id(friend_request.friendship_id)
            if retrieved_request:
                print("Retrieved friend request:")
                print(f"Friendship ID: {retrieved_request.friendship_id}, User1 ID: {retrieved_request.user1_id}, User2 ID: {retrieved_request.user2_id}, Status: {retrieved_request.status}, Requested At: {retrieved_request.requested_at}, Accepted At: {retrieved_request.accepted_at}")
            else:
                print("Friend request not found")

            # Check if there is a friend request between user1 and user2
            retrieved_request = FriendRequest.get_by_users(user1.user_id, user2.user_id)
            if retrieved_request:
                print("Friend request found between user1 and user2")
            else:
                print("No friend request found between user1 and user2")
        else:
            print("One or both users are not beneficiaries.")
    else:
        print("One or both users not found in the database.")


if __name__ == "__main__":
    main()
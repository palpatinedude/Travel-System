import sys,os
import mysql.connector
from models import Review, Response, User, ChatMessage

def main():
    # Assuming user1 and user2 already exist in the database with their respective user IDs

    # Retrieve user1 and user2 from the database based on their usernames
    user1 = User.get_by_username("john_doe")
    user2 = User.get_by_username("janedoe")

    if user1 and user2:  # Check if both users were successfully retrieved
        while True:
            # Prompt the user to send a message or exit
            print("Enter 'exit' to quit.")
            message_text = input(f"{user1.username}: ")

            if message_text.lower() == "exit":
                break

            # Send a message from user1 to user2
            user1.send_message(receiver_id=user2.user_id, message_text=message_text)

            # Retrieve messages for user2
            messages_user2 = ChatMessage.get_messages(user_id=user2.user_id)

            # Display received messages for user2
            print("\nMessages received by user2:")
            for message in messages_user2:
                print(f"From: {message.sender_id}, Message: {message.message_text}, Sent At: {message.sent_at}")

            # Prompt the user to send a reply or exit
            print("\nEnter 'exit' to quit replying.")
            reply_text = input(f"{user2.username}: ")

            if reply_text.lower() == "exit":
                break

            # Send a reply from user2 to user1
            user2.send_message(receiver_id=user1.user_id, message_text=reply_text)

            # Retrieve messages for user1
            messages_user1 = ChatMessage.get_messages(user_id=user1.user_id)

            # Display received messages for user1
            print("\nMessages received by user1:")
            for message in messages_user1:
                print(f"From: {message.sender_id}, Message: {message.message_text}, Sent At: {message.sent_at}")
    else:
        print("One or both users not found in the database.")

if __name__ == "__main__":
    main()

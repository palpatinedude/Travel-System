import sys
import tkinter as tk
import os
sys.path.append('Report 4/Project Code/Code/functions')
sys.path.append('Report 4/Project Code/Code/classes')
sys.path.append('Report 4/Project Code/CodeGUI')
from tkinter import messagebox, ttk
from db_connector import create_connection, close_connection
from tkinter import scrolledtext, Toplevel, Listbox, Button, Scrollbar
import config
import mysql.connector
from mysql.connector import Error

########################################################## REVIEW GUI ##########################################################

class ReviewApp:
    def __init__(self, root, user_id, business_name):
        self.root = root
        self.user_id = user_id  # Logged in user's ID
        self.business_name = business_name  # Business name passed to the constructor
        self.root.title("Review Publication System")
        self.root.geometry("360x640")  # Set window size to simulate a phone screen

        self.review_frame = tk.Frame(root, bg='#118599')
        self.review_frame.pack(fill=tk.BOTH, expand=True)

        # Add empty rows at the top to lower the content
        for i in range(5):
            self.review_frame.grid_rowconfigure(i, minsize=10)

        tk.Label(self.review_frame, text="Please let us know about your experience!", bg='#118599', fg='white',
                 font=('Arial', 22, 'bold'), wraplength=360, anchor='w', justify='left').grid(row=0, column=0, columnspan=6,
                                                                                             padx=5, pady=5, sticky="ew")
        tk.Label(self.review_frame, text="Leave your feedback and help us improve our services", bg='#118599', fg='white',
                 font=('Arial', 16), wraplength=360, anchor='w', justify='left').grid(row=1, column=0, columnspan=6, padx=5,
                                                                                    pady=5, sticky="ew")

        # Add empty rows at the top to lower the content
        for i in range(5):
            self.review_frame.grid_rowconfigure(i, minsize=20)

        tk.Label(self.review_frame, text="Business:", bg='#118599', fg='white', font=('Arial', 14, 'bold')).grid(row=5, column=0,
                                                                                                                padx=5, pady=5,
                                                                                                                sticky='w')
        # Display the business name directly
        tk.Label(self.review_frame, text=self.business_name, bg='#118599', fg='white', font=('Arial', 14)).grid(row=5, column=1,
                                                                                                                columnspan=5, padx=5, pady=5, sticky='ew')

        tk.Label(self.review_frame, text="Rate Service:", bg='#118599', fg='white', font=('Arial', 14, 'bold')).grid(row=6, column=0,
                                                                                                                     padx=5, pady=5,
                                                                                                                     sticky='w')
        self.rating_var = tk.IntVar()
        self.rating_var.set(0)  # Default rating to 0 stars

        self.stars = []
        for i in range(5):
            star = tk.Button(self.review_frame, text="★", font=("Arial", 8), command=lambda i=i: self.set_rating(i + 1))
            star.grid(row=7, column=i + 1, padx=1, pady=1)
            self.stars.append(star)

        tk.Label(self.review_frame, text="Write a Review:", bg='#118599', fg='white', font=('Arial', 14, 'bold')).grid(row=8,
                                                                                                                      column=0,
                                                                                                                      padx=5, pady=5,
                                                                                                                      sticky='nw')
        self.review_text = tk.Text(self.review_frame, width=30, height=8)
        self.review_text.grid(row=9, column=0, columnspan=6, padx=5, pady=5, sticky='w')

        self.submit_button = tk.Button(self.review_frame, text="Submit", command=self.addReview, bg="green", fg="white")
        self.submit_button.grid(row=10, column=0, columnspan=3, padx=5, pady=10, sticky='e')

        self.cancel_button = tk.Button(self.review_frame, text="Cancel", command=self.root.destroy, bg="red", fg="white")
        self.cancel_button.grid(row=10, column=3, columnspan=3, padx=5, pady=10, sticky='w')

    def set_rating(self, rating):
        self.rating_var.set(rating)
        for i in range(5):
            if i < rating:
                self.stars[i].config(fg="gold")
            else:
                self.stars[i].config(fg="black")

    def checkStars(self):
        if self.rating_var.get() == 0:
            messagebox.showerror("Error", "Please rate the service")
            return False
        return True

    def checkLength(self):  # check if length surpasses 100 characters
        if len(self.review_text.get("1.0", tk.END)) > 100:
            messagebox.showerror("Error", "Review text should not exceed 100 characters")
            return False
        return True

    def validateReview(self):
        if self.checkStars() and self.checkLength():
            return True
        return False

    def refValidation(self):
        messagebox.showinfo("Success", "Review created successfully")

    def showReject(self):
        messagebox.showerror("Error", "Failed to create review")

    def rejectMessage(self, message):
        messagebox.showerror("Error", message)

    def fetch_businesses(self):
        businesses = []
        try:
            connection = create_connection()
            cursor = connection.cursor()
            query = "SELECT business_name FROM Business"
            cursor.execute(query)
            for row in cursor.fetchall():
                businesses.append(row[0])
            cursor.close()
            connection.close()
        except Error as e:
            self.rejectMessage(f"Failed to fetch businesses: {e}")
        return businesses

    def addReview(self):
        if not self.validateReview():
            return

        reviewer_id = self.user_id
        selected_business_name = self.business_name
        # print(selected_business_name, reviewer_id)

        try:
            connection = create_connection()
            cursor = connection.cursor()
            
            # Fetch the provider_id for the selected business_name
            query = "SELECT provider_service_id FROM service WHERE service_name = %s"
            cursor.execute(query, (selected_business_name,))
            result = cursor.fetchone()
            # print(result)
            print(reviewer_id, selected_business_name)
            
            if result:
                reviewee_id = result[0]
                print(reviewee_id)
            else:
                self.rejectMessage("Invalid business selected")
            # return

            rating = self.rating_var.get()
            review_text = self.review_text.get("1.0", tk.END).strip()

            if not reviewer_id or not reviewee_id or not review_text:
                self.rejectMessage("All fields are required")
                return

            # Insert the review into the database
            query = "INSERT INTO Review (reviewer_id, reviewee_id, rating, review_text) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (reviewer_id, reviewee_id, rating, review_text))
            connection.commit()
            
            cursor.close()
            connection.close()
            self.refValidation()
        except Error as e:
            self.showReject()
            self.rejectMessage(f"Failed to create review: {e}")

########################################### RESPONSE GUI ####################################################################



########################################### ENTER DESTINATION GUI ############################################################

class DestinationGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Destination Finder")
        self.root.geometry("360x640")  # Set window size to simulate a phone screen

        self.destination_frame = tk.Frame(root, bg='#118599')
        self.destination_frame.pack(fill=tk.BOTH, expand=True)

        # Add empty rows at the top to lower the content
        for i in range(5):
            self.destination_frame.grid_rowconfigure(i, minsize=10)

        tk.Label(self.destination_frame, text="What are you exploring today?", bg='#118599', fg='white', font=('Arial', 22, 'bold'), wraplength=360, anchor='w', justify='left').grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="ew")
        tk.Label(self.destination_frame, text="Please insert country and city", bg='#118599', fg='white', font=('Arial', 16), wraplength=360, anchor='w', justify='left').grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="ew")

        # Add empty rows at the top to lower the content
        for i in range(5):
            self.destination_frame.grid_rowconfigure(i, minsize=20)

        # Input fields for country and city
        tk.Label(self.destination_frame, text="Enter Country:", bg='#118599', fg='white', font=('Arial', 14, 'bold')).grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.country_entry = tk.Entry(self.destination_frame, width=30)
        self.country_entry.grid(row=6, column=0, columnspan=6, padx=10, pady=5, sticky='ew')

        tk.Label(self.destination_frame, text="Enter City:", bg='#118599', fg='white', font=('Arial', 14, 'bold')).grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.city_entry = tk.Entry(self.destination_frame, width=30)
        self.city_entry.grid(row=8, column=0, columnspan=6, padx=10, pady=5, sticky='ew')

        self.submit_button = tk.Button(self.destination_frame, text="Find Destination", command=self.find_destination, bg="green", fg="white")
        self.submit_button.grid(row=10, column=0, columnspan=3, padx=5, pady=10, sticky='e')

    def find_destination(self):
        country = self.country_entry.get()
        city = self.city_entry.get()

        if not country or not city:
            messagebox.showerror("Error", "Both country and city are required")
            return

        connection = create_connection()
        cursor = connection.cursor()

        try:
            # Find the country ID based on the country name
            cursor.execute("SELECT country_id FROM Country WHERE country_name=%s", (country,))
            country_result = cursor.fetchone()

            if not country_result:
                messagebox.showerror("Error", "Country not found")
                return

            country_id = country_result[0]

            # Find the city based on the country ID and city name
            cursor.execute("SELECT city_name, latitude, longitude FROM City WHERE city_name=%s AND country_id=%s", (city, country_id))
            city_result = cursor.fetchone()

            if city_result:
                city_name, latitude, longitude = city_result
                messagebox.showinfo("Destination Found", f"City: {city_name}\nLatitude: {latitude}\nLongitude: {longitude}")
                self.root.destroy()   #close current window 
                # mainPage()
            else:
                messagebox.showerror("Error", "City not found in the specified country")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            cursor.close()
            connection.close()

############################################# FRIEND REQUESTING #############################################################################

class FriendRequestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Friend Request System")
        self.root.geometry("360x640")  # Set window size

        self.connection = create_connection()  # Establish database connection

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True, padx=20, pady=20)

        tk.Label(self.main_frame, text="Add Friends", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        self.search_entry = tk.Entry(self.main_frame, width=30)
        self.search_entry.grid(row=1, column=0, columnspan=2, pady=10)

        self.search_button = tk.Button(self.main_frame, text="Search", command=self.searchByUsername)
        self.search_button.grid(row=2, column=0, pady=10)

        self.add_button = tk.Button(self.main_frame, text="Add Friend", command=self.displayConfirmationDialog)
        self.add_button.grid(row=2, column=1, pady=10)

        self.showAddFriends_button = tk.Button(self.main_frame, text="Load Friends", command=self.showAddFriends)
        self.showAddFriends_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.load_recommendations_button = tk.Button(self.main_frame, text="Load Recommended Friends", command=self.fetchRecommendedFriends)
        self.load_recommendations_button.grid(row=4, column=0, columnspan=2, pady=10)

    def searchByUsername(self):
        username = self.search_entry.get()
        if not username:
            messagebox.showerror("Error", "You haven't typed anything, please write a username.")
            return

        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()  # Fetch the results
        cursor.close()  # Close the cursor after fetching results

        if user:
            self.displayUserProfile(user)
        else:
            messagebox.showerror("Error", "There isn't a user with such a username!")

    def displayUserProfile(self, user):
        profile_window = tk.Toplevel(self.root)
        profile_window.title(f"{user['username']}'s Profile")
        profile_window.geometry("300x200")

        tk.Label(profile_window, text=f"Username: {user['username']}").pack(pady=10)
        tk.Button(profile_window, text="Send Friend Request", command=lambda: self.sendFriendRequest(user)).pack(pady=10)
        # friend_button = tk.Button(self.main_frame, text=friend['username'], command=lambda friend=friend: self.displayUserProfile(friend))


    def sendFriendRequest(self, user):
        sender_id = config.current_user['user_id']  # Use the current logged-in user's ID
        recipient_id = user['user_id']
        cursor = self.connection.cursor()
        query = "INSERT INTO FriendRequest (user1_id, user2_id, status) VALUES (%s, %s, 'pending')"
        cursor.execute(query, (sender_id, recipient_id))
        self.connection.commit()
        cursor.close()

        self.displayConfirmationDialog()

    def displayConfirmationDialog(self):
        confirmation = messagebox.askyesno("Confirmation", "Do you want to send a friend request?")
        if confirmation:
            self.confirmFriendRequest()
        else:
            self.cancelFriendRequest()

    def confirmFriendRequest(self):
        messagebox.showinfo("Info", "Your friend request has been sent.")
        
    def cancelFriendRequest(self):
        messagebox.showinfo("Info", "Friend request cancelled.")
        
    def showAddFriends(self):
        user_id = config.current_user['user_id']  # Use the current logged-in user's ID
        cursor = self.connection.cursor(dictionary=True)
        query = """
        SELECT u.username 
        FROM FriendRequest fr
        JOIN User u ON fr.user2_id = u.user_id
        WHERE fr.user1_id = %s AND fr.status = 'accepted'
        """
        cursor.execute(query, (user_id,))
        friends = cursor.fetchall()
        cursor.close()

        friends_list = [friend['username'] for friend in friends]
        messagebox.showinfo("Friends List", "\n".join(friends_list) if friends_list else "You have no friends added yet.")

    def fetchRecommendedFriends(self):
        # Fetch recommended friends who are not already friends with the current user
        user_id = config.current_user['user_id']
        cursor = self.connection.cursor(dictionary=True)

        # Query to select recommended friends who are not already friends with the current user
        query = """
        SELECT u.user_id, u.username 
        FROM User u
        JOIN FriendRequest fr ON (fr.user1_id = %s AND fr.user2_id = u.user_id) 
                              OR (fr.user2_id = %s AND fr.user1_id = u.user_id)
        WHERE fr.status = 'accepted';
        """
        cursor.execute(query, (user_id, user_id))

        recommended_friends = cursor.fetchall()
        cursor.close()

        if recommended_friends:
            for i, friend in enumerate(recommended_friends):
                # Create buttons for recommended friends
                friend_button = tk.Button(self.main_frame, text=friend['username'], command=lambda id=friend['user_id']: self.displayUserProfile(friend))
                friend_button.grid(row=5+i, column=0, columnspan=2, pady=5)
        else:
            messagebox.showinfo("Recommended Friends", "No recommended friends found.")

################################# FRIENDS ###############################################

class FriendsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Friends")
        self.root.geometry("360x640")
        self.connection = create_connection()  # Establish database connection

        self.friends_frame = tk.Frame(self.root, bg='#118599')
        self.friends_frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.friends_frame, text="My Friends", bg='#118599', fg='white', font=('Arial', 22, 'bold'))
        self.title_label.pack(pady=20)

        self.profile_show_friends()

    def profile_show_friends(self):
        cursor = self.connection.cursor(dictionary=True)
        user_id = config.current_user.user_id  # Use the current logged-in user's ID
        query = """
        SELECT u.user_id, u.username 
        FROM User u
        JOIN FriendRequest fr ON (fr.user1_id = %s AND fr.user2_id = u.user_id) OR (fr.user2_id = %s AND fr.user1_id = u.user_id)
        WHERE fr.status = 'accepted';
        """
        cursor.execute(query, (user_id, user_id))
        friends = cursor.fetchall()
        cursor.close()

        if friends:
            for i, friend in enumerate(friends):
                friend_button = tk.Button(self.friends_frame, text=friend['username'], font=('Arial', 14), bg='white', fg='#118599')
                friend_button.pack(fill=tk.X, pady=5, padx=20)
        else:
            no_friends_label = tk.Label(self.friends_frame, text="You haven't added any friends yet.", bg='#118599', fg='white', font=('Arial', 14, 'italic'))
            no_friends_label.pack(pady=20)

################################# friend requesting #########################################

class FriendRequestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Friend Requests")
        self.root.geometry("360x640")
        self.connection = create_connection()  # Establish database connection

        self.requests_frame = tk.Frame(self.root, bg='#118599')
        self.requests_frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.requests_frame, text="Friend Requests", bg='#118599', fg='white', font=('Arial', 22, 'bold'))
        self.title_label.pack(pady=20)

        self.show_friend_requests()

    def show_friend_requests(self):
        cursor = self.connection.cursor(dictionary=True)
        user_id = config.current_user.user_id  # Use the current logged-in user's ID
        query = """
        SELECT u.user_id, u.username
        FROM User u
        JOIN FriendRequest fr ON fr.user1_id = u.user_id
        WHERE fr.user2_id = %s AND fr.status = 'pending';
        """
        cursor.execute(query, (user_id,))
        requests = cursor.fetchall()
        cursor.close()

        if requests:
            for i, request in enumerate(requests):
                request_label = tk.Label(self.requests_frame, text=request['username'], font=('Arial', 14), bg='white', fg='#118599')
                request_label.pack(fill=tk.X, pady=5, padx=20)
        else:
            no_requests_label = tk.Label(self.requests_frame, text="You have no friend requests.", bg='#118599', fg='white', font=('Arial', 14, 'italic'))
            no_requests_label.pack(pady=20)


# ############################### CHATTING GUI ##########################################

class SocialBondingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Bonding")
        self.root.geometry("360x640")
        
        self.connection = create_connection()  # Establish database connection

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True, padx=20, pady=20)

        # Top-right corner square for chat
        self.chat_button = tk.Button(self.main_frame, text="Chat", bg="white", command=self.open_chat)
        self.chat_button.place(x=300, y=0, width=50, height=50)

        # Buttons
        self.friends_button = tk.Button(self.main_frame, text="My Friends", bg="light blue", command=self.show_friends)
        self.friends_button.pack(fill=tk.X, pady=10)

        self.add_friends_button = tk.Button(self.main_frame, text="Add Friends", bg="light blue", command=self.add_friends)
        self.add_friends_button.pack(fill=tk.X, pady=10)

        self.people_near_me_button = tk.Button(self.main_frame, text="People Near Me", bg="light blue", command=self.show_people_near_me)
        self.people_near_me_button.pack(fill=tk.X, pady=10)

    def open_chat(self):
        # Implement the method to open chat
        root = tk.Toplevel(self.root)
        chat_app = ChattingGUI(root)
        root.mainloop()

    def show_friends(self):
        user_id = config.current_user['user_id']  # Use the current logged-in user's ID
        cursor = self.connection.cursor(dictionary=True)
        query = """
        SELECT u.user_id, u.username 
        FROM User u
        JOIN FriendRequest fr ON fr.user2_id = u.user_id
        WHERE fr.user1_id = %s AND fr.status = 'accepted'
        """
        cursor.execute(query, (user_id,))
        friends = cursor.fetchall()
        cursor.close()

        if friends:
            friends_window = tk.Toplevel(self.root)
            friends_window.title("My Friends")
            friends_window.geometry("300x400")

            for i, friend in enumerate(friends):
                friend_button = tk.Button(friends_window, text=friend['username'], command=lambda id=friend['user_id']: self.open_chat_with_friend(id))
                friend_button.pack(fill=tk.X, pady=5)
        else:
            messagebox.showinfo("No Friends", "You haven't added any friends yet.")

    def open_chat_with_friend(self, friend_id):
        root = tk.Toplevel(self.root)
        chat_app = ChattingGUI(root, friend_id)
        root.mainloop()

    def add_friends(self):
        # Implement the method to add friends
        messagebox.showinfo("Add Friends", "Navigating to add friends...")
        root = tk.Tk()
        app = FriendRequestGUI(root)
        root.mainloop()


    def show_people_near_me(self):
        # Implement the method to show people near me
        messagebox.showinfo("People Near Me", "Showing people near me...")

################################# CHATTING GUI ##########################################

class ChattingGUI:
    def __init__(self, root, friend_id=None):
        self.root = root
        self.root.title("Chatting")
        self.root.geometry("360x640")  # Set window size

        self.connection = create_connection()  # Establish database connection
        self.friend_id = friend_id

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True, padx=20, pady=20)

        tk.Label(self.main_frame, text="Chat with Friends", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        # Load friends of the current user
        self.friends = self.showFriends()

        if self.friends:
            self.showFriendsPage()
        else:
            self.noFriendsMsg()

    def areFriends(self, friend_id):
        # Function to check if selected user is a friend of the current user
        user_id = config.current_user['user_id']
        cursor = self.connection.cursor()
        query = "SELECT * FROM FriendRequest WHERE user1_id = %s AND user2_id = %s AND status = 'accepted'"
        cursor.execute(query, (user_id, friend_id))
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def showFriends(self):
        user_id = config.current_user['user_id']
        cursor = self.connection.cursor(dictionary=True)
        query = """
        SELECT u.user_id, u.username 
        FROM User u
        JOIN FriendRequest fr ON fr.user2_id = u.user_id
        WHERE fr.user1_id = %s AND fr.status = 'accepted'
        """
        cursor.execute(query, (user_id,))
        friends = cursor.fetchall()
        cursor.close()
        return friends

    def noFriendsMsg(self):
        # Function to display a message if the user has no friends yet
        messagebox.showinfo("No Friends", "You haven't added any friends yet.")

    def load_chat(self):
        # Implement the method to load chat history
        pass

    def loadChat(self, friend_id):
        # Function to load chat history between current user and selected friend
        user_id = config.current_user['user_id']
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM ChatMessage WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s) ORDER BY timestamp"
        cursor.execute(query, (user_id, friend_id, friend_id, user_id))
        messages = cursor.fetchall()
        cursor.close()
        return messages

    def returnMessages(self, friend_id):
        # Function to return messages exchanged with the selected friend
        messages = self.loadChat(friend_id)
        return messages

    def createChat(self, friend_id):
        # Function to create a chat window with the selected friend
        if not self.areFriends(friend_id):
            messagebox.showerror("Error", "You are not friends with this user.")
            return

        chat_window = tk.Toplevel(self.root)
        chat_window.title(f"Chat with {friend_id}")

        chat_frame = tk.Frame(chat_window)
        chat_frame.pack(expand=True, fill=tk.BOTH)

        self.chat_text = tk.Text(chat_frame, state=tk.DISABLED)
        self.chat_text.pack(expand=True, fill=tk.BOTH)

        entry_frame = tk.Frame(chat_window)
        entry_frame.pack(fill=tk.X)

        self.message_entry = tk.Entry(entry_frame)
        self.message_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5, pady=5)

        send_button = tk.Button(entry_frame, text="Send", command=lambda: self.sendMessages(friend_id))
        send_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.loadChat(friend_id)

    def sendMessages(self, friend_id):
        # Function to send a message to the selected friend
        message = self.message_entry.get()
        if self.emptyMsg(message):
            messagebox.showerror("Error", "The message can't be empty.")
            return

        user_id = config.current_user['user_id']
        cursor = self.connection.cursor()
        query = "INSERT INTO ChatMessage (sender_id, receiver_id, message_text) VALUES (%s, %s, %s)"
        cursor.execute(query, (user_id, friend_id, message))
        self.connection.commit()
        cursor.close()

        self.message_entry.delete(0, tk.END)
        self.updateChat(friend_id, message)

    def updateChat(self, friend_id, message):
        # Function to update chat history after sending a message
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, f"You: {message}\n")
        self.chat_text.config(state=tk.DISABLED)

    def emptyMsg(self, message):
        # Function to check if the message is empty
        return not message.strip()

    def showFriendsPage(self):
        # Function to display the friends page
        for i, friend in enumerate(self.friends):
            friend_button = tk.Button(self.main_frame, text=friend['username'], command=lambda id=friend['user_id']: self.createChat(id))
            friend_button.grid(row=1+i, column=0, columnspan=2, pady=5)

######################################################   classes marianthi
######################################################################
#####################################################    gia merge 


import tkinter as tk
from tkinter import messagebox
from db_connector import create_connection, close_connection
# from mainPage import mainPage
from tkinter import scrolledtext, Toplevel, Listbox, Button, Scrollbar
import config

# class Review:
#     def __init__(self, review_id=None, reviewer_id=None, reviewee_id=None, rating=None, review_text=None, review_date=None):
#         self.review_id = review_id
#         self.reviewer_id = reviewer_id
#         self.reviewee_id = reviewee_id
#         self.rating = rating
#         self.review_text = review_text
#         self.review_date = review_date

#     def save(self):
#         connection = create_connection()
#         cursor = connection.cursor()
#         if self.review_id is None:
#             try:
#                 cursor.execute(
#                     "INSERT INTO Review (reviewer_id, reviewee_id, rating, review_text) VALUES (%s, %s, %s, %s)", 
#                     (self.reviewer_id, self.reviewee_id, self.rating, self.review_text)
#                 )
#                 connection.commit()
#                 self.review_id = cursor.lastrowid
#                 print("Review added successfully")
#             except Exception as e:
#                 print(f"Error: {e}")
#                 connection.rollback()
#         else:
#             try:
#                 cursor.execute(
#                     "UPDATE Review SET reviewer_id=%s, reviewee_id=%s, rating=%s, review_text=%s WHERE review_id=%s",
#                     (self.reviewer_id, self.reviewee_id, self.rating, self.review_text, self.review_id)
#                 )
#                 connection.commit()
#                 print("Review updated successfully")
#             except Exception as e:
#                 print(f"Error: {e}")
#                 connection.rollback()
#             finally:
#                 cursor.close()
#                 close_connection(connection)

#     def delete(self):
#         connection = create_connection()
#         cursor = connection.cursor()
#         try:
#             cursor.execute("DELETE FROM Review WHERE review_id=%s", (self.review_id,))
#             connection.commit()
#             print("Review deleted successfully")
#         except Exception as e:
#             print(f"Error: {e}")
#             connection.rollback()
#         finally:
#             cursor.close()
#             close_connection(connection)

#     @classmethod
#     def get_all(cls):
#         connection = create_connection()
#         cursor = connection.cursor()
#         try:
#             cursor.execute("SELECT * FROM Review")
#             reviews = cursor.fetchall()
#             return [cls(*row) for row in reviews]
#         except Exception as e:
#             print(f"Error: {e}")
#             return []
#         finally:
#             cursor.close()
#             close_connection(connection)

#     @classmethod
#     def get_by_id(cls, review_id):
#         connection = create_connection()
#         cursor = connection.cursor()
#         try:
#             cursor.execute("SELECT * FROM Review WHERE review_id=%s", (review_id,))
#             row = cursor.fetchone()
#             if row:
#                 return cls(*row)
#             return None
#         except Exception as e:
#             print(f"Error: {e}")
#             return None
#         finally:
#             cursor.close()
#             close_connection(connection)


class Response:
    def __init__(self, response_id=None, review_id=None, replier_id=None, reply_text=None, reply_date=None):
        self.response_id = response_id
        self.review_id = review_id
        self.replier_id = replier_id
        self.reply_text = reply_text
        self.reply_date = reply_date

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        if self.response_id is None:
            try:
                cursor.execute(
                    "INSERT INTO Response (review_id, replier_id, reply_text) VALUES (%s, %s, %s)",
                    (self.review_id, self.replier_id, self.reply_text)
                )
                connection.commit()
                self.response_id = cursor.lastrowid
                print("Response added successfully")
                #cursor.execute("SELECT * FROM Review")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            try:
                cursor.execute(
                    "UPDATE Response SET review_id=%s, replier_id=%s, reply_text=%s WHERE response_id=%s",
                    (self.review_id, self.replier_id, self.reply_text, self.response_id)
                )
                connection.commit()
                print("Response updated successfully")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
            finally:
                cursor.close()
                close_connection(connection)

    def delete(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Response WHERE response_id=%s", (self.response_id,))
            connection.commit()
            print("Response deleted successfully")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_all(cls):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Response")
            responses = cursor.fetchall()
            return [cls(*row) for row in responses]
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_by_id(cls, response_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Response WHERE response_id=%s", (response_id,))
            row = cursor.fetchone()
            if row:
                return cls(*row)
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)

############################# Chat Models ########################################
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
        connection = create_connection()
        cursor = connection.cursor()
        try:
            if self.user_id is None:
                cursor.execute(
                    "INSERT INTO User (username, name, lastname, email, address, exact_address, password, role, membership_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (self.username, self.name, self.lastname, self.email, self.address, self.exact_address, self.password, self.role, self.membership_id)
                )
            else:
                cursor.execute(
                    "UPDATE User SET username=%s, name=%s, lastname=%s, email=%s, address=%s, exact_address=%s, password=%s, role=%s, membership_id=%s WHERE user_id=%s",
                    (self.username, self.name, self.lastname, self.email, self.address, self.exact_address, self.password, self.role, self.membership_id, self.user_id)
                )
            connection.commit()
            print("User saved successfully")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_by_username(username): # changed from user_id to username
        connection = create_connection()
        cursor = connection.cursor(dictionary=True) 
        try:
            cursor.execute("SELECT * FROM User WHERE username=%s", (username,))
            row = cursor.fetchone()
            if row:
                return cls(*row)
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)

    def send_message(self, receiver_id, message_text):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO ChatMessage (sender_id, receiver_id, message_text) VALUES (%s, %s, %s)",
                (self.user_id, receiver_id, message_text)
            )
            connection.commit()
            print("Message sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

class ChatMessage:
    def __init__(self, message_id=None, sender_id=None, receiver_id=None, message_text=None, sent_at=None):
        self.message_id = message_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message_text = message_text
        self.sent_at = sent_at

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            if self.message_id is None:
                cursor.execute(
                    "INSERT INTO ChatMessage (sender_id, receiver_id, message_text) VALUES (%s, %s, %s)",
                    (self.sender_id, self.receiver_id, self.message_text)
                )
            else:
                cursor.execute(
                    "UPDATE ChatMessage SET sender_id=%s, receiver_id=%s, message_text=%s WHERE message_id=%s",
                    (self.sender_id, self.receiver_id, self.message_text, self.message_id)
                )
            connection.commit()
            print("Chat message saved successfully")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_messages(cls, user_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM ChatMessage WHERE sender_id=%s OR receiver_id=%s",
                (user_id, user_id)
            )
            messages = []
            for (message_id, sender_id, receiver_id, message_text, sent_at) in cursor:
                messages.append(ChatMessage(message_id, sender_id, receiver_id, message_text, sent_at))
            return messages
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            close_connection(connection)


############################ MAKE_FRIENDS ########################################

class FriendRequest:
    def __init__(self, friendship_id=None, user1_id=None, user2_id=None, status='pending', requested_at=None, accepted_at=None):
        self.friendship_id = friendship_id
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.status = status
        self.requested_at = requested_at
        self.accepted_at = accepted_at

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            if self.friendship_id is None:
                cursor.execute(
                    "INSERT INTO FriendRequest (user1_id, user2_id, status, requested_at, accepted_at) VALUES (%s, %s, %s, %s, %s)",
                    (self.user1_id, self.user2_id, self.status, self.requested_at, self.accepted_at)
                )
            else:
                cursor.execute(
                    "UPDATE FriendRequest SET user1_id=%s, user2_id=%s, status=%s, requested_at=%s, accepted_at=%s WHERE friendship_id=%s",
                    (self.user1_id, self.user2_id, self.status, self.requested_at, self.accepted_at, self.friendship_id)
                )
            connection.commit()
            print("Friend request saved successfully")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_by_id(cls, friendship_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM FriendRequest WHERE friendship_id=%s", (friendship_id,))
            row = cursor.fetchone()
            if row:
                return cls(*row)
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_by_users(cls, user1_id, user2_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM FriendRequest WHERE (user1_id=%s AND user2_id=%s) OR (user1_id=%s AND user2_id=%s)",
                (user1_id, user2_id, user2_id, user1_id)
            )
            row = cursor.fetchone()
            if row:
                return cls(*row)
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)

# beneficiary #########################################################################################

class Beneficiary:
    def __init__(self, beneficiary_id=None, user_id=None, beneficiary_type=None, date_of_birth=None, address=None, contact_number=None, location_id=None):
        self.beneficiary_id = beneficiary_id
        self.user_id = user_id
        self.beneficiary_type = beneficiary_type
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_number = contact_number
        self.location_id = location_id

    @classmethod
    def get_all(cls):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Beneficiary")
            beneficiaries = cursor.fetchall()
            return [cls(*row) for row in beneficiaries]
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            close_connection(connection)


    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            if self.beneficiary_id is None:
                cursor.execute(
                    "INSERT INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number, location_id) VALUES (%s, %s, %s, %s, %s, %s)",
                    (self.user_id, self.beneficiary_type, self.date_of_birth, self.address, self.contact_number, self.location_id)
                )
            else:
                cursor.execute(
                    "UPDATE Beneficiary SET user_id=%s, beneficiary_type=%s, date_of_birth=%s, address=%s, contact_number=%s, location_id=%s WHERE beneficiary_id=%s",
                    (self.user_id, self.beneficiary_type, self.date_of_birth, self.address, self.contact_number, self.location_id, self.beneficiary_id)
                )
            connection.commit()
            print("Beneficiary saved successfully")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_by_user_id(cls, user_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Beneficiary WHERE user_id=%s", (user_id,))
            row = cursor.fetchone()
            if row:
                return cls(*row)
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)

########################################################## REVIEW GUI ##########################################################

class ReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Review Publication System")
        self.root.geometry("360x640")  # Set window size to simulate a phone screen

        self.review_frame = tk.Frame(root, bg='#118599')
        self.review_frame.pack(fill=tk.BOTH, expand=True)

        # Add empty rows at the top to lower the content
        for i in range(5):
            self.review_frame.grid_rowconfigure(i, minsize=10)

        tk.Label(self.review_frame,text="Please let us know about your experience!", bg='#118599', fg='white',font=('Arial',22,'bold'),wraplength=360,anchor='w',justify='left').grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="ew")
        tk.Label(self.review_frame,text="Leave your feedback and help us improve our services", bg='#118599', fg='white',font=('Arial',16),wraplength=360,anchor='w',justify='left').grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="ew")


        # Add empty rows at the top to lower the content
        for i in range(5):
            self.review_frame.grid_rowconfigure(i, minsize=20)

        tk.Label(self.review_frame, text="Rate Service:", bg='#118599', fg='white',font=('Arial',14,'bold')).grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.rating_var = tk.IntVar()
        self.rating_var.set(0)  # Default rating to 0 stars

        self.stars = []
        for i in range(5):
            star = tk.Button(self.review_frame, text="★", font=("Arial", 8), command=lambda i=i: self.set_rating(i+1))
            star.grid(row=6, column=i+1, padx=1, pady=1)
            self.stars.append(star)

        tk.Label(self.review_frame, text="Write a Review:", bg='#118599', fg='white',font=('Arial',14,'bold')).grid(row=7, column=0, padx=5, pady=5, sticky='nw')
        self.review_text = tk.Text(self.review_frame, width=30, height=8)
        self.review_text.grid(row=8, column=0, columnspan=6, padx=5, pady=5, sticky='w')

        self.submit_button = tk.Button(self.review_frame, text="Submit", command=self.create_review, bg="green", fg="white")
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

    def checkLength(self): #check if length surpasses 100 characters 
        if len(self.review_text.get("1.0", tk.END)) > 100:
            messagebox.showerror("Error", "Review text should not exceed 100 characters")
            return False
        return True

    def validateReview(self):
        self.checkLength()
        self.checkStars()

    def create_review(self):
        # reviewer_id = self.reviewer_id_entry.get()
        reviewer_id= 1
        # reviewee_id = self.reviewee_id_entry.get()
        reviewee_id = 2
        rating = self.rating_var.get()
        review_text = self.review_text.get("1.0", tk.END)

        if not reviewer_id or not reviewee_id or not review_text:
            messagebox.showerror("Error", "All fields are required")
            return
        else:
            self.validateReview()

        try:
            review = Review(reviewer_id=int(reviewer_id), reviewee_id=int(reviewee_id), rating=int(rating), review_text=review_text)
            review.save()
            messagebox.showinfo("Success", "Review created successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create review: {e}")


########################################### ENTER DESTINATION ############################################################


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
                mainPage()
            else:
                messagebox.showerror("Error", "City not found in the specified country")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            cursor.close()
            connection.close()

############################################# FRIEND REQUESTING #############################################################################

# class FriendRequestGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Friend Request System")
#         self.root.geometry("400x300")  # Set window size

#         self.connection = create_connection()  # Establish database connection

#         self.main_frame = tk.Frame(root)
#         self.main_frame.pack(expand=True, padx=20, pady=20)

#         tk.Label(self.main_frame, text="Add Friends", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

#         self.search_entry = tk.Entry(self.main_frame, width=30)
#         self.search_entry.grid(row=1, column=0, columnspan=2, pady=10)

#         self.search_button = tk.Button(self.main_frame, text="Search", command=self.searchByUsername)
#         self.search_button.grid(row=2, column=0, pady=10)

#         self.add_button = tk.Button(self.main_frame, text="Add Friend", command=self.send_request)
#         self.add_button.grid(row=2, column=1, pady=10)

#         self.showAddFriends_button = tk.Button(self.main_frame, text="Load Friends", command=self.showAddFriends)
#         self.showAddFriends_button.grid(row=3, column=0, columnspan=2, pady=10)
        
#         self.load_recommendations_button = tk.Button(self.main_frame, text="Load Recommended Friends", command=self.fetchRecommendedFriends)
#         self.load_recommendations_button.grid(row=4, column=0, columnspan=2, pady=10)

#     def searchByUsername(self):
#         username = self.search_entry.get()
#         if not username:
#             messagebox.showerror("Error", "Please enter a username")
#         else:
#             cursor = self.connection.cursor()
#             query = "SELECT * FROM User WHERE username = %s"
#             cursor.execute(query, (username,))
#             user = cursor.fetchone()  # Fetch the results
#             cursor.close()  # Close the cursor after fetching results

#             if user:
#                 messagebox.showinfo("Info", f"User {username} found")
#             else:
#                 messagebox.showerror("Error", f"User {username} not found")

#     def sendFriendRequest(self):    #kanonika prepei prwta na mpoume sto profil tou kathe xrhsth kai meta na kanoume to request
#         username = self.search_entry.get()
#         if not username:
#             messagebox.showerror("Error", "Please enter a username")
#             return

#         cursor = self.connection.cursor()
#         query = "SELECT user_id FROM User WHERE username = %s"
#         cursor.execute(query, (username,))
#         recipient = cursor.fetchone()
#         cursor.close()

#         if recipient:
#             recipient_id = recipient[0]
#             sender_id = config.current_user['user_id']  # Use the current logged-in user's ID
#             cursor = self.connection.cursor()
#             query = "INSERT INTO FriendRequest (user1_id, user2_id) VALUES (%s, %s)"
#             cursor.execute(query, (sender_id, recipient_id))
#             self.connection.commit()
#             cursor.close()
#             messagebox.showinfo("Info", f"Friend request sent to {username}")
#         else:
#             messagebox.showerror("Error", f"User {username} not found")

#     def showAddFriends(self):
#         user_id = config.current_user['user_id']  # Use the current logged-in user's ID
#         cursor = self.connection.cursor()
#         query = """
#         SELECT u.username FROM FriendRequest fr
#         JOIN User u ON fr.user2_id = u.user_id
#         WHERE fr.user1_id = %s AND fr.status = 'accepted'
#         """
#         cursor.execute(query, (config.current_user['user_id'],))
#         friends = cursor.fetchall()
#         cursor.close()

#         friends_list = [friend[0] for friend in friends]
#         messagebox.showinfo("Friends List", "\n".join(friends_list) if friends_list else "You have no friends added yet.")


#     def fetchRecommendedFriends(self):
#         # Fetch recommended friends who are not already friends with the current user
#         user_id = config.current_user['user_id']
#         cursor = self.connection.cursor(dictionary=True)

#         # Query to select recommended friends who are not already friends with the current user
#         query = """
#         SELECT u.user_id, u.username 
#         FROM User u
#         WHERE u.user_id NOT IN (
#             SELECT user2_id 
#             FROM FriendRequest 
#             WHERE user1_id = %s
#         ) AND u.user_id != %s
#         LIMIT 2
#         """
#         cursor.execute(query, (user_id, user_id))

#         recommended_friends = cursor.fetchall()
#         cursor.close()

#         if recommended_friends:
#             for i, friend in enumerate(recommended_friends):
#                 # Create buttons for recommended friends
#                 friend_button = tk.Button(self.main_frame, text=friend['username'], command=lambda id=friend['user_id']: self.sendFriendRequest(id))
#                 friend_button.grid(row=5+i, column=0, columnspan=2, pady=5)
#         else:
#             messagebox.showinfo("Recommended Friends", "No recommended friends found.")

class FriendRequestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Friend Request System")
        self.root.geometry("400x300")  # Set window size

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
        WHERE u.user_id NOT IN (
            SELECT user2_id 
            FROM FriendRequest 
            WHERE user1_id = %s
        ) AND u.user_id != %s
        LIMIT 2
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

    def show_people_near_me(self):
        # Implement the method to show people near me
        messagebox.showinfo("People Near Me", "Showing people near me...")

class ChattingGUI:
    def __init__(self, root, friend_id=None):
        self.root = root
        self.root.title("Chatting")
        self.root.geometry("400x300")  # Set window size

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

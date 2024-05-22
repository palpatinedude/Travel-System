import tkinter as tk
from tkinter import messagebox
from db_connector import create_connection, close_connection
from mainPage import mainPage
from tkinter import scrolledtext

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
            self.checkStars()
            self.checkLength()

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

############################################# CHAT #############################################################################


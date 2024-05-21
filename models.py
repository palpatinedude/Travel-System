import tkinter as tk
from tkinter import messagebox
from db_connector import create_connection, close_connection

class Review:
    def __init__(self, review_id=None, reviewer_id=None, reviewee_id=None, rating=None, review_text=None, review_date=None):
        self.review_id = review_id
        self.reviewer_id = reviewer_id
        self.reviewee_id = reviewee_id
        self.rating = rating
        self.review_text = review_text
        self.review_date = review_date

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        if self.review_id is None:
            try:
                cursor.execute(
                    "INSERT INTO Review (reviewer_id, reviewee_id, rating, review_text) VALUES (%s, %s, %s, %s)", 
                    (self.reviewer_id, self.reviewee_id, self.rating, self.review_text)
                )
                connection.commit()
                self.review_id = cursor.lastrowid
                print("Review added successfully")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            try:
                cursor.execute(
                    "UPDATE Review SET reviewer_id=%s, reviewee_id=%s, rating=%s, review_text=%s WHERE review_id=%s",
                    (self.reviewer_id, self.reviewee_id, self.rating, self.review_text, self.review_id)
                )
                connection.commit()
                print("Review updated successfully")
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
            cursor.execute("DELETE FROM Review WHERE review_id=%s", (self.review_id,))
            connection.commit()
            print("Review deleted successfully")
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
            cursor.execute("SELECT * FROM Review")
            reviews = cursor.fetchall()
            return [cls(*row) for row in reviews]
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_by_id(cls, review_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Review WHERE review_id=%s", (review_id,))
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
    def __init__(self, user_id=None, username=None, name=None, lastname=None, email=None, address=None, exact_address=None, password=None, role=None, membership_id=None):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.lastname = lastname
        self.email = email
        self.address = address
        self.exact_address = exact_address
        self.password = password
        self.role = role
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
    def get_by_username(cls, username): # changed from user_id to username
        connection = create_connection()
        cursor = connection.cursor()
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

        self.review_frame = tk.Frame(root)
        self.review_frame.pack(pady=10)

        tk.Label(self.review_frame, text="Reviewer ID:").grid(row=0, column=0, padx=5, pady=5)
        self.reviewer_id_entry = tk.Entry(self.review_frame)
        self.reviewer_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.review_frame, text="Reviewee ID:").grid(row=1, column=0, padx=5, pady=5)
        self.reviewee_id_entry = tk.Entry(self.review_frame)
        self.reviewee_id_entry.grid(row=1, column=1, padx=5, pady=5)

        # tk.Label(self.review_frame, text="Rating:").grid(row=2, column=0, padx=5, pady=5)     #gia rating se text 1~5
        # self.rating_entry = tk.Entry(self.review_frame)
        # self.rating_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.review_frame, text="Rate Service:").grid(row=2, column=0, padx=5, pady=5)
        self.rating_var = tk.IntVar()
        self.rating_var.set(0)  # Default rating to 0 stars

        self.stars = []
        for i in range(5):
            star = tk.Button(self.review_frame, text="★", font=("Arial", 20), command=lambda i=i: self.set_rating(i+1))
            star.grid(row=2, column=i+1, padx=2, pady=5)
            self.stars.append(star)

        tk.Label(self.review_frame, text="Write a Review:").grid(row=3, column=0, padx=5, pady=5)
        self.review_text_entry = tk.Entry(self.review_frame)
        self.review_text_entry.grid(row=3, column=2, padx=5, pady=5)

        self.create_review_button = tk.Button(self.review_frame, text="Submit", command=self.create_review)
        self.create_review_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.display_reviews_button = tk.Button(self.review_frame, text="Display Reviews", command=self.display_reviews)
        self.display_reviews_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.review_listbox = tk.Listbox(root, width=80)
        self.review_listbox.pack(pady=10)

        self.response_frame = tk.Frame(root)
        self.response_frame.pack(pady=10)

        tk.Label(self.response_frame, text="Review ID:").grid(row=0, column=0, padx=5, pady=5)
        self.review_id_entry = tk.Entry(self.response_frame)
        self.review_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.response_frame, text="Replier ID:").grid(row=1, column=0, padx=5, pady=5)
        self.replier_id_entry = tk.Entry(self.response_frame)
        self.replier_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.response_frame, text="Reply Text:").grid(row=2, column=0, padx=5, pady=5)
        self.reply_text_entry = tk.Entry(self.response_frame)
        self.reply_text_entry.grid(row=2, column=1, padx=5, pady=5)

        self.create_response_button = tk.Button(self.response_frame, text="Create Response", command=self.create_response)
        self.create_response_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.display_responses_button = tk.Button(self.response_frame, text="Display Responses", command=self.display_responses)
        self.display_responses_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.response_listbox = tk.Listbox(root, width=80)
        self.response_listbox.pack(pady=10)

    def set_rating(self, rating):
        self.rating_var.set(rating)
        for i in range(5):
            if i < rating:
                self.stars[i].config(fg="gold")
            else:
                self.stars[i].config(fg="black")

    def create_review(self):
        reviewer_id = self.reviewer_id_entry.get()
        reviewee_id = self.reviewee_id_entry.get()
        rating = self.rating_var.get()
        review_text = self.review_text_entry.get()

        if not reviewer_id or not reviewee_id or not rating or not review_text:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            review = Review(reviewer_id=int(reviewer_id), reviewee_id=int(reviewee_id), rating=int(rating), review_text=review_text)
            review.save()
            messagebox.showinfo("Success", "Review created successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create review: {e}")

    def display_reviews(self):
        self.review_listbox.delete(0, tk.END)
        reviews = Review.get_all()
        for review in reviews:
            self.review_listbox.insert(tk.END, f"ID: {review.review_id}, Reviewer: {review.reviewer_id}, Reviewee: {review.reviewee_id}, Rating: {review.rating}, Text: {review.review_text}")

    def create_response(self):
        review_id = self.review_id_entry.get()
        replier_id = self.replier_id_entry.get()
        reply_text = self.reply_text_entry.get()

        if not review_id or not replier_id or not reply_text:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            response = Response(review_id=int(review_id), replier_id=int(replier_id), reply_text=reply_text)
            response.save()
            messagebox.showinfo("Success", "Response created successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create response: {e}")

    def display_responses(self):
        self.response_listbox.delete(0, tk.END)
        responses = Response.get_all()
        for response in responses:
            self.response_listbox.insert(tk.END, f"ID: {response.response_id}, Review ID: {response.review_id}, Replier: {response.replier_id}, Text: {response.reply_text}")

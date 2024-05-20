import sys
import os
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from models import Review, Response, User

# # #connect to MySQL
# # mydb = mysql.connector.connect(
# # host="localhost",
# # user="root",
# # passwd="4655",
# # database="od"
# # )

# # #check if connection is established         #testing 
# # if (mydb):
# #     print("Connection Successful")
# # else:
# #     print("Connection Unsuccessful")

# # #creating a cursor object using the cursor() method
# # mycursor = mydb.cursor() #cursor object which is used to interact with the database

# ########################################################################################################


class ReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Review and Response Management")

        self.review_frame = tk.Frame(root)
        self.review_frame.pack(pady=10)

        tk.Label(self.review_frame, text="Reviewer ID:").grid(row=0, column=0, padx=5, pady=5)
        self.reviewer_id_entry = tk.Entry(self.review_frame)
        self.reviewer_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.review_frame, text="Reviewee ID:").grid(row=1, column=0, padx=5, pady=5)
        self.reviewee_id_entry = tk.Entry(self.review_frame)
        self.reviewee_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.review_frame, text="Rating:").grid(row=2, column=0, padx=5, pady=5)
        self.rating_entry = tk.Entry(self.review_frame)
        self.rating_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.review_frame, text="Review Text:").grid(row=3, column=0, padx=5, pady=5)
        self.review_text_entry = tk.Entry(self.review_frame)
        self.review_text_entry.grid(row=3, column=1, padx=5, pady=5)

        self.create_review_button = tk.Button(self.review_frame, text="Create Review", command=self.create_review)
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

    def create_review(self):
        reviewer_id = self.reviewer_id_entry.get()
        reviewee_id = self.reviewee_id_entry.get()
        rating = self.rating_entry.get()
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

if __name__ == "__main__":
    root = tk.Tk()
    app = ReviewApp(root)
    root.mainloop()

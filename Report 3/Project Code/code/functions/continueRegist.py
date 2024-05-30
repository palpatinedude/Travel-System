import sys
sys.path.append('../classes/')
sys.path.append('../database/')
import tkinter as tk
from tkinter import messagebox
from dbConnection import create_connection
import datetime
import random
import string
import barcode
from barcode.writer import ImageWriter
from allClasses import Membership, Card, Points

def generate_isbn13_barcode():
    # generate a random 12-digit number exclude the check digit
    random_number = ''.join(random.choices(string.digits, k=12))

    # calculate the check digit for the random number
    check_digit = sum(int(digit) * (3 if i % 2 else 1) for i, digit in enumerate(random_number[::-1])) % 10
    check_digit = (10 - check_digit) % 10

    # concatenate the random number and the check digit to get the full number
    isbn13_number = random_number + str(check_digit)

    # generate the barcode image
    ean = barcode.get_barcode_class('ean13')
    ean_barcode = ean(isbn13_number, writer=ImageWriter())
    barcode_filename = ean_barcode.save('isbn13_barcode')

    return isbn13_number, barcode_filename

def generate_unique_card_number(cursor):
    while True:
        card_number = ''.join(random.choices(string.digits, k=16))
        cursor.execute("SELECT card_id FROM Card WHERE cardnumber = %s", (card_number,))
        if cursor.fetchone() is None:
            return card_number

def calculate_expiration_date(duration):
    if duration == 'Monthly':
        return datetime.date.today() + datetime.timedelta(days=30)
    elif duration == '6-monthly':
        return datetime.date.today() + datetime.timedelta(days=180)
    elif duration == 'One year':
        return datetime.date.today() + datetime.timedelta(days=365)
    else:
        raise ValueError("Invalid duration")

def continueRegistration(selected_membership, user_id, duration):
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                # create a membership instance
                membership = Membership(
                    membership_type=selected_membership,
                    duration=duration,
                    membership_status="Active",
                    created_date=datetime.date.today()
                )

                # insert membership details into the database
                membership.save()
                membership_id = membership.membership_id

                # assign membership to user
                cursor.execute("UPDATE User SET membership_id = %s WHERE user_id = %s", (membership_id, user_id))

                # beneficiary_id associated with user_id
                cursor.execute("SELECT beneficiary_id FROM Beneficiary WHERE user_id = %s", (user_id,))
                beneficiary_id = cursor.fetchone()[0]

                # generate and insert card details only for basic and premium memberships
                if selected_membership in ['Basic', 'Premium']:
                    # generate unique card number and barcode
                    card_number = generate_unique_card_number(cursor)
                    isbn13_number, barcode_filename = generate_isbn13_barcode()

                    # calculate expiration date
                    expiration_date = calculate_expiration_date(duration)
                    print("edw einai h karta")
                    # card instance
                    card = Card(beneficiary_id=beneficiary_id, cardnumber=card_number, barcode=isbn13_number, expiration_date=expiration_date)

                    # insert card details into the database
                    card.save()

                    # fetch card_id after inserting the card record
                    card_id = card.card_id

                    # points instance for initial points entry
                    initial_points = 0
                    points = Points(card_id=card_id, points=initial_points, available_coupons='')

                    # insert initial points entry into the database
                    points.save()

                connection.commit()
                messagebox.showinfo("Membership Assigned", f"{selected_membership} membership has been assigned to the user.")
                return True
        except Exception as e:
            connection.rollback()
            messagebox.showerror("Error", f"Failed to assign membership and issue card: {e}")
            return False
        finally:
            connection.close()
    else:
        messagebox.showerror("Database Error", "Failed to connect to the database.")
        return False

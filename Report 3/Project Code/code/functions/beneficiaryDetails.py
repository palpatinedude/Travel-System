import sys
sys.path.append('../classes/')
import re
from dbConnection import create_connection
from datetime import datetime
from tkinter import messagebox
from allClasses import  SimpleUser, ServiceProvider


def beneficiaryDetails(user_id, beneficiary_type, dob_entry, address_entry, contact_number_entry, additional_entries, window):
    dob = dob_entry.get()
    address = address_entry.get()
    contact_number = contact_number_entry.get()

    if not all([dob, address, contact_number]):
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    try:
        dob = datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Input Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    if not re.match(r'^[0-9+\-\(\)\s]+$', contact_number):
        messagebox.showerror("Input Error", "Invalid contact number. Please use only digits, spaces, hyphens, and parentheses.")
        return    

    connection = create_connection()
    cursor = connection.cursor()

    try:
        # ppdate beneficiary table
        beneficiary_query = """
        UPDATE Beneficiary 
        SET date_of_birth = %s, address = %s, contact_number = %s
        WHERE user_id = %s
        """
        cursor.execute(beneficiary_query, (dob, address, contact_number, user_id))
        connection.commit()

        cursor.execute("SELECT beneficiary_id FROM Beneficiary WHERE user_id = %s", (user_id,))
        beneficiary_id = cursor.fetchone()[0] 

        # insert into specific role  table
        if beneficiary_type == "Simple User":
            bistory, preferences = additional_entries
            simple_user = SimpleUser(beneficiary_id=beneficiary_id, bistory=bistory, preferences=preferences)
            simple_user.save()
        elif beneficiary_type == "Service Provider":
            languages_spoken, specialties, certifications = additional_entries
            service_provider = ServiceProvider(beneficiary_id=beneficiary_id, languages_spoken=languages_spoken, specialties=specialties, certifications=certifications)
            service_provider.save()

        messagebox.showinfo("Success", "Beneficiary details saved successfully.")
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

    window.destroy()
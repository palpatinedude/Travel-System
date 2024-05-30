import sys
sys.path.append('../classes/')
import re
from db_connector import create_connection
from datetime import datetime
from tkinter import messagebox
from allClasses import SimpleUser, ServiceProvider, Beneficiary


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
        beneficiary = Beneficiary.get_by_id(user_id)
        print("edw eimai sto beneficiaryDetails.py")
        if beneficiary:
            beneficiary.update(date_of_birth=dob, address=address, contact_number=contact_number)
            beneficiary_id = beneficiary.beneficiary_id
            if beneficiary_type == "Simple User":
                bistory, preferences = additional_entries
                simple_user = SimpleUser(beneficiary_id=beneficiary_id, bistory=bistory, preferences=preferences)
                simple_user.save()
            elif beneficiary_type == "Service Provider":
                languages_spoken, specialties, certifications = additional_entries
                service_provider = ServiceProvider(beneficiary_id=beneficiary_id, languages_spoken=languages_spoken, specialties=specialties, certifications=certifications)
                service_provider.save()

            messagebox.showinfo("Success", "Beneficiary details saved successfully.")
        else:
            messagebox.showerror("Error", "Beneficiary not found.")
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        connection.close()
        window.destroy()
import sys
sys.path.append('../classes/')
sys.path.append('../database/')
from db_connector import create_connection
from tkinter import messagebox
from allClasses import BusinessPartner

def partnerDetails(user_id, tax_code_entry, registration_number_entry, website_entry, description_entry, window):
    tax_code = tax_code_entry.get()
    registration_number = registration_number_entry.get()
    website = website_entry.get()
    description = description_entry.get("1.0", tk.END).strip()

    if not all([tax_code, registration_number, website, description]):
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    partner = BusinessPartner(user_id, tax_code, registration_number, website, description)
    result = partner.save()

    if result:
        messagebox.showinfo("Success", "Partner details saved successfully.")
        window.destroy()
    else:
        messagebox.showerror("Database Error", "An error occurred while saving partner details.")
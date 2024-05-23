import tkinter as tk
from tkinter import messagebox
from dbConnection import create_connection
from datetime import datetime
import re

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
        # update Beneficiary table
        beneficiary_query = """
        UPDATE Beneficiary 
        SET date_of_birth = %s, address = %s, contact_number = %s
        WHERE user_id = %s
        """
        cursor.execute(beneficiary_query, (dob, address, contact_number, user_id))
        connection.commit()
       # messagebox.showinfo("Success", "Beneficiary details updated successfully.")

        cursor.execute("SELECT beneficiary_id FROM Beneficiary WHERE user_id = %s", (user_id,))
        beneficiary_id = cursor.fetchone()[0] 

        # insert into role-specific table
        if beneficiary_type == "Simple User":
            bistory, preferences = additional_entries
            simple_user_query = """
            INSERT INTO SimpleUser (beneficiary_id, bistory, preferences)
            VALUES (%s, %s, %s)
            """
            cursor.execute(simple_user_query, (beneficiary_id, bistory, preferences))
        elif beneficiary_type == "Service Provider":
            languages_spoken, specialties, certifications = additional_entries
            service_provider_query = """
            INSERT INTO ServiceProvider (beneficiary_id, languages_spoken, specialties, certifications)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(service_provider_query, (beneficiary_id, languages_spoken, specialties, certifications))

        connection.commit()
        messagebox.showinfo("Success", "Beneficiary details saved successfully.")
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

    window.destroy()

def beneficiaryWindow(role, user_id):
    beneficiary_window = tk.Tk()
    beneficiary_window.title("Beneficiary Details")
    beneficiary_window.configure(bg="pink")  
    print(user_id)

    # set window dimensions similar to a phone screen
    phone_width = 360
    phone_height = 640
    beneficiary_window.geometry(f"{phone_width}x{phone_height}")

    tk.Label(beneficiary_window, text="Date of Birth (YYYY-MM-DD):", font=("Arial", 9), bg="pink").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(beneficiary_window, text="Address:", font=("Arial", 9), bg="pink").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(beneficiary_window, text="Contact Number:", font=("Arial", 9), bg="pink").grid(row=2, column=0, padx=10, pady=10)
    
    dob_entry = tk.Entry(beneficiary_window, font=("Arial", 9))
    address_entry = tk.Entry(beneficiary_window, font=("Arial", 9))
    contact_number_entry = tk.Entry(beneficiary_window, font=("Arial", 9))
    
    dob_entry.grid(row=0, column=1, padx=10, pady=10)
    address_entry.grid(row=1, column=1, padx=10, pady=10)
    contact_number_entry.grid(row=2, column=1, padx=10, pady=10)

    additional_entries = []

    if role == "Simple User":
        tk.Label(beneficiary_window, text="Bistory:", font=("Arial", 9), bg="pink").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(beneficiary_window, text="Preferences:", font=("Arial", 9), bg="pink").grid(row=4, column=0, padx=10, pady=10)

        bistory_entry = tk.Entry(beneficiary_window, font=("Arial", 9))
        preferences_entry = tk.Entry(beneficiary_window, font=("Arial", 9))

        bistory_entry.grid(row=3, column=1, padx=10, pady=10)
        preferences_entry.grid(row=4, column=1, padx=10, pady=10)

        additional_entries = [bistory_entry, preferences_entry]

    elif role == "Service Provider":
        tk.Label(beneficiary_window, text="Languages Spoken:", font=("Arial", 9), bg="pink").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(beneficiary_window, text="Specialties:", font=("Arial", 9), bg="pink").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(beneficiary_window, text="Certifications:", font=("Arial", 9), bg="pink").grid(row=5, column=0, padx=10, pady=10)

        languages_spoken_entry = tk.Entry(beneficiary_window, font=("Arial", 9))
        specialties_entry = tk.Entry(beneficiary_window, font=("Arial", 9))
        certifications_entry = tk.Entry(beneficiary_window, font=("Arial", 9))

        languages_spoken_entry.grid(row=3, column=1, padx=10, pady=10)
        specialties_entry.grid(row=4, column=1, padx=10, pady=10)
        certifications_entry.grid(row=5, column=1, padx=10, pady=10)

        additional_entries = [languages_spoken_entry, specialties_entry, certifications_entry]

    save_button = tk.Button(
        beneficiary_window, 
        text="Save", 
        command=lambda: beneficiaryDetails(
            user_id, role, dob_entry, address_entry, contact_number_entry, 
            [entry.get() for entry in additional_entries],
            beneficiary_window
        ), 
        font=("Arial", 9)
    )
    save_button.grid(row=6, columnspan=2, pady=20)
    
    beneficiary_window.mainloop()
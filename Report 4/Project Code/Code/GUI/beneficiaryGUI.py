import sys
sys.path.append('Report 4/Project Code/Code/functions')
sys.path.append('Report 4/Project Code/Code/classes')
import tkinter as tk
from tkinter import messagebox
from beneficiaryDetails import beneficiaryDetails

def beneficiaryWindow(role, user_id):
    beneficiary_window = tk.Tk()
    beneficiary_window.title("Beneficiary Details")
    beneficiary_window.configure(bg="pink")  
    print(user_id)

    # set window dimensions similar to a phone screen
    phone_width = 360
    phone_height = 640
    beneficiary_window.geometry(f"{phone_width}x{phone_height}")

    # add title at the top
    tk.Label(beneficiary_window, text="Beneficiary Details", font=("Arial", 14, "bold"), bg="pink").grid(row=0, column=0, columnspan=2, pady=(20, 10))

    tk.Label(beneficiary_window, text="Date of Birth (YYYY-MM-DD):", font=("Arial", 10), bg="pink").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(beneficiary_window, text="Address:", font=("Arial", 10), bg="pink").grid(row=2, column=0, padx=10, pady=10)
    tk.Label(beneficiary_window, text="Contact Number:", font=("Arial", 10), bg="pink").grid(row=3, column=0, padx=10, pady=10)
    
    dob_entry = tk.Entry(beneficiary_window, font=("Arial", 10))
    address_entry = tk.Entry(beneficiary_window, font=("Arial", 10))
    contact_number_entry = tk.Entry(beneficiary_window, font=("Arial", 10))
    
    dob_entry.grid(row=1, column=1, padx=10, pady=25)
    address_entry.grid(row=2, column=1, padx=10, pady=25)
    contact_number_entry.grid(row=3, column=1, padx=10, pady=25)

    additional_entries = []

    if role == "Simple User":
        tk.Label(beneficiary_window, text="Bistory:", font=("Arial", 10), bg="pink").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(beneficiary_window, text="Preferences:", font=("Arial", 10), bg="pink").grid(row=5, column=0, padx=10, pady=10)

        bistory_entry = tk.Entry(beneficiary_window, font=("Arial", 10))
        preferences_entry = tk.Entry(beneficiary_window, font=("Arial", 10))

        bistory_entry.grid(row=4, column=1, padx=10, pady=25)
        preferences_entry.grid(row=5, column=1, padx=10, pady=25)

        additional_entries = [bistory_entry, preferences_entry]

    elif role == "Service Provider":
        tk.Label(beneficiary_window, text="Languages Spoken:", font=("Arial", 10), bg="pink").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(beneficiary_window, text="Specialties:", font=("Arial", 10), bg="pink").grid(row=5, column=0, padx=10, pady=10)
        tk.Label(beneficiary_window, text="Certifications:", font=("Arial", 10), bg="pink").grid(row=6, column=0, padx=10, pady=10)

        languages_spoken_entry = tk.Entry(beneficiary_window, font=("Arial", 10))
        specialties_entry = tk.Entry(beneficiary_window, font=("Arial", 10))
        certifications_entry = tk.Entry(beneficiary_window, font=("Arial", 10))

        languages_spoken_entry.grid(row=4, column=1, padx=10, pady=25)
        specialties_entry.grid(row=5, column=1, padx=10, pady=25)
        certifications_entry.grid(row=6, column=1, padx=10, pady=25)

        additional_entries = [languages_spoken_entry, specialties_entry, certifications_entry]

    save_button = tk.Button(
        beneficiary_window, 
        text="Save", 
        command=lambda: beneficiaryDetails(
            user_id, role, dob_entry, address_entry, contact_number_entry, 
            [entry.get() for entry in additional_entries],
            beneficiary_window
        ), 
        font=("Arial", 10),
        width=26,  
        height=2 , 
        bg="#808080",  
        fg="white"  
    )
    save_button.grid(row=7, columnspan=2, pady=85)
    
    beneficiary_window.mainloop()
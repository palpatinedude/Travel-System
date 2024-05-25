import tkinter as tk
from tkinter import messagebox
from partnerDetails import partnerDetails

def partnerWindow(role, user_id):
    partner_window = tk.Tk()
    partner_window.title("Partner Details")
    partner_window.configure(bg="lightblue")

    phone_width = 360
    phone_height = 640
    partner_window.geometry(f"{phone_width}x{phone_height}")

    # labels
    tax_code_label = tk.Label(partner_window, text="Tax Code:", font=("Arial", 10), bg="lightblue")
    registration_number_label = tk.Label(partner_window, text="Registration Number:", font=("Arial", 10), bg="lightblue")
    website_label = tk.Label(partner_window, text="Website:", font=("Arial", 10), bg="lightblue")
    description_label = tk.Label(partner_window, text="Description:", font=("Arial", 10), bg="lightblue")

    tax_code_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    registration_number_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    website_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    description_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    # entry 
    tax_code_entry = tk.Entry(partner_window, font=("Arial", 10))
    registration_number_entry = tk.Entry(partner_window, font=("Arial", 10))
    website_entry = tk.Entry(partner_window, font=("Arial", 10))
    description_entry = tk.Text(partner_window, font=("Arial", 10), wrap="word", height=7, width=20)

    tax_code_entry.grid(row=0, column=1, padx=10, pady=5)
    registration_number_entry.grid(row=1, column=1, padx=10, pady=5)
    website_entry.grid(row=2, column=1, padx=10, pady=5)
    description_entry.grid(row=3, column=1, padx=10, pady=5)


    save_button = tk.Button(partner_window, text="Save", command=lambda: partnerDetails(
        user_id, tax_code_entry, registration_number_entry, website_entry, description_entry, partner_window), 
        font=("Arial", 10), bg="green", fg="white")
    save_button.grid(row=4, columnspan=2, pady=10)

    partner_window.mainloop()

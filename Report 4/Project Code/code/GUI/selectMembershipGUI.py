import sys
sys.path.append('../functions/')
import tkinter as tk
from tkinter import messagebox
from continueRegist import continueRegistration
from mainPage import mainPage
from allClasses import  Beneficiary

# function to handle registration continuation
def continue_registration(window, user_id, selected_membership, duration, beneficiary_id):
    if selected_membership:
        # if a membership is selected, proceed with registration continuation
        success = continueRegistration(selected_membership, user_id, duration)
        if success:
            window.destroy()
            mainPage(beneficiary_id)
    else:
        # if no membership is selected, show an error message
        messagebox.showinfo("Error", "Please select a membership.")

# function to display subscription packages window
def packagesWindow(role, user_id):
    # create the packages window
    packages_window = tk.Tk()
    packages_window.title("Subscription Packages")

    # set window dimensions similar to a phone screen
    phone_width = 360
    phone_height = 640
    packages_window.geometry(f"{phone_width}x{phone_height}")
    packages_window.configure(bg="#1e272e")

    # Create a label to display role-specific message
    role_label = tk.Label(packages_window, text=f"Welcome {role}!", font=("Arial", 12), bg="#1e272e", fg="white")
    role_label.pack(pady=10)

    # Retrieve the beneficiary object
    beneficiary = Beneficiary.get_by_id(user_id)
    if not beneficiary:
        messagebox.showerror("Error", "Beneficiary not found.")
        packages_window.destroy()
        return
    beneficiary_id = beneficiary.beneficiary_id

    # membership options based on the user's role
    if role == "Service Provider":
        membership_options = [("Premium", {"Monthly": "14.99", "6-monthly": "10.00", "One year": "8.00"})]
    elif role == "Simple User":
        membership_options = [("Basic", {"Monthly": "12.99", "6-monthly": "8.00", "One year": "6.00"})]
    elif role == "Business Partner":
        membership_options = [("Professional", {"Monthly": "14.99", "6-monthly": "10.00", "One year": "8.00"})]

    memberships_frame = tk.Frame(packages_window, bg="#1e272e")
    memberships_frame.pack(pady=6)

    membership_colors = {"Monthly": "#fbc531", "6-monthly": "#e74c3c", "One year": "#3498db"}

    # create rectangles representing membership packages
    for membership, details in membership_options:
        for duration, price in details.items():
            # create a frame for each membership option
            membership_frame = tk.Frame(memberships_frame, bd=2, relief="solid", bg=membership_colors[duration])
            membership_frame.pack(padx=20, pady=20, ipadx=55, ipady=23, fill=tk.BOTH, expand=True)

            membership_name_label = tk.Label(membership_frame, text=membership, font=("Arial", 14, "bold"), bg=membership_colors[duration])
            membership_name_label.pack()

            price_label = tk.Label(membership_frame, text=f"{duration}: ${price}", font=("Arial", 14), bg=membership_colors[duration])
            price_label.pack()

    # dropdown menu to select membership duration
    duration_label = tk.Label(packages_window, text="Select Membership Duration:", font=("Arial", 12), bg="#1e272e", fg="white")
    duration_label.pack(pady=10)

    duration_options = list(membership_options[0][1].keys())
    selected_duration = tk.StringVar()
    selected_duration.set(duration_options[0])

    duration_dropdown = tk.OptionMenu(packages_window, selected_duration, *duration_options)
    duration_dropdown.config(bg="#4cd137", fg="white", font=("Arial", 12))
    duration_dropdown.pack()

    # function to handle registration continuation
    def on_continue_click():
        continue_registration(packages_window, user_id, membership_options[0][0], selected_duration.get(), beneficiary_id)

    # button to continue registration
    continue_button = tk.Button(packages_window, text="Continue", command=on_continue_click, bg="#4cd137", fg="white", font=("Arial", 14))
    continue_button.pack(side=tk.BOTTOM, padx=20, pady=20, ipadx=55, ipady=28)

    packages_window.mainloop()

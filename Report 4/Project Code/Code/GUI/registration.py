import sys
sys.path.append('database')
sys.path.append('functions')
sys.path.append('classes')
sys.path.append('GUI')
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from registAuthentication import registerUser
from db_connector import create_connection
from beneficiaryGUI import beneficiaryWindow
from partner import partnerWindow
from allClasses import User
from selectMembershipGUI import packagesWindow

def register(username_entry, name_entry, lastname_entry, email_entry, password_entry, repeat_password_entry, role_var, location_entry, registration_window):
    connection = create_connection()

    username = username_entry.get()
    name = name_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    repeat_password = repeat_password_entry.get()
    role = role_var.get()
    location = location_entry.get()
    
    if not all([username,name, lastname, email, password, repeat_password, role, location]):
        messagebox.showerror("Registration Error", "Please enter all fields.")
        return

    if password != repeat_password:
        messagebox.showerror("Registration Error", "Passwords do not match.")
        return

    if User.check_username_existence(username):
        messagebox.showerror("Registration Error", "Username already exists. Please choose a different one.")
        return

    if User.check_email_existence(email):
        messagebox.showerror("Registration Error", "Email already exists. Please use a different one.")
        return

# IN THE LOCATION ENTRY HERE WE CAN ADD A FUNCTION TO CHECK IF THE LOCATION EXISTS IN THE DATABASE AND IF THE FORMAT IS CORRECT

   # print(location)
    success, user_id = registerUser(username, name, lastname, email, password, role, location)
    print(success, user_id)
    print("eimai edw2")
    if success:
        messagebox.showinfo("Registration", "Registration Successful!")
        registration_window.destroy()
        if role == "Simple User" or role == "Service Provider" :
            beneficiaryWindow(role, user_id)
            packagesWindow(role, user_id) 
        else:
            partnerWindow(role,user_id)
            packagesWindow(role, user_id)

    else:
        messagebox.showerror("Registration Error", "Failed to register user.")
       

def registrationWindow():
    # create the registration window 
    registration_window = tk.Tk()
    registration_window.title("Registration Page")
    
    # set window dimensions similar to a phone screen
    phone_width = 360
    phone_height = 640
    registration_window.geometry(f"{phone_width}x{phone_height}")

    # load the background image
    # background_image = Image.open("../images/registration.jpg")
    # background_photo = ImageTk.PhotoImage(background_image)

    # create a canvas to display the background image
    canvas = tk.Canvas(registration_window, width=phone_width, height=phone_height)
    canvas.pack(fill="both", expand=True)
    # canvas.create_image(0, 0, anchor="nw", image=background_photo)

   
    # create labels 
    username_label = tk.Label(registration_window, text="Username:", font=("Arial", 9), bg="pink")
    name_label = tk.Label(registration_window, text="Name:", font=("Arial", 9), bg="pink")
    lastname_label = tk.Label(registration_window, text="Last Name:", font=("Arial", 9), bg="pink")
    email_label = tk.Label(registration_window, text="Email:", font=("Arial", 9), bg="pink")
    password_label = tk.Label(registration_window, text="Password:", font=("Arial", 9), bg="pink")
    repeat_password_label = tk.Label(registration_window, text="Repeat Password:", font=("Arial", 9), bg="pink")
   # phone_label = tk.Label(registration_window, text="Phone Number:", font=("Arial", 9), bg="pink")
    location_label = tk.Label(registration_window, text="Location:", font=("Arial", 9), bg="pink")

    # create entry fields 
    username_entry = tk.Entry(registration_window, font=("Arial", 9))
    name_entry = tk.Entry(registration_window, font=("Arial", 9),width=20)
    lastname_entry = tk.Entry(registration_window, font=("Arial", 9))
    password_entry = tk.Entry(registration_window, show="*", font=("Arial", 9))
    repeat_password_entry = tk.Entry(registration_window, show="*", font=("Arial", 9))
    email_entry = tk.Entry(registration_window, font=("Arial", 9))
  #  phone_entry = tk.Entry(registration_window, font=("Arial", 9))
    location_entry = tk.Entry(registration_window, font=("Arial", 9))

    role_label = tk.Label(registration_window, text="Select Role:", font=("Arial", 9), bg="pink")
    role_label.place(relx=0.05, rely=0.75)

    role_var = tk.StringVar(registration_window)
    role_var.set("Simple User") 
   
    role_dropdown = tk.OptionMenu(registration_window, role_var, "Business Partner", "Simple User", "Service Provider")
    role_dropdown.config(font=("Arial", 9), bg="pink")
    role_dropdown.place(relx=0.5, rely=0.75)

    # create buttons 
    register_button = tk.Button(registration_window, text="Start your 7-days FREE trial", font=("Arial", 11), bg="pink")
    continue_button = tk.Button(registration_window, text="Continue to choose Subscription Packages",command=lambda: register(username_entry, name_entry, lastname_entry, email_entry, password_entry, repeat_password_entry, role_var, location_entry, registration_window), font=("Arial",11), bg="pink")

    # layout widgets 
    username_label.place(relx=0.05, rely=0.1)
    name_label.place(relx=0.05, rely=0.2)
    lastname_label.place(relx=0.05, rely=0.3)
    password_label.place(relx=0.05, rely=0.4)
    repeat_password_label.place(relx=0.05, rely=0.5)
    email_label.place(relx=0.05, rely=0.6)
   # phone_label.place(relx=0.05, rely=0.5)
    location_label.place(relx=0.05, rely=0.7)

    username_entry.place(relx=0.5, rely=0.1)
    name_entry.place(relx=0.5, rely=0.2)
    lastname_entry.place(relx=0.5, rely=0.3)
    password_entry.place(relx=0.5, rely=0.4)
    repeat_password_entry.place(relx=0.5, rely=0.5)
    email_entry.place(relx=0.5, rely=0.6)
  #  phone_entry.place(relx=0.5, rely=0.5)
    location_entry.place(relx=0.5, rely=0.7)

   
    register_button.place(relx=0.2, rely=0.8)
    continue_button.place(relx=0.1, rely=0.9)

    registration_window.mainloop()
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from subprocess import Popen
import sys
sys.path.append('../functions/')
from loginAuthentication import authenticate
from registration import registrationWindow
from mainPage import mainPage
import config
from package import get_beneficiary_id

def login():
    print("Login button clicked")
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Login Error", "Please enter both username and password.")
        return

    if authenticate(username, password):
        messagebox.showinfo("Login", "Login Successful!")
        print("Logged in user:", config.current_user)  # print logged in user info
        root.destroy()
        mainPage()
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")
        return

#SEPARATION MUST BE DONE BETWEEN THE BUSINESS PARTNER AND BENEFICIARIES 

    success, user_id = authenticate(username, password)
    if success: # ONLY BENEFICIARIES FOR NOW 
        beneficiary_id = get_beneficiary_id(user_id) 
        messagebox.showinfo("Login", "Login Successful!")
        root.destroy()
        mainPage(beneficiary_id)
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")
        return
        

def registrationPage():
    '''
   print("Register button clicked")
   root.destroy()
   Popen('registration.py', shell=True)
   '''
    root.destroy()
    registrationWindow()
  

# create the main window
root = tk.Tk()
root.title("Login Page")

# set window dimensions similar to a phone screen
phone_width = 360
phone_height = 640
root.geometry(f"{phone_width}x{phone_height}")

background_image = Image.open("../images/loginpage.webp")
background_photo = ImageTk.PhotoImage(background_image)

# create a canvas to display the background image
canvas = tk.Canvas(root, width=phone_width, height=phone_height)
canvas.pack(fill="both", expand=True) 
canvas.create_image(0, 0, anchor="nw", image=background_photo)

# create labels
username_label = tk.Label(root, text="Username:",  bg="pink")
password_label = tk.Label(root, text="Password:",  bg="pink")

# create entry fields
username_entry = tk.Entry(root, font=("Arial", 12), width=20)  # increased font size and width
password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=20)  # increased font size and width

# create buttons
login_button = tk.Button(root, text="Login", command=login, font=("Arial", 12), width=7, height=2, bg="pink")  # increased font size and height
register_button = tk.Button(root, text="Register", command=registrationPage, font=("Arial", 12), width=7, height=2, bg="pink")  # increased font size and height

# place widgets even further below
username_label.place(relx=0.5, rely=0.7, anchor="center")
password_label.place(relx=0.5, rely=0.8, anchor="center")
username_entry.place(relx=0.5, rely=0.75, anchor="center")
password_entry.place(relx=0.5, rely=0.85, anchor="center")
login_button.place(relx=0.35, rely=0.95, anchor="center")
register_button.place(relx=0.65, rely=0.95, anchor="center")

root.mainloop()

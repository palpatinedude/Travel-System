import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from subprocess import Popen
from registration import registrationWindow
import sys
sys.path.append('../functions/')
from loginAuthentication import authenticate
import config  # import the config module
from mainPage import mainPage 

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

def registrationPage():
    root.destroy()
    registrationWindow()

root = tk.Tk()
root.title("Login Page")
phone_width = 360
phone_height = 640
root.geometry(f"{phone_width}x{phone_height}")

canvas = tk.Canvas(root, width=phone_width, height=phone_height)
canvas.pack(fill="both", expand=True)

username_label = tk.Label(root, text="Username:",  bg="pink")
password_label = tk.Label(root, text="Password:",  bg="pink")

username_entry = tk.Entry(root, font=("Arial", 12), width=20)
password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=20)

login_button = tk.Button(root, text="Login", command=login, font=("Arial", 12), width=7, height=2, bg="pink")
register_button = tk.Button(root, text="Register", command=registrationPage, font=("Arial", 12), width=7, height=2, bg="pink")

username_label.place(relx=0.5, rely=0.7, anchor="center")
password_label.place(relx=0.5, rely=0.8, anchor="center")
username_entry.place(relx=0.5, rely=0.75, anchor="center")
password_entry.place(relx=0.5, rely=0.85, anchor="center")
login_button.place(relx=0.35, rely=0.95, anchor="center")
register_button.place(relx=0.65, rely=0.95, anchor="center")

root.mainloop()

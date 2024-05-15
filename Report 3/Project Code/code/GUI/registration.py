import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def register():
    messagebox.showinfo("Registration", "Registration Successful!")

def create_registration_window():
    # create the registration window 
    registration_window = tk.Tk()
    registration_window.title("Registration Page")
    
    # set window dimensions similar to a phone screen
    phone_width = 360
    phone_height = 640
    registration_window.geometry(f"{phone_width}x{phone_height}")

    # load the background image
    background_image = Image.open("../images/registration.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # create a canvas to display the background image
    canvas = tk.Canvas(registration_window, width=phone_width, height=phone_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    # create labels 
    name_label = tk.Label(registration_window, text="Name:", font=("Arial", 9), bg="pink")
    lastname_label = tk.Label(registration_window, text="Last Name:", font=("Arial", 9), bg="pink")
    password_label = tk.Label(registration_window, text="Password:", font=("Arial", 9), bg="pink")
    repeat_password_label = tk.Label(registration_window, text="Repeat Password:", font=("Arial", 9), bg="pink")
    email_label = tk.Label(registration_window, text="Email:", font=("Arial", 9), bg="pink")
    phone_label = tk.Label(registration_window, text="Phone Number:", font=("Arial", 9), bg="pink")
    location_label = tk.Label(registration_window, text="Location:", font=("Arial", 9), bg="pink")

    # create entry fields 
    name_entry = tk.Entry(registration_window, font=("Arial", 9),width=20)
    lastname_entry = tk.Entry(registration_window, font=("Arial", 9))
    password_entry = tk.Entry(registration_window, show="*", font=("Arial", 9))
    repeat_password_entry = tk.Entry(registration_window, show="*", font=("Arial", 9))
    email_entry = tk.Entry(registration_window, font=("Arial", 9))
    phone_entry = tk.Entry(registration_window, font=("Arial", 9))
    location_entry = tk.Entry(registration_window, font=("Arial", 9))

    # create buttons 
    register_button = tk.Button(registration_window, text="Start your 7-days FREE trial", command=register, font=("Arial", 11), bg="pink")
    continue_button = tk.Button(registration_window, text="Continue to choose Subscription Packages", font=("Arial",11), bg="pink")

    # layout widgets 
    name_label.place(relx=0.05, rely=0.1)
    lastname_label.place(relx=0.05, rely=0.2)
    password_label.place(relx=0.05, rely=0.3)
    repeat_password_label.place(relx=0.05, rely=0.4)
    email_label.place(relx=0.05, rely=0.5)
    phone_label.place(relx=0.05, rely=0.6)
    location_label.place(relx=0.05, rely=0.7)

    name_entry.place(relx=0.5, rely=0.1)
    lastname_entry.place(relx=0.5, rely=0.2)
    password_entry.place(relx=0.5, rely=0.3)
    repeat_password_entry.place(relx=0.5, rely=0.4)
    email_entry.place(relx=0.5, rely=0.5)
    phone_entry.place(relx=0.5, rely=0.6)
    location_entry.place(relx=0.5, rely=0.7)

    register_button.place(relx=0.2, rely=0.8)
    continue_button.place(relx=0.1, rely=0.9)

    registration_window.mainloop()

if __name__ == "__main__":
    create_registration_window()

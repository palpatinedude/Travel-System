import sys
sys.path.append('classes')
import tkinter as tk
from beneficiary import Beneficiary
from editProfileGUI import changeMyInfo
import config

def viewEditProfile(window, beneficiary_id):
    print("edit profile button")
    window.destroy()
    print(beneficiary_id)
    user_type = Beneficiary.getRoleID(beneficiary_id)
    print(user_type)
    if user_type:
        changeMyInfo(beneficiary_id, user_type)
    else:
        print("Unable to determine user role")

def viewFriends():
    print("view friends button")

def friendRequests():
    print("view friend requests button")

def showProfile(beneficiary_id):
    profile_window = tk.Tk()
    profile_window.title("Profile Page")

    # set window dimensions
    window_width = 360
    window_height = 640
    profile_window.geometry(f"{window_width}x{window_height}")
    profile_window.configure(bg="#7171C6")

    # profile page title
    profile_label = tk.Label(profile_window, text="My Profile", font=("Arial", 20), bg="#836FFF", fg="black")
    profile_label.pack(pady=20)

    # img = tk.PhotoImage(file='GUI/profile.png')
    # img = img.subsample(2)
    # img_label = tk.Label(profile_window, image=img, bg="#33A1C9")
    # img_label.image = img
    # img_label.place(x=50, y=90)

    #  frame for the buttons
    button_frame = tk.Frame(profile_window, bg="#7171C6")
    button_frame.place(x=220, y=90)

    # buttons
    edit_button = tk.Button(button_frame, text="Edit", command=lambda: viewEditProfile(profile_window, beneficiary_id), font=("Arial", 10), bg="#9FB6CD", fg="black", width=13, height=2)
    edit_button.pack(pady=5)
    friends_button = tk.Button(button_frame, text="Friends", command=viewFriends, font=("Arial", 10), bg="#9FB6CD", fg="black", width=13, height=2)
    friends_button.pack(pady=5)
    friend_requests_button = tk.Button(button_frame, text="Friend Requests", command=friendRequests, font=("Arial", 10), bg="#9FB6CD", fg="black", width=13, height=2)
    friend_requests_button.pack(pady=5)

    button_frame2 = tk.Frame(profile_window, bg="#7171C6")
    button_frame2.place(x=57, y=280)

    saved_button = tk.Button(button_frame2, text="Saved", font=("Arial", 10), bg="#9FB6CD", fg="black", width=30, height=2)
    saved_button.pack(pady=10)
    bookings_button = tk.Button(button_frame2, text="Bookings", font=("Arial", 10), bg="#9FB6CD", fg="black", width=30, height=2)
    bookings_button.pack(pady=10)
    notifications_button = tk.Button(button_frame2, text="Notifications", font=("Arial", 10), bg="#9FB6CD", fg="black", width=30, height=2)
    notifications_button.pack(pady=10)
    membership_button = tk.Button(button_frame2, text="Membership", font=("Arial", 10), bg="#9FB6CD", fg="black", width=30, height=2)
    membership_button.pack(pady=10)

    profile_window.mainloop()
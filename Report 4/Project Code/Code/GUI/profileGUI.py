import sys
sys.path.append('Report 4/Project Code/Code/functions')
sys.path.append('Report 4/Project Code/Code/classes')
import tkinter as tk
import config
from allClasses import Beneficiary, Membership
from editProfileGUI import changeMyInfo
from db_connector import create_connection
from makefriendsGUI import viewFriendRequests, friendRequests
from models import FriendRequestApp, FriendsApp

from allClasses import Beneficiary, Membership
from editProfileGUI import changeMyInfo

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
    root = tk.Tk()
    app = FriendsApp(root)
    root.mainloop()

def friendRequests():
    print("view friend requests button")
    root = tk.Tk()
    app = FriendRequestApp(root)
    root.mainloop()

def handleMembershipCancellation(beneficiary_id):
    #for membership cancellation confirmation
    membership_window = tk.Toplevel()
    membership_window.title("Cancel Membership")
    

    confirmation_msg = "Are you sure you want to cancel your membership?"
    
    #  confirmation message
    confirmation_label = tk.Label(membership_window, text=confirmation_msg, font=("Arial", 12))
    confirmation_label.pack(pady=10)
    
    #  buttons
    def confirmMembershipCancellation():
        confirm = messagebox.askyesno("Confirm", confirmation_msg)
        if confirm:
            cancelMembership(beneficiary_id)
            membership_window.destroy()

    
    confirm_button = tk.Button(membership_window, text="Yes", command=confirmMembershipCancellation)
    confirm_button.pack(pady=5)
    cancel_button = tk.Button(membership_window, text="No", command=membership_window.destroy)
    cancel_button.pack(pady=5)

def cancelMembership(beneficiary_id):
    membership = Membership()
    membership.delete(beneficiary_id)
    messagebox.showinfo("Success", "Your membership has been canceled")

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

    # img = tk.PhotoImage(file='Report 4/Project Code/Code/GUI/profile.png')
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
    membership_button = tk.Button(button_frame2, text="Membership", command=lambda: handleMembershipCancellation(beneficiary_id), font=("Arial", 10), bg="#9FB6CD", fg="black", width=30, height=2)
    membership_button.pack(pady=10)

    profile_window.mainloop()
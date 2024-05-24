# import sys,os
# import mysql.connector 
# import tkinter as tk
# from models import ReviewApp, Response, User, ChatMessage, FriendRequest, Beneficiary, FriendRequestGUI
# import config

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FriendRequestGUI(root)
#     root.mainloop()

# main.py
# main.py
import tkinter as tk
from loginpage import root as login_root
import config
from models import FriendRequestGUI

def main():
    login_root.mainloop()  # Run the login window

    if config.current_user:
        root = tk.Tk()
        app = FriendRequestGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()


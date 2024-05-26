import sys
import os
import mysql.connector
import tkinter as tk
from tkinter import messagebox
import config
from loginpage import root as login_root
from models import Response, User, ReviewApp, ChattingGUI, SocialBondingGUI

# ########################################################################################################

def main():
    login_root.mainloop()  # Run the login window
    user_id = config.current_user

    if config.current_user:
        root = tk.Tk()
        app = ReviewApp(root, user_id)
        root.mainloop()

if __name__ == "__main__":
    main()
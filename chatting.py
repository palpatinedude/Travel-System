import sys,os
import mysql.connector
from models import ReviewApp, ChattingGUI, SocialBondingGUI
import config
from loginpage import root as login_root
import tkinter as tk

def main():
    login_root.mainloop()  # Run the login window

    if config.current_user:
        root = tk.Tk()
        app = SocialBondingGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()
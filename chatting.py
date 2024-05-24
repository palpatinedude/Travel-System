import sys,os
import mysql.connector
from models import Response, User, ChatMessage, ReviewApp, ChattingGUI
import config
from loginpage import root as login_root
import tkinter as tk

def main():
    login_root.mainloop()  # Run the login window

    if config.current_user:
        root = tk.Tk()
        app = ChattingGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()

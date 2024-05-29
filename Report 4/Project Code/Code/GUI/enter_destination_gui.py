import sys,os
import mysql.connector
from models import DestinationGui
import tkinter as tk
from tkinter import messagebox
import config
from loginpage import root as login_root

def main():
    login_root.mainloop()  # Run the login window

    if config.current_user:
     root = tk.Tk()
     app = DestinationGui(root)
     root.mainloop()

if __name__ == "__main__":
    main()
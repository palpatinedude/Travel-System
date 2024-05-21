import sys,os
import mysql.connector
from models import ReviewApp, User, ChatMessage, FriendRequest, Beneficiary, DestinationGui
import tkinter as tk
from tkinter import messagebox


if __name__ == "__main__":
    root = tk.Tk()
    app = DestinationGui(root)
    root.mainloop()
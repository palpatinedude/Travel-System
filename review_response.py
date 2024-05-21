import sys
import os
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from models import Review, Response, User, ReviewApp

# # #connect to MySQL
# # mydb = mysql.connector.connect(
# # host="localhost",
# # user="root",
# # passwd="4655",
# # database="od"
# # )

# # #check if connection is established         #testing 
# # if (mydb):
# #     print("Connection Successful")
# # else:
# #     print("Connection Unsuccessful")

# # #creating a cursor object using the cursor() method
# # mycursor = mydb.cursor() #cursor object which is used to interact with the database

# ########################################################################################################

if __name__ == "__main__":
    root = tk.Tk()
    app = ReviewApp(root)
    root.mainloop()

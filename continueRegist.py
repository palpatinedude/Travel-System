import sys
sys.path.append('../database/')
import tkinter as tk
from tkinter import messagebox
from db_connector import create_connection
import datetime

def continueRegistration(selected_membership, user_id,duration):
    # handle the selected membership and continue the registration process
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                # insert membership
                cursor.execute("INSERT INTO Membership (membership_type, duration, membership_status, created_date) VALUES (%s, %s, %s, %s)", (selected_membership, "Monthly", "Active", datetime.date.today()))
                membership_id = cursor.lastrowid
                # assign membership to user
                cursor.execute("UPDATE User SET membership_id = %s WHERE user_id = %s", (membership_id, user_id))
                connection.commit()
                messagebox.showinfo("Membership Assigned", f"{selected_membership} membership has been assigned to the user.")
                return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to assign membership: {e}")
            return False
        finally:
            connection.close()
    else:
        messagebox.showerror("Database Error", "Failed to connect to the database.")
        return False

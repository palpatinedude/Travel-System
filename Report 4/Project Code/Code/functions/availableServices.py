import sys
import tkinter as tk
from db_connector import create_connection
from datetime import datetime

def areAvailableServices(service_id):
    try:
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM ServiceAvailability WHERE service_id = %s", (service_id,))
            count = cursor.fetchone()[0]
            cursor.close()
            return count > 0
    except Exception as e:
        print(f"Error checking service availability: {e}")
        return False

def getAvailableDates(service_id):
    try:
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT available_date FROM ServiceAvailability WHERE service_id = %s", (service_id,))
            available_dates = [date[0] for date in cursor.fetchall()]
            cursor.close()
            return available_dates
    except Exception as e:
        print(f"Error retrieving available dates: {e}")
        return []

def getAvailableHours(service_id, date):
    try:
        with create_connection() as conn:
            print(service_id, date)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT time_range 
                FROM AvailableHours 
                WHERE service_id = %s AND available_date = %s
            """, (service_id, date))
            available_hours = cursor.fetchall()
            cursor.close()
            print(available_hours)
            return available_hours
    except Exception as e:
        print(f"Error retrieving available hours: {e}")
        return []

def getServiceIdByStartDate(start_date):
     try:
         with create_connection() as conn:
             cursor = conn.cursor()
             cursor.execute("SELECT service_id FROM ServiceAvailability WHERE available_date = %s", (start_date,))
             rows = cursor.fetchall()
             if rows:
                 service_id = rows[0][0]
                 cursor.close()
                 return service_id
             else:
                 cursor.close()
                 return None

     except Exception as e:
         print(f"Error retrieving service_id by start_date: {e}")
         return None

def updateService(service_id, start_date, end_date=None, time_range=None):
    try:
        if start_date and start_date != '':
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
        else:
            start_date = None
        
        if end_date and end_date != '':
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        else:
            end_date = None
        
        print(start_date, end_date, time_range)
        
        with create_connection() as conn:
            cursor = conn.cursor()
            
            if start_date and end_date:
                cursor.execute("DELETE FROM ServiceAvailability WHERE service_id = %s AND available_date BETWEEN %s AND %s",
                               (service_id, start_date, end_date))
            elif start_date:
                cursor.execute("DELETE FROM ServiceAvailability WHERE service_id = %s AND available_date = %s",
                               (service_id, start_date))
            
            if time_range:
                cursor.execute("DELETE FROM AvailableHours WHERE service_id = %s AND available_date BETWEEN %s AND %s AND time_range = %s",
                               (service_id, start_date, end_date, time_range))
            else:
                cursor.execute("DELETE FROM AvailableHours WHERE service_id = %s AND available_date BETWEEN %s AND %s",
                               (service_id, start_date, end_date))
            
            conn.commit()
            cursor.close()
            print("Service availability updated successfully.")
            
    except Exception as e:
        print(f"Error updating service availability: {e}")

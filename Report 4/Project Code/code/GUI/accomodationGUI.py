import tkinter as tk
from allClasses import Accommodation

def makeReservation():
    print("Reservation made!")

def displayAccomodation(accommodation):
    accommodation_window = tk.Tk()
    accommodation_window.configure(bg="#CD3278")
    accommodation_window.title("Accommodation Details")
    

    window_width = 360
    window_height = 640
    accommodation_window.geometry(f"{window_width}x{window_height}")
    

    details_label = tk.Label(accommodation_window, text=f"Service ID: {accommodation.service_name}\n"
                                                        f"Number of Rooms: {accommodation.num_rooms}\n"
                                                        f"Facilities: {accommodation.facilities}")
    details_label.pack(pady=20)
    

    reservation_button = tk.Button(accommodation_window, text="Make Reservation", command=makeReservation)
    reservation_button.pack(pady=20)
    

    accommodation_window.mainloop()
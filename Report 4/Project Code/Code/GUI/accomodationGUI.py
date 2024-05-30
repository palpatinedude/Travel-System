import sys
sys.path.append('Report 4/Project Code/Code/functions')
sys.path.append('Report 4/Project Code/Code/classes')
import tkinter as tk
from allClasses import Accommodation, Booking
from availableServices import areAvailableServices, getAvailableDates, getAvailableHours, getServiceIdByStartDate, updateService
from PIL import Image, ImageTk


# global variables
start_date_var = None
end_date_var = None
hour_var = None

def makeReservation(service_id, beneficiary_id):
    if not areAvailableServices(service_id):
        messagebox.showinfo("No Available Services", "No available dates for this service!")
        return

    available_dates = getAvailableDates(service_id)
    displayDatePage(available_dates,beneficiary_id)

def displayDatePage(available_dates,beneficiary_id):
    dates_window = tk.Toplevel()
    dates_window.title("Available Dates")
    
    date_frame = tk.Frame(dates_window)
    date_frame.pack()

    # labels for each date in the available_dates list
    for i, date in enumerate(available_dates):
        date_label = tk.Label(date_frame, text=date)
        date_label.grid(row=i//7, column=i%7, padx=5, pady=5)

    # selecting start and end dates
    global start_date_var, end_date_var
    start_date_var = tk.StringVar()
    end_date_var = tk.StringVar()
    start_date_label = tk.Label(dates_window, text="Start Date:")
    start_date_label.pack()
    start_date_entry = tk.Entry(dates_window, textvariable=start_date_var)
    start_date_entry.pack()
    end_date_label = tk.Label(dates_window, text="End Date:")
    end_date_label.pack()
    end_date_entry = tk.Entry(dates_window, textvariable=end_date_var)
    end_date_entry.pack()

    # confirm selection
    confirm_button = tk.Button(dates_window, text="Confirm", command=lambda: selectDate(dates_window,beneficiary_id))
    confirm_button.pack()

def selectDate(window,beneficiary_id):
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    window.destroy()
    displayHourPage(start_date,beneficiary_id)

def displayHourPage(date,beneficiary_id):
    global hour_var
    hour_var = tk.StringVar()
    
    hours_window = tk.Toplevel()
    hours_window.title("Available Hours")

    service_id = getServiceIdByStartDate(date)
    available_hours = getAvailableHours(service_id,date)
    
    hours_frame = tk.Frame(hours_window)
    hours_frame.pack()

    for i, hour in enumerate(available_hours):
        hour_label = tk.Radiobutton(hours_frame, text=hour, variable=hour_var, value=hour)
        hour_label.grid(row=i//4, column=i%4, padx=5, pady=5)

    confirm_button = tk.Button(hours_window, text="Confirm", command=lambda: displayHour(hours_window,service_id,beneficiary_id))
    confirm_button.pack()

def displayHour(window,service_id,beneficiary_id):
    selected_hour = hour_var.get()
    window.destroy()
    displayConfirmWindow(selected_hour,service_id,beneficiary_id)

def displayConfirmWindow(hour,service_id,beneficiary_id):
    confirm_window = tk.Toplevel()
    confirm_window.title("Confirm Reservation")

    details_text = f"Start Date: {start_date_var.get()}\nEnd Date: {end_date_var.get()}\nHour: {hour}"
    details_label = tk.Label(confirm_window, text=details_text)
    details_label.pack(pady=20)

    confirm_button = tk.Button(confirm_window, text="Confirm", command=lambda: confirmChoice(confirm_window,beneficiary_id,service_id))
    confirm_button.pack(side=tk.LEFT, padx=10)

    cancel_button = tk.Button(confirm_window, text="Cancel", command=lambda: cancelProcedure(confirm_window))
    cancel_button.pack(side=tk.RIGHT, padx=10)

def confirmChoice(window, beneficiary_id, service_id):
    window.destroy()
    booking = Booking(booking_date=start_date_var.get(), booking_status="pending", booker_id=beneficiary_id, service_id=service_id)
    booking.save()
    print("Booking done")
    displayConfirmMsg(window)
    updateService(service_id, start_date_var.get(), end_date_var.get(),hour_var.get())
   

   
def displayConfirmMsg(window):
    messagebox.showinfo("Reservation Confirmed", "Thank you for your reservation, your application is in pending. We will send you a confirmation email.")
    displayServicePage(window)

def displayServicePage(window):
    window.destroy()
   

def cancelProcedure(window):
    window.destroy()

def displayAccommodation(accommodation,beneficiary_id):
    accommodation_window = tk.Tk()
    accommodation_window.configure(bg="#CD3278")
    accommodation_window.title("Accommodation Details")

    # set window dimensions
    window_width = 360
    window_height = 640
    accommodation_window.geometry(f"{window_width}x{window_height}")

    canvas = tk.Canvas(accommodation_window, width=window_width, height=window_height//2)
    canvas.pack()

    background_image = Image.open("../images/accomodation.jpg")
    background_image = background_image.resize((window_width, window_height//2))
    background_photo = ImageTk.PhotoImage(background_image)


    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    # drame for the lower half of the window
    lower_frame = tk.Frame(accommodation_window, bg="#CD3278")
    lower_frame.pack(fill=tk.BOTH, expand=True)

    title_label = tk.Label(lower_frame, text="Accommodation Details", font=("Arial", 16, "bold"), bg="#CD3278", fg="white")
    title_label.pack(pady=20)

    # details of the specific accommodation
    details_text = (f"Service Name: {accommodation.service_name}\n"
                    f"Number of Rooms: {accommodation.num_rooms}\n"
                    f"Facilities: {accommodation.facilities}")
    details_label = tk.Label(lower_frame, text=details_text, font=("Arial", 12), bg="#7A8B8B", fg="white", justify=tk.LEFT)
    details_label.pack(pady=20, padx=70, anchor="w")

    service_id = accommodation.service_id
    reservation_button = tk.Button(lower_frame, text="Make Reservation", command=lambda: makeReservation(service_id,beneficiary_id), font=("Arial", 12, "bold"), bg="#7A8B8B", fg="white", padx=10, pady=10)
    reservation_button.pack(pady=20)

    accommodation_window.mainloop()
import sys
sys.path.append('classes')
sys.path.append('GUI')
import tkinter as tk
from allClasses import Market, Bars, Hotels, FoodAndBeverage, Accommodation, Car, Activity
from accomodationGUI import displayAccomodation

def open_accommodation_window(window,accommodation):
    print("Accommodation window opened")
    window.destroy()
    displayAccomodation(accommodation)
    
def open_car_window(window,car):
    print("Car window opened")
    window.destroy()
    
def open_activity_window(window,activity):
    print("Activity window opened")
    window.destroy()

def showServices(filter_parameters=None, budget_amount=None):
    services_window = tk.Tk()
    services_window.title("Display Services")
    
    window_width = 360
    window_height = 640
    services_window.geometry(f"{window_width}x{window_height}")
    services_window.configure(bg="pink")
    
    #  labels and frames for each business type
    market_label = tk.Label(services_window, text="Market", bg="pink", font=("Arial", 14))
    market_frame = tk.Frame(services_window, bg="lightblue")
    bar_label = tk.Label(services_window, text="Bars", bg="pink", font=("Arial", 14))
    bar_frame = tk.Frame(services_window, bg="lightgreen")
    hotel_label = tk.Label(services_window, text="Hotels", bg="pink", font=("Arial", 14))
    hotel_frame = tk.Frame(services_window, bg="lightyellow")
    food_beverage_label = tk.Label(services_window, text="Food and Beverage", bg="pink", font=("Arial", 14))
    food_beverage_frame = tk.Frame(services_window, bg="lightcoral")

    accommodation_label = tk.Label(services_window, text="Accommodation", bg="pink", font=("Arial", 14))
    accommodation_frame = tk.Frame(services_window, bg="#FFD39B")
    car_label = tk.Label(services_window, text="Car", bg="pink", font=("Arial", 14))
    car_frame = tk.Frame(services_window, bg="#98F5FF")
    activity_label = tk.Label(services_window, text="Activity", bg="pink", font=("Arial", 14))
    activity_frame = tk.Frame(services_window, bg="#FF9912")
    

    frame_padding = (10, 5)
    
    market_label.pack(anchor="w", padx=10, pady=(20, 5))
    market_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 20))
    bar_label.pack(anchor="w", padx=10, pady=frame_padding)
    bar_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 20))
    hotel_label.pack(anchor="w", padx=10, pady=frame_padding)
    hotel_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 20))
    food_beverage_label.pack(anchor="w", padx=10, pady=frame_padding)
    food_beverage_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 20))

    accommodation_label.pack(anchor="w", padx=10, pady=frame_padding)
    accommodation_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 20))
    car_label.pack(anchor="w", padx=10, pady=frame_padding)
    car_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 20))
    activity_label.pack(anchor="w", padx=10, pady=frame_padding)
    activity_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 20))
    
    #  all businesses/services of each type
    markets = Market.get_all()
    bars = Bars.get_all()
    hotels = Hotels.get_all()
    food_beverages = FoodAndBeverage.get_all()
    accommodations = Accommodation.get_all()
    cars = Car.get_all()
    activities = Activity.get_all()
    
    # y businesses in their respective frames
    for market in markets:
        market_label = tk.Label(market_frame, text=market.business_name, bg="lightblue")
        market_label.pack(anchor="w", padx=5)
    
    for bar in bars:
        bar_label = tk.Label(bar_frame, text=bar.business_name, bg="lightgreen")
        bar_label.pack(anchor="w", padx=5)
    
    for hotel in hotels:
        hotel_label = tk.Label(hotel_frame, text=hotel.business_name, bg="lightyellow")
        hotel_label.pack(anchor="w", padx=5)
    
    for food_beverage in food_beverages:
        food_beverage_label = tk.Label(food_beverage_frame, text=food_beverage.business_name, bg="lightcoral")
        food_beverage_label.pack(anchor="w", padx=5)

    # services for each type
    for accommodation in accommodations:
        accommodation_button = tk.Button(accommodation_frame, text=accommodation.service_name, bg="#FFD39B", command=lambda: open_accommodation_window(services_window,accommodation))
        accommodation_button.pack(anchor="w", padx=5, pady=5)

    for car in cars:
        car_button = tk.Button(car_frame, text=car.service_name, bg="#98F5FF", command=lambda: open_car_window(services_window,car))
        car_button.pack(anchor="w", padx=5, pady=5)

    for activity in activities:
        activity_button = tk.Button(activity_frame, text=activity.service_name, bg="#FF9912",  command=lambda: open_activity_window(services_window,activity))
        activity_button.pack(anchor="w", padx=5, pady=5)    
    
    services_window.mainloop()

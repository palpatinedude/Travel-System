import sys
sys.path.append('Report 4/Project Code/Code/functions')
sys.path.append('Report 4/Project Code/Code/classes')
sys.path.append('Report 4/Project Code/CodeGUI')
import tkinter as tk
import config
from models import SocialBondingGUI, ReviewApp
from profileGUI import showProfile
from cardGUI import displayCard
from pointsGUI import displayPoints
from functools import partial
from filtersGUI import chooseFilters

def exploreDestinationAction(window,beneficiary_id):
    print("Explore Destination action")
    window.destroy()
    chooseFilters(beneficiary_id)

def socialBondingAction(window):
    print("Social Bonding action")
    if config.current_user:
     root = tk.Tk()
     app = SocialBondingGUI(root)
     root.mainloop()

def entertainmentAction(window):
    print("Entertainment action")

def mapAction(window):
    print("Map action")

def profileAction(window, beneficiary_id):
    print("Profile action")
    if config.current_user:
        # window.destroy() 
        showProfile(beneficiary_id)

def destinationAction(window):
    print("Destination action")

def cardAction(window):
    print("Card action")
    window.destroy() 
    displayCard()

def pointsAction(window,beneficiary_id):
    print("Point action") 
    window.destroy() 
    displayPoints(beneficiary_id) 

def mainPage(beneficiary_id):
    main_window = tk.Tk()
    main_window.title("Main Page")

    # set window dimensions
    window_width = 360
    window_height = 640
    main_window.geometry(f"{window_width}x{window_height}")
    main_window.configure(bg="#FA8072")

    # create a top frame for the first three buttons
    top_frame = tk.Frame(main_window, height=50)
    top_frame.pack(fill="x", pady=10)  

    map_button = tk.Button(top_frame, text="Map", command=lambda: mapAction(main_window), width=10, height=2, bg="#848484", fg="white")
    map_button.grid(row=0, column=0, padx=10, pady=10)

    destination_button = tk.Button(top_frame, text="Destination", command=lambda: destinationAction(main_window), width=10, height=2, bg="#848484", fg="white")
    destination_button.grid(row=0, column=1, padx=10, pady=10)

    profile_button = tk.Button(top_frame, text="Profile", command=lambda: profileAction(main_window,beneficiary_id), width=10, height=2, bg="#848484", fg="white")
    profile_button.grid(row=0, column=2, padx=50, pady=10)


    # create a frame to hold the other buttons
    button_frame = tk.Frame(main_window)
    button_frame.pack(pady=50)

    explore_button = tk.Button(button_frame, text="Explore Destination", command=lambda: exploreDestinationAction(main_window,beneficiary_id), width=20, height=3, bg="#71C671", fg="white")
    explore_button.grid(row=0, column=0, padx=10, pady=40)

    social_button = tk.Button(button_frame, text="Social Bonding", command=lambda: socialBondingAction(main_window), width=20, height=3, bg="#71C671", fg="white")
    social_button.grid(row=0, column=1, padx=10, pady=40)

    entertainment_button = tk.Button(button_frame, text="Entertainment", command=lambda: entertainmentAction(main_window), width=30, height=5, bg="#71C671", fg="white")
    entertainment_button.grid(row=1, column=0, columnspan=2, pady=15)

    # create a new frame for the card and points buttons
    bottom_frame = tk.Frame(main_window)
    bottom_frame.pack(fill="x", pady=75)

    card_button = tk.Button(bottom_frame, text="Card", command=lambda: cardAction(main_window), width=15, height=2, bg="#848484", fg="white")
    card_button.grid(row=0, column=0, padx=10, pady=10)

    point_button = tk.Button(bottom_frame, text="Points", command=lambda: pointsAction(main_window,beneficiary_id), width=15, height=2, bg="#848484", fg="white")
    point_button.grid(row=0, column=1, padx=70, pady=10)

    main_window.mainloop()
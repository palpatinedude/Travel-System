import tkinter as tk
import config
from models import SocialBondingGUI, ReviewApp

def exploreDestinationAction():
    print("Explore Destination action")
    if config.current_user:
        root = tk.Tk()
        app = ReviewApp(root)
        root.mainloop()

def socialBondingAction():
    print("Social Bonding action")
    if config.current_user:
        root = tk.Tk()
        app = SocialBondingGUI(root)
        root.mainloop()

def entertainmentAction():
    print("Entertainment action")

def mapAction():
    print("Map action")

def profileAction():
    print("Profile action")

def destinationAction():
    print("Destination action")

def cardAction():
    print("Card action")

def pointAction():
    print("Point action")    

def mainPage():
    main_window = tk.Tk()
    main_window.title("Main Page")

    # set window dimensions
    window_width = 360
    window_height = 640
    main_window.geometry(f"{window_width}x{window_height}")
    main_window.configure(bg="yellow")

    # create a top frame for the first three buttons
    top_frame = tk.Frame(main_window, height=50)
    top_frame.pack(fill="x", pady=10)  

    map_button = tk.Button(top_frame, text="Map", command=mapAction, width=10, height=2, bg="pink", fg="white")
    map_button.grid(row=0, column=0, padx=10, pady=10)

    destination_button = tk.Button(top_frame, text="Destination", command=destinationAction, width=10, height=2, bg="pink", fg="white")
    destination_button.grid(row=0, column=1, padx=10, pady=10)

    profile_button = tk.Button(top_frame, text="Profile", command=profileAction, width=10, height=2, bg="pink", fg="white")
    profile_button.grid(row=0, column=2, padx=50, pady=10)


    # create a frame to hold the other buttons
    button_frame = tk.Frame(main_window)
    button_frame.pack(pady=50)

    explore_button = tk.Button(button_frame, text="Explore Destination", command=exploreDestinationAction, width=20, height=3, bg="blue", fg="white")
    explore_button.grid(row=0, column=0, padx=10, pady=40)

    social_button = tk.Button(button_frame, text="Social Bonding", command=socialBondingAction, width=20, height=3, bg="red", fg="white")
    social_button.grid(row=0, column=1, padx=10, pady=40)

    entertainment_button = tk.Button(button_frame, text="Entertainment", command=entertainmentAction, width=30, height=5, bg="green", fg="white")
    entertainment_button.grid(row=1, column=0, columnspan=2, pady=15)

    # create a new frame for the card and points buttons
    bottom_frame = tk.Frame(main_window)
    bottom_frame.pack(fill="x", pady=75)

    card_button = tk.Button(bottom_frame, text="Card", command=cardAction, width=15, height=2, bg="pink", fg="white")
    card_button.grid(row=0, column=0, padx=10, pady=10)

    point_button = tk.Button(bottom_frame, text="Points", command=pointAction, width=15, height=2, bg="pink", fg="white")
    point_button.grid(row=0, column=1, padx=70, pady=10)

    main_window.mainloop()

    
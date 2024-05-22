import tkinter as tk

def exploreDestinationAction():
    print("Explore Destination action")

def socialBondingAction():
    print("Social Bonding action")

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

    
class DestinationGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Destination Finder")
        self.root.geometry("360x640")  # Set window size to simulate a phone screen

        self.destination_frame = tk.Frame(root, bg='#118599')
        self.destination_frame.pack(fill=tk.BOTH, expand=True)

        # Add empty rows at the top to lower the content
        for i in range(5):
            self.destination_frame.grid_rowconfigure(i, minsize=10)

        tk.Label(self.destination_frame, text="What are you exploring today?", bg='#118599', fg='white', font=('Arial', 22, 'bold'), wraplength=360, anchor='w', justify='left').grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="ew")
        tk.Label(self.destination_frame, text="Please insert country and city", bg='#118599', fg='white', font=('Arial', 16), wraplength=360, anchor='w', justify='left').grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="ew")

        # Add empty rows at the top to lower the content
        for i in range(5):
            self.destination_frame.grid_rowconfigure(i, minsize=20)

        # Input fields for country and city
        tk.Label(self.destination_frame, text="Enter Country:", bg='#118599', fg='white', font=('Arial', 14, 'bold')).grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.country_entry = tk.Entry(self.destination_frame, width=30)
        self.country_entry.grid(row=6, column=0, columnspan=6, padx=10, pady=5, sticky='ew')

        tk.Label(self.destination_frame, text="Enter City:", bg='#118599', fg='white', font=('Arial', 14, 'bold')).grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.city_entry = tk.Entry(self.destination_frame, width=30)
        self.city_entry.grid(row=8, column=0, columnspan=6, padx=10, pady=5, sticky='ew')

        self.submit_button = tk.Button(self.destination_frame, text="Find Destination", command=self.find_destination, bg="green", fg="white")
        self.submit_button.grid(row=10, column=0, columnspan=3, padx=5, pady=10, sticky='e')

    def find_destination(self):
        country = self.country_entry.get()
        city = self.city_entry.get()

        if not country or not city:
            messagebox.showerror("Error", "Both country and city are required")
            return

        connection = create_connection()
        cursor = connection.cursor()

        try:
            # Find the country ID based on the country name
            cursor.execute("SELECT country_id FROM Country WHERE country_name=%s", (country,))
            country_result = cursor.fetchone()

            if not country_result:
                messagebox.showerror("Error", "Country not found")
                return

            country_id = country_result[0]

            # Find the city based on the country ID and city name
            cursor.execute("SELECT city_name, latitude, longitude FROM City WHERE city_name=%s AND country_id=%s", (city, country_id))
            city_result = cursor.fetchone()

            if city_result:
                city_name, latitude, longitude = city_result
                messagebox.showinfo("Destination Found", f"City: {city_name}\nLatitude: {latitude}\nLongitude: {longitude}")
                self.root.destroy()   #close current window 
                mainPage()
            else:
                messagebox.showerror("Error", "City not found in the specified country")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            cursor.close()
            connection.close()

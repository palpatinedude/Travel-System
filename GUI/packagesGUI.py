import tkinter as tk

def showPackages(filter_parameters=None, budget_amount=None):
    # Create a new window
    packages_window = tk.Tk()
    packages_window.title("Display Packages")
    
    window_width = 360
    window_height = 640
    packages_window.geometry(f"{window_width}x{window_height}")
    packages_window.configure(bg="pink")

    packages_window.mainloop()


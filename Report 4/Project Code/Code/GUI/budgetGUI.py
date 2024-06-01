# IF SELECT AND FILTERS AND BUDGET PLANNER THEN SHOW INTERGRATED PACKAGES OTHERWISE SHOW THE APPROPRIATE SERVICES
# IMPLEMENT ONLY TO DISPLAY THE SERVICES IN ORDER TO MAKE A RESERVATION

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from packagesGUI import showPackages
from exploreDestinationGUI import showServices

def chooseBudget():
    budget_amount = budget_entry.get()
    if check(budget_amount):
        return float(budget_amount)
    else:
        chooseBudgetMess(budget_window)

def check(budget_amount):
    try:
        budget_amount = float(budget_amount)
        if budget_amount == 0:
            messagebox.showinfo("Message", "Please fill in a non-zero budget.")
            return False
        elif budget_amount > 0:
            return True
        else:
            return False
    except ValueError:
        messagebox.showinfo("Message", "Please fill in a valid budget.")
        return False

def notFilled():
    print("Please fill in your budget.")

def chooseBudgetMess(window):
    messagebox.showinfo("Message", "Please fill in your budget.")
    window.destroy()

def continue_with_budget(window, filter_parameters, beneficiary_id):
    budget_amount = chooseBudget()
    if filter_parameters or budget_amount:
        window.destroy()
        showServices(filter_parameters, budget_amount, beneficiary_id)
    elif filter_parameters:
        window.destroy()
        showPackages(filter_parameters, budget_amount)

def continue_without_budget(window, filter_parameters, beneficiary_id):
    print("Continue without budget planner")
    window.destroy()
    showServices(filter_parameters, None, beneficiary_id)

def showBudget(filter_parameters, beneficiary_id):
    global budget_window
    budget_window = tk.Tk()
    budget_window.title("Budget Planner")
    budget_window.configure(bg="#FA8072")

    # set window dimensions
    window_width = 360
    window_height = 640
    budget_window.geometry(f"{window_width}x{window_height}")

    # load and set the background image
    background_image = Image.open("../images/budget.jpg")
    background_image = background_image.resize((window_width, window_height))
    background_photo = ImageTk.PhotoImage(background_image)
    
    # create a canvas to display the background image
    canvas = tk.Canvas(budget_window, width=window_width, height=window_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    # title label
    title_label = tk.Label(canvas, text="Budget Planner", font=("Arial", 20, "bold"), bg="#FA8072", fg="white")
    canvas.create_window(window_width // 2, 80, window=title_label, anchor="n")

    # label
    budget_label = tk.Label(canvas, text="Enter your budget amount:", font=("Arial", 12), bg="#FA8072", fg="white")
    canvas.create_window(window_width // 2, 150, window=budget_label, anchor="n")

    # entry
    global budget_entry
    budget_entry = tk.Entry(canvas, font=("Arial", 12), bg="white", fg="black", width=20)
    canvas.create_window(window_width // 2, 180, window=budget_entry, anchor="n")

    continue_button = tk.Button(canvas, text="Continue", command=lambda: continue_with_budget(budget_window, filter_parameters, beneficiary_id), font=("Arial", 12, "bold"), bg="lightcoral", fg="white")
    canvas.create_window(window_width // 2, 240, window=continue_button, anchor="n")

    continue_without_button = tk.Button(canvas, text="Continue without Budget Planner", command=lambda: continue_without_budget(budget_window, filter_parameters, beneficiary_id), font=("Arial", 12, "bold"), bg="lightcoral", fg="white")
    canvas.create_window(window_width // 2, 290, window=continue_without_button, anchor="n")

    budget_window.mainloop()

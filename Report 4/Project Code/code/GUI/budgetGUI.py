# IF SELECT AND FILTERS AND BUDGET PLANNER THEN SHOW INTERGRATED PACKAGES OTHERWISE SHOW THE APPROPRIATE SERVICES
# IMPLEMENT ONLY TO DISPLAY THE SERVICES IN ORDER TO MAKE A RESERVATION
import tkinter as tk
from packagesGUI import showPackages
from exploreDestinationGUI import showServices

def chooseBudget():
    budget_amount = budget_entry.get()
    if check(budget_amount):
        return float(budget_amount)
    else:
        notFilled()

def check(budget_amount):
    if budget_amount:
        return True
    else:
        return False

def notFilled():
    print("Please fill in your budget.")

def chooseBudgetMess(window):
    tk.messagebox.showinfo("Message", "Please fill in your budget.")
    window.destroy()

def continue_with_budget(window, filter_parameters):
    budget_amount = chooseBudget()
    if filter_parameters or budget_amount:
        window.destroy()
        showServices(filter_parameters, budget_amount)
    elif filter_parameters:
        window.destroy()
        showPackages(filter_parameters, budget_amount)

def continue_without_budget(window, filter_parameters):
    print("Continue without Budget Planner")
    window.destroy()
    showServices(filter_parameters)

def showBudget(filter_parameters):
    budget_window = tk.Tk()
    budget_window.title("Budget Planner")
    budget_window.configure(bg="#FA8072")

    window_width = 360
    window_height = 640
    budget_window.geometry(f"{window_width}x{window_height}")
    budget_window.configure(bg="#FA8072")
    
    budget_label = tk.Label(budget_window, text="Enter your budget amount:", bg="#FA8072", fg="white")
    budget_label.pack(pady=10)

    global budget_entry
    budget_entry = tk.Entry(budget_window, bg="white", fg="black", width=20)
    budget_entry.pack(pady=5)

    continue_button = tk.Button(budget_window, text="Continue", command=lambda: continue_with_budget(budget_window, filter_parameters), bg="lightcoral")
    continue_button.pack(pady=10)

    continue_without_button = tk.Button(budget_window, text="Continue without Budget Planner", command=lambda: continue_without_budget(budget_window, filter_parameters), bg="lightcoral")
    continue_without_button.pack()

    budget_window.mainloop()
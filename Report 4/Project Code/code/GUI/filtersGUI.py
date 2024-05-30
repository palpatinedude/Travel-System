import tkinter as tk
from budgetGUI import showBudget

#  variables globally
solo_var = None
couple_var = None
family_var = None
group_var = None
eco_var = None
adventurous_var = None
sightseeing_var = None
nature_var = None
city_var = None
mountain_var = None
relaxation_var = None
cultural_var = None
countryside_var = None

def goToBudgetGUI(window,beneficiary_id):
    global solo_var, couple_var, family_var, group_var, eco_var, adventurous_var, sightseeing_var, nature_var, city_var, mountain_var, relaxation_var, cultural_var, countryside_var
    
    selected_filters = []
    if solo_var.get():
        selected_filters.append("Solo traveler")
    if couple_var.get():
        selected_filters.append("Couple traveler")
    if family_var.get():
        selected_filters.append("Family traveler")
    if group_var.get():
        selected_filters.append("Group traveler")
    if eco_var.get():
        selected_filters.append("Eco-friendly travel")
    if adventurous_var.get():
        selected_filters.append("Adventurous")
    if sightseeing_var.get():
        selected_filters.append("Sightseeing")
    if nature_var.get():
        selected_filters.append("Nature exploration")
    if city_var.get():
        selected_filters.append("City")
    if mountain_var.get():
        selected_filters.append("Mountain")
    if relaxation_var.get():
        selected_filters.append("Relaxation")
    if cultural_var.get():
        selected_filters.append("Cultural experiences")
    if countryside_var.get():
        selected_filters.append("Countryside")

    window.destroy()  
    showBudget(selected_filters,beneficiary_id)

def chooseFilters(beneficiary_id):
    global solo_var, couple_var, family_var, group_var, eco_var, adventurous_var, sightseeing_var, nature_var, city_var, mountain_var, relaxation_var, cultural_var, countryside_var
    
    filter_window = tk.Tk()
    filter_window.title("Choose Filters")

    window_width = 360
    window_height = 640
    filter_window.geometry(f"{window_width}x{window_height}")
    filter_window.configure(bg="#FA8072")

    # variables
    solo_var = tk.IntVar()
    couple_var = tk.IntVar()
    family_var = tk.IntVar()
    group_var = tk.IntVar()
    eco_var = tk.IntVar()
    adventurous_var = tk.IntVar()
    sightseeing_var = tk.IntVar()
    nature_var = tk.IntVar()
    city_var = tk.IntVar()
    mountain_var = tk.IntVar()
    relaxation_var = tk.IntVar()
    cultural_var = tk.IntVar()
    countryside_var = tk.IntVar()

    # checkboxes
    checkbox_width = 16
    checkbox_height = 1

    font_size = 9

    checkbox_font = ("Arial", font_size, "bold")  

    solo_cb = tk.Checkbutton(filter_window, text="Solo traveler", variable=solo_var, bg="lightblue", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    solo_cb.pack(anchor="center", pady=10)
    couple_cb = tk.Checkbutton(filter_window, text="Couple traveler", variable=couple_var, bg="lightgreen", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    couple_cb.pack(anchor="center", pady=10)
    family_cb = tk.Checkbutton(filter_window, text="Family traveler", variable=family_var, bg="lightyellow", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    family_cb.pack(anchor="center", pady=10)
    group_cb = tk.Checkbutton(filter_window, text="Group traveler", variable=group_var, bg="lightcoral", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    group_cb.pack(anchor="center", pady=10)
    eco_cb = tk.Checkbutton(filter_window, text="Eco-friendly travel", variable=eco_var, bg="lightpink", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    eco_cb.pack(anchor="center", pady=10)
    adventurous_cb = tk.Checkbutton(filter_window, text="Adventurous", variable=adventurous_var, bg="lightsalmon", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    adventurous_cb.pack(anchor="center", pady=10)
    sightseeing_cb = tk.Checkbutton(filter_window, text="Sightseeing", variable=sightseeing_var, bg="lightcyan", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    sightseeing_cb.pack(anchor="center", pady=10)
    nature_cb = tk.Checkbutton(filter_window, text="Nature exploration", variable=nature_var, bg="lightseagreen", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    nature_cb.pack(anchor="center", pady=10)
    city_cb = tk.Checkbutton(filter_window, text="City", variable=city_var, bg="lightgrey", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    city_cb.pack(anchor="center", pady=10)
    mountain_cb = tk.Checkbutton(filter_window, text="Mountain", variable=mountain_var, bg="lightgoldenrodyellow", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    mountain_cb.pack(anchor="center", pady=10)
    relaxation_cb = tk.Checkbutton(filter_window, text="Relaxation", variable=relaxation_var, bg="lightcoral", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    relaxation_cb.pack(anchor="center", pady=10)
    cultural_cb = tk.Checkbutton(filter_window, text="Cultural experiences", variable=cultural_var, bg="lightgreen", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    cultural_cb.pack(anchor="center", pady=10)
    countryside_cb = tk.Checkbutton(filter_window, text="Countryside", variable=countryside_var, bg="lightblue", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    countryside_cb.pack(anchor="center", pady=10)


    explore_button = tk.Button(filter_window, text="Explore", command=lambda: goToBudgetGUI(filter_window,beneficiary_id), bg="lightcoral", width=checkbox_width, height=checkbox_height, font=checkbox_font)
    explore_button.pack(pady=10)

    filter_window.mainloop()



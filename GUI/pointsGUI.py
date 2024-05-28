import sys
sys.path.append('functions')
sys.path.append('classes')
import tkinter as tk
from tkinter import PhotoImage
from points import Points

def displayPoints(beneficiary_id):
    points_window = tk.Tk()
    points_window.title("Points Page")

    # set window dimensions
    window_width = 360
    window_height = 640
    points_window.geometry(f"{window_width}x{window_height}")
    points_window.configure(bg="#33A1C9")

    # label to display points page title
    points_label = tk.Label(points_window, text="Points Page", font=("Arial", 24), bg="lightblue", fg="black")
    points_label.pack(pady=20)

    my_points_label = tk.Label(points_window, text="My Points", font=("Arial", 16), bg="#33A1C9", fg="black")
    my_points_label.pack(pady=20)

    points_instance = Points()
    points = points_instance.getPoints(beneficiary_id)
    
    points_value = points[0] if points else 0
    points_info_label = tk.Label(points_window, text=f"{points_value}", font=("Arial", 14), bg="#33A1C9", fg="black")
    points_info_label.pack(pady=10)

    button_frame = tk.Frame(points_window, bg="#33A1C9")
    button_frame.pack(pady=20)

    scan_card_button = tk.Button(button_frame, text="Scan Card", font=("Arial", 12), bg="pink", fg="black", width=12, height=2)
    scan_card_button.grid(row=0, column=0, padx=20)

    points_history_button = tk.Button(button_frame, text="Points History", font=("Arial", 12), bg="pink", fg="black", width=12, height=2)
    points_history_button.grid(row=0, column=1, padx=20)

    vouchers_button = tk.Button(button_frame, text="Vouchers", font=("Arial", 12), bg="pink", fg="black", width=12, height=2)
    vouchers_button.grid(row=1, column=0, padx=20)

    voucher_map_button = tk.Button(button_frame, text="Voucher Map", font=("Arial", 12), bg="pink", fg="black", width=12, height=2)
    voucher_map_button.grid(row=1, column=1, padx=20)

    img = tk.PhotoImage(file="../images/reward.png")  
    img_label = tk.Label(points_window, image=img, bg="#33A1C9")
    img_label.image = img 
    img_label.pack(pady=20)

    points_window.mainloop()
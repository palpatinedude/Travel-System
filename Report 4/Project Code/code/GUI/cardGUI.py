import sys
sys.path.append('../database/')
import tkinter as tk
from tkinter import messagebox
from db_connector import create_connection
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageTk

# function to resize  image
def resize(image, width, height):
    resized_image = image.resize((width, height))
    return resized_image

# function to generate  barcode
def generateBarcode(barcode_value, bg_color="#D2691E", fg_color="white"):
    # generate barcode image
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(f'978{barcode_value}', writer=ImageWriter())
    ean.default_writer_options.update({
        'background': bg_color,
        'foreground': fg_color,
        'write_text': False
    })
    barcode_image = ean.render()  
    return barcode_image

def displayCard():
    card_window = tk.Tk()
    card_window.title("Card Page")

    # set window dimensions
    window_width = 360
    window_height = 640
    card_window.geometry(f"{window_width}x{window_height}")
    card_window.configure(bg="#33A1C9")

    card_label = tk.Label(card_window, text="Card Membership", font=("Arial", 20), bg="lightblue", fg="#D2691E")
    card_label.pack(pady=30)

    # frame to display the card details
    card_frame = tk.Frame(card_window,  width=400, height=200, bg="#D2691E")
    card_frame.pack(pady=50)

    
    company_label = tk.Label(card_frame, text="OdysseyExp", font=("Arial", 16, "bold"), bg="#D2691E", fg="white")
    company_label.pack(pady=10)

    # beneficiary details from the database
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                # query to fetch beneficiary's name and barcode
                cursor.execute("""
                SELECT u.name, u.lastname, c.barcode 
                FROM Card c 
                JOIN Beneficiary b ON c.beneficiary_id = b.beneficiary_id 
                JOIN User u ON b.user_id = u.user_id
                """)
                beneficiary_details = cursor.fetchone() 
                
                if beneficiary_details:
                    beneficiary_name, lastname, barcode_value = beneficiary_details[:3]

                    # display beneficiary's name
                    beneficiary_label = tk.Label(card_frame, text=f"{beneficiary_name} {lastname}", font=("Arial", 12), bg="#D2691E", fg="white")
                    beneficiary_label.pack(pady=5)

                    barcode_image = generateBarcode(barcode_value)
                    resized_barcode_image = resize(barcode_image, 250, 100)

                    # Convert barcode image to tkinter format
                    barcode_photo = ImageTk.PhotoImage(resized_barcode_image)
                    barcode_label = tk.Label(card_frame, image=barcode_photo, bg="#D2691E")
                    barcode_label.image = barcode_photo  
                    barcode_label.pack(pady=5)
                else:
                    messagebox.showwarning("No Data", "No beneficiary found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            connection.close()

    # frame for buttons 
    button_frame = tk.Frame(card_window, bg="#D2691E")
    button_frame.pack(pady=20)

    scan_button = tk.Button(button_frame, text="Scan", font=("Arial", 12), bg="#D2691E", fg="black")
    scan_button.pack(side="left", padx=10)

    details_button = tk.Button(button_frame, text="Details Of Card", font=("Arial", 12), bg="#D2691E", fg="black")
    details_button.pack(side="left", padx=10)

    settings_button = tk.Button(button_frame, text="Settings", font=("Arial", 12),  bg="#D2691E", fg="black")
    settings_button.pack(side="left", padx=10)   

    # frame to display previous card uses
    previous_uses_frame = tk.Frame(card_window, bg="#D2691E")
    previous_uses_frame.pack(pady=20)


    # fetch previous uses of the card from the database
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                # query to fetch previous card uses
                cursor.execute("""
               SELECT b.business_name
               FROM PointsHistory ph
               JOIN Points p ON ph.points_id = p.points_id
               JOIN Card c ON p.card_id = c.card_id
               JOIN Beneficiary bf ON c.beneficiary_id = bf.beneficiary_id
               JOIN User u ON bf.user_id = u.user_id
               JOIN Business b ON ph.business_id = b.business_id
               WHERE u.name = %s AND u.lastname = %s;
                """, (beneficiary_name, lastname))
                previous_uses = cursor.fetchall() 
                
                if previous_uses:
                    for use in previous_uses:
                        business_name = use[0]
                        # display previous use of the card
                        previous_use_label = tk.Label(previous_uses_frame, text=f"Previous Use: {business_name}", font=("Arial", 12), bg="#D2691E", fg="white")
                        previous_use_label.pack(pady=5)
                else:
                    # display message if no previous uses found
                    no_previous_use_label = tk.Label(previous_uses_frame, text="No previous use", font=("Arial", 12), bg="#D2691E", fg="white")
                    no_previous_use_label.pack(pady=5)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            connection.close()
 

    card_window.mainloop()

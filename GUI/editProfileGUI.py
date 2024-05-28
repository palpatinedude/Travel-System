import sys
sys.path.append('classes')
import tkinter as tk
from user import User
from beneficiary import Beneficiary
from simpleUser import SimpleUser
from serviceProvider import ServiceProvider

def saveInfo(window, username_entry, password_entry, user_type, beneficiary_id, bistory_entry=None, preferences_entry=None, certifications_entry=None, specialities_entry=None, languages_entry=None):
    print("Profile saved")
    username = username_entry.get()
    password = password_entry.get()
    
    # retrieve user_id using beneficiary_id
    user_id = Beneficiary.get_id_by_beneficiary_id(beneficiary_id)
    print(user_id)

  
    user = User.get_by_id(user_id)
    if user:
        # Update username and password if they are provided and not empty
        if username:
            user.username = username
        if password:
            user.password = password
        
        # update user information
        user.update(username=user.username, password=user.password)  # save changes to the database
    else:
        print("User with the given user_id not found.")
        return

    # update additional attributes based on the user_type
    if user_type == "Simple User":
        bistory = bistory_entry.get()
        preferences = preferences_entry.get()
        simple_user = SimpleUser.get_by_id(beneficiary_id)
        if simple_user:
            # update bistory and preferences if they are provided and not empty
            if bistory:
                simple_user.bistory = bistory
            if preferences:
                simple_user.preferences = preferences
            print(simple_user.bistory, simple_user.preferences)    
            simple_user.update(beneficiary_id=beneficiary_id,bistory=simple_user.bistory, preferences=simple_user.preferences)
            print("SimpleUser updated successfully!")
        else:
            print("SimpleUser with the given beneficiary_id not found.")

    elif user_type == "Service Provider":
        certifications = certifications_entry.get()
        specialities = specialities_entry.get()
        languages_spoken = languages_entry.get()
        service_provider = ServiceProvider.get_by_id(beneficiary_id)
        if service_provider:
            # θpdate certifications, specialities, and languages_spoken if they are provided and not empty
            if certifications:
                service_provider.certifications = certifications
            if specialities:
                service_provider.specialities = specialities
            if languages_spoken:
                service_provider.languages_spoken = languages_spoken
            service_provider.update(certifications=service_provider.certifications, specialities=service_provider.specialities, languages_spoken=service_provider.languages_spoken)
            print("ServiceProvider updated successfully!")
        else:
            print("ServiceProvider with the given beneficiary_id not found.")    


def changeMyInfo(beneficiary_id, user_type):
    edit_window = tk.Tk()
    edit_window.title("Edit Profile")

    # set window dimensions (phone size)
    window_width = 360
    window_height = 640
    edit_window.geometry(f"{window_width}x{window_height}")
    edit_window.configure(bg="#D3D3D3")

    title_label = tk.Label(edit_window, text="Edit Profile", font=("Arial", 20), bg="#D3D3D3", fg="black")
    title_label.pack(pady=20)

    # frame for form entries
    form_frame = tk.Frame(edit_window, bg="#D3D3D3")
    form_frame.pack(pady=10)

    username_label = tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#D3D3D3", fg="black")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    username_entry = tk.Entry(form_frame, font=("Arial", 12))
    username_entry.grid(row=0, column=1, padx=10, pady=10)


    password_label = tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#D3D3D3", fg="black")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    password_entry = tk.Entry(form_frame, font=("Arial", 12), show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    if user_type == "Simple User":

        bistory_label = tk.Label(form_frame, text="Bistory:", font=("Arial", 12), bg="#D3D3D3", fg="black")
        bistory_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        bistory_entry = tk.Entry(form_frame, font=("Arial", 12))
        bistory_entry.grid(row=2, column=1, padx=10, pady=10)

     
        preferences_label = tk.Label(form_frame, text="Preferences:", font=("Arial", 12), bg="#D3D3D3", fg="black")
        preferences_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        preferences_entry = tk.Entry(form_frame, font=("Arial", 12))
        preferences_entry.grid(row=3, column=1, padx=10, pady=10)

    elif user_type == "Service Provider":

        certifications_label = tk.Label(form_frame, text="Certifications:", font=("Arial", 12), bg="#D3D3D3", fg="black")
        certifications_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        certifications_entry = tk.Entry(form_frame, font=("Arial", 12))
        certifications_entry.grid(row=2, column=1, padx=10, pady=10)

        specialities_label = tk.Label(form_frame, text="Specialities:", font=("Arial", 12), bg="#D3D3D3", fg="black")
        specialities_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        specialities_entry = tk.Entry(form_frame, font=("Arial", 12))
        specialities_entry.grid(row=3, column=1, padx=10, pady=10)

        languages_label = tk.Label(form_frame, text="Languages Spoken:", font=("Arial", 12), bg="#D3D3D3", fg="black")
        languages_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        languages_entry = tk.Entry(form_frame, font=("Arial", 12))
        languages_entry.grid(row=4, column=1, padx=10, pady=10)


    save_button = tk.Button(edit_window, text="Save", command=lambda: saveInfo(edit_window, username_entry, password_entry, user_type, beneficiary_id,bistory_entry if user_type == "Simple User" else None, preferences_entry if user_type == "Simple User" else None, certifications_entry if user_type == "Service Provider" else None, specialities_entry if user_type == "Service Provider" else None, languages_entry if user_type == "Service Provider" else None), font=("Arial", 12), bg="#4CAF50", fg="white", width=20)
    save_button.pack(pady=20)

    edit_window.mainloop()
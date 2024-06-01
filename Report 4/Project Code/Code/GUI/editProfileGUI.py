import sys
sys.path.append('../classes/')
sys.path.append('../functions/')
import tkinter as tk
from allClasses import Beneficiary, SimpleUser, ServiceProvider, User
from beneficiaryDetails import validateBistory, validatePreferences, validateCertifications, validateSpecialities
from registAuthentication import validatePassword, validateUsername


def saveInfo(window, username_entry, password_entry, user_type, beneficiary_id, bistory_entry=None, preferences_entry=None, certifications_entry=None, specialities_entry=None, languages_entry=None):
    print("Profile saved")
    username = username_entry.get()
    password = password_entry.get()
    
    # validate username and password
    is_valid_username, username_error = validateUsername(username)
    is_valid_password, password_error = validatePassword(password)
    
    if not is_valid_username:
        tk.messagebox.showerror("Input Error", username_error)
        return
    if not is_valid_password:
        tk.messagebox.showerror("Input Error", password_error)
        return
    
    # retrieve user_id using beneficiary_id
    user_id = Beneficiary.get_id_by_beneficiary_id(beneficiary_id)
    print(user_id)

    user = User.get_by_id(user_id)
    if user:
        # update username and password if they are provided and not empty
        if username:
            user.username = username
        if password:
            user.password = password
        
        # update user information
        user.update(username=user.username, password=user.password)  
    else:
        print("User with the given user_id not found.")
        return

 
    if user_type == "Simple User":
        bistory = bistory_entry.get()
        preferences = preferences_entry.get()
        
        # validate bistory and preferences
        is_valid_bistory, bistory_error = validateBistory(bistory)
        is_valid_preferences, preferences_error = validatePreferences(preferences)
        
        if not is_valid_bistory:
            tk.messagebox.showerror("Input Error", bistory_error)
            return
        if not is_valid_preferences:
            tk.messagebox.showerror("Input Error", preferences_error)
            return
        
        simple_user = SimpleUser.get_by_id(beneficiary_id)
        if simple_user:
            # update bistory and preferences if they are provided and not empty
            if bistory:
                simple_user.bistory = bistory
            if preferences:
                simple_user.preferences = preferences
                
            simple_user.update(beneficiary_id=beneficiary_id, bistory=simple_user.bistory, preferences=simple_user.preferences)
            print("SimpleUser updated successfully!")
        else:
            print("SimpleUser with the given beneficiary_id not found.")

    elif user_type == "Service Provider":
        certifications = certifications_entry.get()
        specialities = specialities_entry.get()
        languages_spoken = languages_entry.get()
        
        # validate certifications and specialities
        is_valid_certifications, certifications_error = validateCertifications(certifications)
        is_valid_specialities, specialities_error = validateSpecialities(specialities)
        
        if not is_valid_certifications:
            tk.messagebox.showerror("Input Error", certifications_error)
            return
        if not is_valid_specialities:
            tk.messagebox.showerror("Input Error", specialities_error)
            return
        
        service_provider = ServiceProvider.get_by_id(beneficiary_id)
        if service_provider:
            # update certifications, specialities, and languages_spoken if they are provided and not empty
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

    # set window dimensions
    window_width = 360
    window_height = 640
    edit_window.geometry(f"{window_width}x{window_height}")
    edit_window.configure(bg="#D3D3D3")

    title_label = tk.Label(edit_window, text="Edit Profile", font=("Arial", 20), bg="#D3D3D3", fg="black")
    title_label.pack(pady=20)

    # form entries
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

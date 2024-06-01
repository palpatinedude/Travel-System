import re
from datetime import datetime
from tkinter import messagebox
from db_connector import create_connection
from allClasses import SimpleUser, ServiceProvider, Beneficiary



def validateBistory(bistory_entry):
    max_chars = 100
    if not bistory_entry:
        return False, "Bistory cannot be empty."

    if len(bistory_entry) > max_chars:
        return False, f"Bistory exceeds maximum character limit of {max_chars}."

    if any(char.isdigit() for char in bistory_entry):
        return False, "Bistory cannot contain numbers."

    return True, None

def validatePreferences(preferences_entry):
    max_chars = 50
    if not preferences_entry:
        return False, "Preferences cannot be empty."

    if len(preferences_entry) > max_chars:
        return False, f"Preferences exceeds maximum character limit of {max_chars}."

    if any(char.isdigit() for char in preferences_entry):
        return False, "Preferences cannot contain numbers."

    return True, None

def validateCertifications(certifications_entry):
    max_chars = 50
    if not certifications_entry:
        return False, "Certifications cannot be empty."

    if len(certifications_entry) > max_chars:
        return False, f"Certifications exceeds maximum character limit of {max_chars}."

    if any(char.isdigit() for char in certifications_entry):
        return False, "Certifications cannot contain numbers."

    return True, None

def validateSpecialities(specialities_entry):
    max_chars = 50
    if not specialities_entry:
        return False, "Specialities cannot be empty."

    if len(specialities_entry) > max_chars:
        return False, f"Specialities exceeds maximum character limit of {max_chars}."

    if any(char.isdigit() for char in specialities_entry):
        return False, "Specialities cannot contain numbers."

    return True, None

def beneficiaryDetails(user_id, beneficiary_type, dob_entry, address_entry, contact_number_entry, additional_entries, window):
    dob = dob_entry.get()
    address = address_entry.get()
    contact_number = contact_number_entry.get()

    if not all([dob, address, contact_number]):
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    try:
        dob = datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Input Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    if not re.match(r'^[0-9+\-\(\)\s]+$', contact_number):
        messagebox.showerror("Input Error", "Invalid contact number. Please use only digits, spaces, hyphens, and parentheses.")
        return

    connection = create_connection()
    cursor = connection.cursor()
    try:
        beneficiary = Beneficiary.get_by_id(user_id)
        if beneficiary:
            beneficiary.update(date_of_birth=dob, address=address, contact_number=contact_number)
            beneficiary_id = beneficiary.beneficiary_id
            if beneficiary_type == "Simple User":
                if len(additional_entries) != 2:
                    messagebox.showerror("Input Error", "Invalid number of additional entries for Simple User.")
                    return
                bistory_entry, preferences_entry = additional_entries
                is_valid_bistory, bistory_error = validateBistory(bistory_entry)
                is_valid_preferences, preferences_error = validatePreferences(preferences_entry)
                if not is_valid_bistory:
                    messagebox.showerror("Input Error", bistory_error)
                    return
                if not is_valid_preferences:
                    messagebox.showerror("Input Error", preferences_error)
                    return
                simple_user = SimpleUser(beneficiary_id=beneficiary_id, bistory=bistory_entry, preferences=preferences_entry)
                simple_user.save()
            elif beneficiary_type == "Service Provider":
                if len(additional_entries) != 3:
                    messagebox.showerror("Input Error", "Invalid number of additional entries for Service Provider.")
                    return
                languages_spoken_entry, specialties_entry, certifications_entry = additional_entries
                is_valid_specialities, specialities_error = validateSpecialities(specialties_entry)
                is_valid_certifications, certifications_error = validateCertifications(certifications_entry)
                if not is_valid_specialities:
                    messagebox.showerror("Input Error", specialities_error)
                    return
                if not is_valid_certifications:
                    messagebox.showerror("Input Error", certifications_error)
                    return
                service_provider = ServiceProvider(beneficiary_id=beneficiary_id, languages_spoken=languages_spoken_entry, specialties=specialties_entry, certifications=certifications_entry)
                service_provider.save()

            messagebox.showinfo("Success", "Beneficiary details saved successfully.")
        else:
            messagebox.showerror("Error", "Beneficiary not found.")
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        connection.close()
      #  window.destroy()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ContactsApp:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Contact Management System - PRODIGY INFOTECH")
        
        self.contact_data = self.load_contact_data()

        title = tk.Label(main_window, text="Contact Management System", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        self.add_contact_button = tk.Button(main_window, text="Add Contact", command=self.add_new_contact)
        self.add_contact_button.pack(pady=5)

        self.view_contact_button = tk.Button(main_window, text="View Contacts", command=self.display_contacts)
        self.view_contact_button.pack(pady=5)

        self.edit_contact_button = tk.Button(main_window, text="Edit Contact", command=self.modify_contact)
        self.edit_contact_button.pack(pady=5)

        self.delete_contact_button = tk.Button(main_window, text="Delete Contact", command=self.remove_contact)
        self.delete_contact_button.pack(pady=5)

    def load_contact_data(self):
        if os.path.isfile("contacts.json"):
            with open("contacts.json", "r") as file:
                return json.load(file)
        return {}

    def save_contact_data(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contact_data, file, indent=4)

    def add_new_contact(self):
        name = simpledialog.askstring("Input", "Please enter the contact's name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Please enter the phone number:")
        if not phone:
            return
        email = simpledialog.askstring("Input", "Please enter the email address:")
        if not email:
            return

        self.contact_data[name] = {"phone": phone, "email": email}
        self.save_contact_data()
        messagebox.showinfo("Success", "Contact has been added successfully!")

    def display_contacts(self):
        contact_info = ""
        for name, details in self.contact_data.items():
            contact_info += f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\n\n"
        
        if contact_info:
            messagebox.showinfo("Contact List", contact_info)
        else:
            messagebox.showinfo("Contact List", "No contacts available.")

    def modify_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact you want to modify:")
        if name not in self.contact_data:
            messagebox.showerror("Error", "This contact does not exist.")
            return

        phone = simpledialog.askstring("Input", "Enter the new phone number:", initialvalue=self.contact_data[name]["phone"])
        if not phone:
            return
        email = simpledialog.askstring("Input", "Enter the new email address:", initialvalue=self.contact_data[name]["email"])
        if not email:
            return

        self.contact_data[name] = {"phone": phone, "email": email}
        self.save_contact_data()
        messagebox.showinfo("Success", "Contact has been updated successfully!")

    def remove_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to remove:")
        if name not in self.contact_data:
            messagebox.showerror("Error", "This contact does not exist.")
            return

        del self.contact_data[name]
        self.save_contact_data()
        messagebox.showinfo("Success", "Contact has been deleted successfully!")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = ContactsApp(main_window)
    main_window.mainloop()

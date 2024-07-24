import tkinter as tk
from tkinter import simpledialog, messagebox

class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def update_contact(self, index, contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = contact

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)

    def get_contact(self, index):
        if 0 <= index < len(self.contacts):
            return self.contacts[index]
        return None

    def search_contacts(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                results.append(contact)
        return results

    def get_all_contacts(self):
        return self.contacts

class ContactApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.manager = ContactManager()

        self.contact_listbox = tk.Listbox(root, width=50, height=15)
        self.contact_listbox.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Contact", command=self.view_contact)
        self.view_button.pack()

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def refresh_listbox(self, contacts=None):
        self.contact_listbox.delete(0, tk.END)
        if contacts is None:
            contacts = self.manager.get_all_contacts()
        for idx, contact in enumerate(contacts):
            self.contact_listbox.insert(tk.END, f"{idx + 1}. {contact.name} - {contact.phone}")

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter name:")
        phone = simpledialog.askstring("Add Contact", "Enter phone number:")
        email = simpledialog.askstring("Add Contact", "Enter email:")
        address = simpledialog.askstring("Add Contact", "Enter address:")
        if name and phone:
            contact = Contact(name, phone, email, address)
            self.manager.add_contact(contact)
            self.refresh_listbox()

    def view_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            contact = self.manager.get_contact(selected_index)
            if contact:
                messagebox.showinfo("View Contact", f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}")
        except IndexError:
            messagebox.showwarning("View Contact", "Please select a contact to view.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number to search:")
        if search_term:
            results = self.manager.search_contacts(search_term)
            self.refresh_listbox(results)

    def update_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            contact = self.manager.get_contact(selected_index)
            if contact:
                name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact.name)
                phone = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contact.phone)
                email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact.email)
                address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact.address)
                if name and phone:
                    updated_contact = Contact(name, phone, email, address)
                    self.manager.update_contact(selected_index, updated_contact)
                    self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Update Contact", "Please select a contact to update.")

    def delete_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            self.manager.delete_contact(selected_index)
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Delete Contact", "Please select a contact to delete.")

if _name_ == "_main_":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()

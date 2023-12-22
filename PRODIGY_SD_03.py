#Implement a Simple Contact Management System

#Develop a program that allows users to store and manage contact information. The program should provide options to add a new contact by entering their name, phone number, and email address. It should also allow users to view their contact list, edit existing contacts, and delete contacts if needed. The program should store the contacts in memory or in a file for persistent storage.

import json

class ContactManagementSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(contact)
        print(f"Contact for {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact['name']} - Phone: {contact['phone_number']}, Email: {contact['email']}")

    def edit_contact(self, index, name, phone_number, email):
        if 1 <= index <= len(self.contacts):
            self.contacts[index - 1] = {'name': name, 'phone_number': phone_number, 'email': email}
            print(f"Contact for {name} edited successfully!")
        else:
            print("Invalid index. Please provide a valid index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact for {deleted_contact['name']} deleted successfully!")
        else:
            print("Invalid index. Please provide a valid index.")

    def save_to_file(self, filename='contacts.json'):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
        print(f"Contacts saved to {filename}.")

    def load_from_file(self, filename='contacts.json'):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print(f"No contacts file found. Starting with an empty contact list.")

def main():
    cms = ContactManagementSystem()

    while True:
        print("\nContact Management System Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            cms.add_contact(name, phone_number, email)
        elif choice == '2':
            cms.view_contacts()
        elif choice == '3':
            index = int(input("Enter the index of the contact to edit: "))
            name = input("Enter the updated name: ")
            phone_number = input("Enter the updated phone number: ")
            email = input("Enter the updated email address: ")
            cms.edit_contact(index, name, phone_number, email)
        elif choice == '4':
            index = int(input("Enter the index of the contact to delete: "))
            cms.delete_contact(index)
        elif choice == '5':
            filename = input("Enter the filename to save contacts (default: contacts.json): ")
            cms.save_to_file(filename)
        elif choice == '6':
            filename = input("Enter the filename to load contacts from (default: contacts.json): ")
            cms.load_from_file(filename)
        elif choice == '7':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

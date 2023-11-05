class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class ContactManager:
    def __init__(self):
        self.contacts = []
      
    def add_contact(self, contact):
        self.contacts.append(contact)
    def view_contacts(self):
        for i, contact in enumerate(self.contacts):
            print(f"{i + 1}. Name: {contact.name}, Phone: {contact.phone}")
    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if
                         search_term.lower() in contact.name.lower() or
                         search_term in contact.phone]
        if found_contacts:
            for i, contact in enumerate(found_contacts):
                print(f"{i + 1}. Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No contacts found.")
    def update_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")
    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")
def main():
    contact_manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter a name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            name = input("Enter the new name: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.update_contact(index - 1, new_contact)
       elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index - 1)
        elif choice == "6":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()

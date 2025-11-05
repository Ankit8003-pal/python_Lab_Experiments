import json
import os
1
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from JSON file with exception handling."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Contacts file is corrupt. Starting with empty contacts.")
        return []
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return []

def save_contacts(contacts):
    """Save contacts to JSON file."""
    try:
        with open(CONTACTS_FILE, 'w') as f:
            json.dump(contacts, f, indent=4)
    except Exception as e:
        print(f"Error saving contacts: {e}")

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def search_contacts(contacts):
    """Search contacts by name or phone."""
    query = input("Enter name or phone to search: ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if not results:
        print("No contacts found.")
        return
    print("\nSearch Results:")
    for contact in results:
        print(f"- Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ").strip().lower()
    if not name:
        print("Name cannot be empty.")
        return
    for contact in contacts:
        if contact['name'].lower() == name:
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            contact['phone'] = input("Enter new phone (leave blank to keep current): ").strip() or contact['phone']
            contact['email'] = input("Enter new email (leave blank to keep current): ").strip() or contact['email']
            save_contacts(contacts)
            print(f"Contact '{contact['name']}' updated successfully.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").strip().lower()
    if not name:
        print("Name cannot be empty.")
        return
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            del contacts[i]
            save_contacts(contacts)
            print(f"Contact '{contact['name']}' deleted successfully.")
            return
    print("Contact not found.")

def display_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts available.")
        return
    print("\nAll Contacts:")
    for contact in contacts:
        print(f"- Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            display_contacts(contacts)
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

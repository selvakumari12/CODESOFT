import json
CONTACT_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if name in contacts:
        print("Contact already exists.")
        return

    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")


def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip()
    found = False

    for name, details in contacts.items():
        if query.lower() in name.lower() or query in details["phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True

    if not found:
        print("No contact found.")


def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("Leave fields blank to keep current values.")
    phone = input(f"New phone number (current: {contacts[name]['phone']}): ").strip()
    email = input(f"New email (current: {contacts[name]['email']}): ").strip()
    address = input(f"New address (current: {contacts[name]['address']}): ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address

    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

contacts= []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    print("Contact added successfully!")


def show_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n===== CONTACTS =====")

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print()


def search_contact():
    search = input("Enter name to search: ").lower()

    found = False

    for contact in contacts:
        if search in contact["name"].lower():
            print("\nContact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    show_contacts()

    if not contacts:
        return

    number = int(input("Enter contact number to update: "))

    if 1 <= number <= len(contacts):
        contact = contacts[number - 1]

        contact["name"] = input("Enter new name: ")
        contact["phone"] = input("Enter new phone number: ")
        contact["email"] = input("Enter new email: ")

        print("Contact updated successfully!")

    else:
        print("Invalid contact number.")


def delete_contact():
    show_contacts()

    if not contacts:
        return

    number = int(input("Enter contact number to delete: "))

    if 1 <= number <= len(contacts):
        deleted_contact = contacts.pop(number - 1)

        print("Deleted:", deleted_contact["name"])

    else:
        print("Invalid contact number.")


while True:

    print("\n==== CONTACT BOOK ====")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

        
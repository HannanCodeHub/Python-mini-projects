contacts = []


def add_contacts():

    name = input("Enter a name: ")
    number = input("Enter a phone number: ")
    email = input("Enter email: ")

    info = {
        "name": name,
        "number": number,
        "email": email
    }

    contacts.append(info)


add_contacts()

print(contacts)
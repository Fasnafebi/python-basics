filename = "contacts.txt"

def load_contacts():
    contacts = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(filename, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact saved!\n")

def view_contacts(contacts):
    print("All Contacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

def search_contact(contacts):
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("Contact not found!")
    print()

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted!")
            break
    else:
        print("Contact not found!")
    print()

def main():
    contacts = load_contacts()
    
    while True:
        print("Contact Book")
        print("\t1\tAdd contact")
        print("\t2\tView all contacts")
        print("\t3\tSearch contact")
        print("\t4\tDelete contact")
        print("\t5\tExit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()

# Collection exercise

contacts = {}           # name → (phone, email)
registered_emails = set()   # for duplicate checking

while True:
    action = input("\n[a]dd / [l]ookup / [s]how / [q]uit: ").lower()
    if action == "q":
        break
    elif action == "a":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        if email in registered_emails:
            print("This email is already registered. Please try again.")
        else:
            registered_emails.add(email)
            contacts[name] = (phone, email)
    elif action == "l":
        name = input("Name: ")
        if name in contacts.keys():
            phone, email = contacts[name]
            print(f"Phone: {phone}, Email: {email}")
        else:
            print("Contact not found.")
    elif action == "s":
        for key, value in contacts.items():
            print(f"{key}: {value}")
    else:
        print("Invalid action. Please try again.")
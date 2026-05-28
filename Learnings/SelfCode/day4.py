# Contact Book with Error Handling

contacts = {}           # name → (phone, email)
registered_emails = set()   # for duplicate checking

class ContactBookError(Exception):
    def __init__(self, reason, message):
        self.reason = reason
        super().__init__(f"Contact Book Error - {reason}: {message}")
        
def add_contact(name, phone, email):
    if not name or not isinstance(name, str):
        raise ContactBookError("Invalid Name", "Name must be a non-empty string.")
    if not phone or not isinstance(phone, str):
        raise ContactBookError("Invalid Phone", "Phone must be a non-empty string.")
    if not email or not isinstance(email, str):
        raise ContactBookError("Invalid Email", "Email must be a non-empty string.")
    if "@" not in email:
        raise ContactBookError("Invalid Email", "Email must contain an '@' symbol.")
    if email in registered_emails:
        raise ContactBookError("Duplicate Email", "Email is already registered.")
    registered_emails.add(email)
    contacts[name] = (phone, email)
    
def lookup_contact(name):
    if name in contacts.keys():
        phone, email = contacts[name]
        print(f"Phone: {phone}, Email: {email}")
    else:
        raise ContactBookError("Lookup Failed", "Contact not found.")
    
def delete_contact(name):
    if name in contacts.keys():
        email = contacts[name][1]
        registered_emails.remove(email)
        del contacts[name]
        print(f"Contact '{name}' has been deleted.")
    else:
        raise ContactBookError("Delete Failed", "Contact not found.")
    
    
while True:
    action = input("\n[a]dd / [l]ookup / [s]how / [d]elete / [q]uit: ").lower()
    if action == "q":
        break
    else:
        try:
            if action == "a":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                add_contact(name, phone, email)
            elif action == "l":
                name = input("Name: ")
                lookup_contact(name)
            elif action == "s":
                for key, value in contacts.items():
                    print(f"{key}: {value}")
            elif action == "d":
                name = input("Name: ")
                delete_contact(name)
            else:
                print("Invalid action. Please try again.")
        except ContactBookError as e:
            print(e)
        finally:
            print(f"Contacts currently in the book: {len(contacts)}")
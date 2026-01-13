# Contact Book

# Storing Contacts
# ----------------
contacts = []

# Functions
# Add Contact


def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("✅ Contact Added Successfully.")


# View Contact
# --------------------
def view_contact():

    if not contacts:
        print("💾 No Contacts Yet")
        return

    print("📕 Your Contacts: ")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


# Search Contact
# ---------------
def search_contact(name):
    for c in contacts:
        if c["name"].lower() == name.lower():
            print("🔎 Contact Found.")
            print(f"{c['name']} | {c['phone']} | {c['email']}")
            return

    print("❌ Contact Not Found")


# Update Contact
# --------------
def update_contact(name):
    for c in contacts:
        if c["name"].lower() == name.lower():
            new_phone = input("New Phone: ")
            new_email = input("New Email: ")
            c["phone"] = new_phone
            c["email"] = new_email
            print("✏ Contact Updated")
            return

    print("❌ Contact Not Found")


# Delete Contact
# ----------------------------
def delete_contact(name):
    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            print("🗑 Contact Deleted")
            return

    print("❌ Contact Not Found")


# Main
# ----------------------
def main():

    while True:
        print("\n------ Contact Book ------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(name, phone, email)

        elif choice == "2":
            view_contact()

        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            update_contact(name)

        elif choice == "5":
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == "6":
            print("👋 Goodbye")
            break

        else:
            print("❌ Invalid Choice.")


# Run
if __name__ == "__main__":
    main()

import json

FILENAME = "passwords.json"


# -------------------- LOAD DATA --------------------
def load_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# -------------------- SAVE DATA --------------------
def save_data(accounts):
    with open(FILENAME, "w") as f:
        json.dump(accounts, f, indent=4)


# -------------------- ADD ACCOUNT --------------------
def add_account(accounts):
    app = input("Site/App Name: ")
    username = input("Username: ")
    password = input("Password: ")

    account = {
        "app": app,
        "username": username,
        "password": password
    }

    accounts.append(account)
    save_data(accounts)

    print("✅ Password saved successfully")


# -------------------- VIEW ALL ACCOUNTS --------------------
def view_accounts(accounts):
    if not accounts:
        print("❌ No accounts saved yet")
        return

    print("\nSaved Accounts:")
    for acc in accounts:
        print(f"- {acc['app']} ({acc['username']})")


# -------------------- SEARCH ACCOUNT --------------------
def search_account(accounts):
    name = input("Enter app/site name to search: ")

    for acc in accounts:
        if acc["app"].lower() == name.lower():
            print("\n🔐 Account Found:")
            print("App:", acc["app"])
            print("Username:", acc["username"])
            print("Password:", acc["password"])
            return

    print("❌ Account not found")


# -------------------- MAIN --------------------
def main():
    accounts = load_data()

    while True:
        print("\n------ PASSWORD MANAGER ------")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Search Account")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_account(accounts)

        elif choice == "2":
            view_accounts(accounts)

        elif choice == "3":
            search_account(accounts)

        elif choice == "4":
            print("👋 Goodbye")
            break

        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main()

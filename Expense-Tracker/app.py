# Expense Tracker

# Expenses
expenses = []

# add expense
# --------------------------------------------------


def add_expense(amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    print("✅ Expense Added Successfully.")

# View Expense
# -------------------------------------------


def view_expense():

    if not expenses:
        print("💾 No Expenses Yet!")
        return

    print("💵 Your Expenses:")
    for i, e in enumerate(expenses, start=1):
        print(f'{i}. {e['amount']} | {e["category"]} | {e["description"]}')


# total spent
# -------------------------------------------
def total_spent():

    total = 0

    for e in expenses:

        total += e["amount"]

    print("-"*50)
    print(f"\n💸 Total Amount Spent: {total}")
    return total


# Export to file
def export_file():
    filename = "Expenses.txt"

    with open(filename, "w") as f:
        for e in expenses:
            line = f"{e['amount']} | {e['category']} | {e['description']}\n"
            f.write(line)

    print(f"📁 Expenses exported to {filename}")

# main
# -----------------------------------------


def main():

    while True:

        print("\n")
        print("----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Show Total Spent")
        print("4. Export to File")
        print("5. Exit")

        choice = input("\n\nEnter your choice: ")

        if choice == "1":
            amount = int(input("\nAmount: "))
            category = input("\nCategory (Food/Travel/Bills): ")
            description = input("\nDescription: ")
            add_expense(amount, category, description)

        elif choice == "2":
            view_expense()

        elif choice == "3":
            total_spent()

        elif choice == "4":
            export_file()

        elif choice == "5":
            print("👋 Goodbye")

        else:
            print(" ❌ Invalid Choice")


# Run
if __name__ == "__main__":
    main()

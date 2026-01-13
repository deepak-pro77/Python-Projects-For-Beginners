# Notes
notes = []

# -------------------------------------------------------


def add_note(note):

    if note == "":
        print("❌ Note is Empty!")

    else:
        notes.append(note)
        print(f"✅ Note Added Successfully!")


def view_note():

    if not notes:
        print("❌ No Notes Found!")
    else:
        print("📝 Your Notes:")
        for note in notes:
            print("-", note)


def delete_note(note):

    if note in notes:
        notes.remove(note)
        print("🗑 Note Deleted Successfully")
    else:
        print("❌ Note does not exist")


def save_note():

    filename = "notes.txt"

    with open(filename, "w") as f:
        for note in notes:
            f.write(note + "\n")

# -------------------------------------------------


def main():

    print("-----------Notes App-------------")

    while True:

        print("-"*50)
        print("\n1. Add Note")
        print('2. View Note')
        print("3. Delete Note")
        print("4. Save Note")
        print("5. Exit")

        print('-'*50)
        choice = input("\nEnter your Choice: ")

        if choice == "1":
            note = input("📓 Note: ")
            add_note(note)
        elif choice == "2":
            view_note()
        elif choice == "3":
            note = input("📓 Enter Note to Delete: ").lower()
            delete_note(note)
        elif choice == "4":
            save_note()
        elif choice == "5":
            print("👋 GoodBye")
            break

        else:
            print("❌ Invalid Choice.")


# ----------------------------------------------
if __name__ == "__main__":
    main()

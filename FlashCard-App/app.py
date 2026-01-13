import random

flashcards = []


# Add flashcard
def add_card():
    question = input("Enter question: ")
    answer = input("Enter answer: ")

    card = {"question": question, "answer": answer}
    flashcards.append(card)

    print("✅ Flashcard added successfully!")


# View flashcards
def view_cards():
    if not flashcards:
        print("📭 No flashcards yet!")
        return

    print("\n📚 Your Flashcards:")
    for i, card in enumerate(flashcards, start=1):
        print(f"{i}. Q: {card['question']}  |  A: {card['answer']}")


# Quiz mode
def quiz_mode():
    if not flashcards:
        print("📭 No flashcards to quiz!")
        return

    card = random.choice(flashcards)
    print("\n🤔 Question:", card["question"])

    user = input("Your answer: ").strip().lower()

    if user == card["answer"].strip().lower():
        print("🎉 Correct!")
    else:
        print(f"❌ Wrong! Correct answer is: {card['answer']}")


# Delete flashcard
def delete_card():
    view_cards()

    if not flashcards:
        return

    try:
        index = int(input("\nEnter card number to delete: "))
        flashcards.pop(index - 1)
        print("🗑️ Flashcard deleted.")
    except:
        print("❌ Invalid choice")


# Main menu
def main():
    while True:
        print("\n------ Flashcard App ------")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Quiz Mode")
        print("4. Delete Flashcard")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_card()
        elif choice == "2":
            view_cards()
        elif choice == "3":
            quiz_mode()
        elif choice == "4":
            delete_card()
        elif choice == "5":
            print("👋 Goodbye")
            break
        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main()

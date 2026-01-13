# Word Counter

def word_counter(text):

    text = text.strip()

    # word count
    words = text.split()
    word_count = len(words)

    # character count
    char_count = len(text.replace(" ", ""))

    print(f"\n🧾 Total Words: {word_count}")
    print(f"🔠 Total Characters (no spaces): {char_count}")


# main
def main():

    print('---------Word Counter --------------')

    while True:

        text = input("\nInput Text: ")

        if not text.strip():
            print("❌ Please enter some text.")
            continue

        word_counter(text)

        again = input("\nCount again? (yes/no): ").lower()
        if again == "no":
            print("👋 Goodbye!")
            break


# run
if __name__ == "__main__":
    main()

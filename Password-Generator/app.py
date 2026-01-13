#  Password Generator

# Imports
import random
import string

# Function


def generate_pass(length, use_low, use_upper, use_digits, use_symobols):
    characters = ""

    if use_low:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symobols:
        characters += string.punctuation

    if not characters:
        print("❌ You must select at least one character type.")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    return password


# main
def main():

    print("🔐 Password Generator")

    # ask for length
    length = int(input("Enter Password Length: "))

    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_pass(
        length, use_lower, use_upper, use_digits, use_symbols)

    if password:
        print("\n🎉 Your generated password:")
        print(password)


# run
if __name__ == "__main__":
    main()

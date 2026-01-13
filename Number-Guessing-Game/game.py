# Number Guessing Game

# Imports
import random

# Functions
# ---------------------------------------


def guess(user_guess, secret):

    if user_guess == secret:
        print(f"🎉 You Guessed the Number Correct: {user_guess}")
        return True

    elif user_guess > secret:
        print("🔝 Too High....")
    else:
        print("⏬ Too Low....")

    return False


# Main Function
# ----------------------------
def main():

    secret = random.randint(1, 100)
    attempts = 0

    while True:

        print("-"*50)
        user_input = input("\nGuess the Number (1-100): ")

        if user_input.strip() == "":
            print("please Enter a Number.")
            continue

        try:
            user_guess = int(user_input)
        except ValueError:
            print("❌ Invalid input. Enter a number only.")
            continue

        attempts += 1

        if guess(user_guess, secret):
            print(f"🏁 You guessed it in {attempts} attempts.")
            break


# Run
if __name__ == "__main__":
    main()

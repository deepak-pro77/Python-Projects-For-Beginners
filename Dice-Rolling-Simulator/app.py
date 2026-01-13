# Rolling Dice Simulator

# Imports
import random

# Function


def roll_dice():
    return random.randint(1, 6)


def main():
    print("🎲 Rolling Dice Simulator")

    while True:

        user = input(
            "\n Press ENTER to roll the dice or type 'exit' to quit: ").lower()

        if user == "exit":
            print('👋 GoodBye')
            break

        dice1 = roll_dice()
        dice2 = roll_dice()

        print(f"🎯 You Rolled: {dice1} and {dice2}")

        if dice1 == dice2:
            print("🔥 Wow! You rolled a double!")


# Run
if __name__ == "__main__":
    main()

# Simple Calculator

# Calculations Function
# ------------------------------------------
def calculate(num1, num2, operation):

    if operation == "+":
        result = print(f'{num1} + {num2} = {num1+num2}')
        return result

    if operation == "-":
        result = print(f'{num1} - {num2} = {num1-num2}')
        return result

    if operation == "*":
        result = print(f'{num1} x {num2} = {num1*num2}')
        return result

    if operation == "/":
        result = print(f'{num1} / {num2} = {num1//num2}')
        return result


# main function
# ------------------------------------
def main():

    print("\n")
    print(" 🧮 Simple Calculator")

    print("-"*50)

    while True:

        num1 = input("\nEnter num1: ")
        num2 = input("\nEnter num2: ")
        operation = input("\nEnter your operation (+ - * /): ")

        if num1.strip() and num2.strip() == "":
            print("Please Enter a number: ")
            continue

        try:
            num_1 = int(num1)
            num_2 = int(num2)
            print('-'*50)
            calculate(num_1, num_2, operation)
        except ValueError:
            print("❌ Invalid input. Enter a number only.")
            continue

        ask = input("Do you want to continue (Yes/No)? ").lower()

        if ask == "no":
            print("👋 Goodbye")
            break


# Run
if __name__ == "__main__":
    main()

# 🌡Temperature Converter

# -------------------------------------------------------
def c_to_f(c):

    f = (c * 9/5) + 32
    print(f"🌡️ {c}°C = {round(f, 2)}°F")


def f_to_c(f):

    c = (f - 32) * 5/9
    print(f"🌡️ {c}°C = {round(f, 2)}°F")


def c_to_k(c):

    k = c + 273.15
    print(f"🌡️ {c}°C = {round(k, 2)}K")


def k_to_c(k):

    c = k - 273.15
    print(f"🌡️ {c}°C = {round(k, 2)}K")


# main
def main():

    while True:

        print('------- Temperature Converter ------')

        print("1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        print("3. Celsius → Kelvin")
        print("4. Kelvin → Cesius")
        print("5. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            c = float(input("Celsius: "))
            c_to_f(c)

        elif choice == "2":
            f = float(input("Enter Fahrenheit: "))
            f_to_c(f)

        elif choice == "3":
            c = float(input("Enter Celsius: "))
            c_to_k(c)

        elif choice == "4":
            k = float(input("Enter Kelvin: "))
            k_to_c(k)

        elif choice == "5":
            print("👋 GoodBye")
            break

        else:
            print("❌ Invalid Choice")


# Run
if __name__ == "__main__":
    main()

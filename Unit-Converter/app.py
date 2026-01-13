# Unit Converter

# ---------------- Conversion Functions ----------------

def kg_to_lb(kg):
    lb = kg * 2.20462
    print(f"✅ {kg} kg = {round(lb, 3)} lb")


def lb_to_kg(lb):
    kg = lb / 2.20462
    print(f"✅ {lb} lb = {round(kg, 3)} kg")


def km_to_miles(km):
    miles = km * 0.621371
    print(f"✅ {km} km = {round(miles, 3)} miles")


def miles_to_km(miles):
    km = miles * 1.60934
    print(f"✅ {miles} miles = {round(km, 3)} km")


# ---------------- Main Program ----------------

def main():

    while True:

        print("\n---------- Unit Converter -----------")
        print("1. Kg → Lb")
        print("2. Lb → Kg")
        print("3. Km → Miles")
        print("4. Miles → Km")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            kg = float(input("Enter kilograms: "))
            kg_to_lb(kg)

        elif choice == "2":
            lb = float(input("Enter pounds: "))
            lb_to_kg(lb)

        elif choice == "3":
            km = float(input("Enter kilometers: "))
            km_to_miles(km)

        elif choice == "4":
            miles = float(input("Enter miles: "))
            miles_to_km(miles)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid Choice, try again.")


if __name__ == "__main__":
    main()

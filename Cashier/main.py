#############################################################
import random

counters = [1, 2, 3, 4, 5]
counter = random.choice(counters)

# SUPERMARKET INVENTORY
product_prices_pkr = {

    # Fruits (per kg unless noted)
    "Apple": 350,
    "Banana": 180,
    "Orange": 250,
    "Mango": 400,
    "Grapes": 500,
    "Pineapple": 450,
    "Strawberry": 700,
    "Watermelon": 120,
    "Papaya": 220,
    "Guava": 200,
    "Pear": 450,
    "Peach": 380,
    "Plum": 420,

    # Vegetables (per kg)
    "Potato": 80,
    "Onion": 100,
    "Tomato": 120,
    "Carrot": 90,
    "Cabbage": 110,
    "Cauliflower": 130,
    "Spinach": 60,
    "Broccoli": 300,
    "Capsicum": 250,
    "Cucumber": 90,
    "Eggplant": 120,
    "Garlic": 600,
    "Ginger": 500,

    # Dairy
    "Milk": 220,          # per liter
    "Butter": 650,        # 200g
    "Cheese": 850,        # 200g
    "Yogurt": 180,        # 500g
    "Cream": 300,
    "Ice Cream": 450,

    # Bakery
    "Bread": 160,
    "Buns": 120,
    "Cake": 900,
    "Cookies": 250,
    "Biscuits": 180,
    "Donuts": 300,

    # Grains & Staples
    "Rice": 300,
    "Wheat Flour": 160,
    "Sugar": 150,
    "Salt": 60,
    "Lentils": 320,
    "Chickpeas": 280,
    "Beans": 350,
    "Oats": 420,
    "Pasta": 280,
    "Noodles": 120,

    # Meat & Eggs
    "Chicken": 620,       # per kg
    "Beef": 950,
    "Mutton": 2200,
    "Fish": 700,
    "Eggs": 360,          # dozen
    "Sausages": 650,

    # Snacks
    "Chips": 100,
    "Popcorn": 120,
    "Crackers": 180,
    "Nachos": 250,
    "Chocolate": 200,
    "Candy": 80,

    # Beverages
    "Tea": 1200,          # 500g
    "Coffee": 900,
    "Juice": 180,
    "Soft Drink": 150,
    "Mineral Water": 80,
    "Energy Drink": 320,

    # Frozen Foods
    "Frozen Peas": 300,
    "Frozen Corn": 280,
    "Frozen Chicken Nuggets": 650,
    "Frozen Fries": 420,

    # Household Items
    "Dish Soap": 180,
    "Laundry Detergent": 450,
    "Toilet Cleaner": 220,
    "Tissues": 160,
    "Paper Towels": 240,
    "Garbage Bags": 200,

    # Personal Care
    "Shampoo": 450,
    "Conditioner": 480,
    "Soap": 120,
    "Toothpaste": 220,
    "Toothbrush": 150,
    "Hand Wash": 260,
    "Body Lotion": 520,

    # Spices & Condiments
    "Black Pepper": 900,
    "Red Chili Powder": 420,
    "Turmeric": 300,
    "Cumin": 520,
    "Ketchup": 260,
    "Mayonnaise": 320,
    "Soy Sauce": 280,
    "Vinegar": 180
}


# User Cart
cart = {}


def save_bill(cart, subtotal, discount, final_total):
    filename = f"bill_counter_{counter}.txt"

    with open(filename, "a") as file:
        file.write("\n------ RECEIPT ------\n")
        for item, qty in cart.items():
            price = product_prices_pkr[item]
            file.write(f"{item} x{qty} = PKR {price * qty}\n")

        file.write("---------------------\n")
        file.write(f"Subtotal : PKR {subtotal}\n")
        file.write(f"Discount : PKR {discount}\n")
        file.write(f"Total    : PKR {final_total}\n")
        file.write("---------------------\n")


def do_shop():

    print("#### Enjoy ####")
    print("\n'Type Stop to End'")

    cart.clear()

    while True:

        item = input("\n🛒 Item: ").capitalize()

        if item == "Stop":
            print("\nTHANK YOU 💚")

            subtotal = sum(product_prices_pkr[i] * q for i, q in cart.items())

            discount = 0
            if subtotal >= 2000:
                discount = int(subtotal * 0.05)

            final_total = subtotal - discount

            print_receipt(cart, subtotal, discount, final_total)
            save_bill(cart, subtotal, discount, final_total)
            break

        if item not in product_prices_pkr:
            print("❌ Item Not Found in SuperMarket")
            continue

        quantity = int(input("Quantity: "))

        cart[item] = cart.get(item, 0) + quantity

        total_price = product_prices_pkr[item] * quantity
        print(f"👓 Scanning: {item} x{quantity} = PKR {total_price}")


def print_receipt(cart, subtotal, discount, final_total):
    print("\n🧾 -------- RECEIPT --------")
    for item, qty in cart.items():
        price = product_prices_pkr[item]
        print(f"{item:15} x{qty:<3} = PKR {price * qty}")

    print("-" * 30)
    print(f"Subtotal        : PKR {subtotal}")
    print(f"Discount        : PKR {discount}")
    print(f"Grand Total     : PKR {final_total}")
    print("🧾 --------------------------")


def main():

    print("########################################")
    print('WELCOME TO THE SUPERMARKET')
    print("\nDEEPAK SUPERMARKET")

    print('-'*50)

    do_shop()


# Run
if __name__ == "__main__":
    main()

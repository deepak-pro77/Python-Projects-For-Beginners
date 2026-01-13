##############################################################
import random

# Just for Fun - Using Counter for cashier
counters = [1, 2, 3, 4, 5]
counter = random.choice(counters)


# total products in super market

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

# User items bought
cart = {}   # item -> quantity


def pick_items():
    print("#### Enjoy ####")
    print("\n'Type Stop to End'")

    cart.clear()   # reset cart for new customer

    while True:
        item = input("\n🛒Item: ").capitalize()

        if item == "Stop":
            print("\nTHANK YOU 💚")
            grand_total = sum(
                product_prices_pkr[i] * q for i, q in cart.items())
            print(f"\nGrand Total = PKR {grand_total}")
            break

        if item not in product_prices_pkr:
            print("❌ Item not found in supermarket")
            continue

        quantity = int(input("Quantity: "))

        cart[item] = cart.get(item, 0) + quantity

        total_price = product_prices_pkr[item] * quantity
        print(f"👓 Scanning: {item} x{quantity} = PKR {total_price}")


def main():

    print("----------------DEEPAK SUPERMARKET----------------")

    while True:

        print("#"*50)
        print(f"\n###Counter No: ({counter})###")
        print("\n🛒Welcome To the Counter")

        pick_items()


# run
if __name__ == "__main__":
    main()

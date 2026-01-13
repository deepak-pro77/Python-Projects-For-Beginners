import requests

API_KEY = "e535f4f0a8065af41b3ead28"   # remove space
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

VALID_CURRENCIES = ["USD", "EUR", "CAD", "AUD", "PKR", "INR"]


def convert_currency():
    amount = float(input("Amount: "))
    from_currency = input("From (e.g., USD): ").upper()
    to_currency = input("To (e.g., PKR): ").upper()

    if from_currency not in VALID_CURRENCIES or to_currency not in VALID_CURRENCIES:
        print("Invalid currency code")
        return

    url = f"{BASE_URL}/latest/{from_currency}"

    response = requests.get(url)
    data = response.json()

    if data["result"] != "success":
        print("API error:", data.get("error-type"))
        return

    rate = data["conversion_rates"][to_currency]
    converted = amount * rate

    print(f"{amount} {from_currency} = {converted} {to_currency}")


convert_currency()

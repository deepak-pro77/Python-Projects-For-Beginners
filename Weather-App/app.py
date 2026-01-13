# ---------------------------------------
import requests


API_KEY = "YOURAPIKEY"


while True:

    city = input("City: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 401:
        print("❌ Invalid API key — verify email or regenerate key.")
        break

    if data.get("cod") == "404":
        print("❌ City not found")
        continue

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"\n🌦 Weather in {city}")
    print(f"🌡 Temperature: {temp}°C")
    print(f"📝 Condition: {desc}")
    print(f"💧 Humidity: {humidity}%\n")


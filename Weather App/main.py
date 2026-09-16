import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter city name: ").strip()

if not city:
    print("City name cannot be empty.")
    exit()

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 404:
    print("City not found. Please check the city name and try again.")
    exit()

if response.status_code != 200:
    print("Something went wrong. Please try again.")
    exit()

data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]

print("City:", city)
print("Temperature:", temperature, "°C")
print("Feels like:", feels_like, "°C")
print("Humidity:", humidity, "%")
print("Wind speed:", wind_speed, "m/s")
print("Condition:", description)

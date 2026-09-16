import os
from datetime import datetime
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

try:
    response = requests.get(url, params=params, timeout=10)
except requests.exceptions.RequestException:
    print("Unable to connect to the weather service.")
    exit()

if response.status_code == 404:
    print("City not found. Please check the city name and try again.")
    exit()

if response.status_code == 401:
    print("Invalid API key. Please check your .env file.")
    exit()

if response.status_code != 200:
    print("Something went wrong. Please try again.")
    exit()

data = response.json()

temperature = data["main"]["temp"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]
country = data["sys"]["country"]
pressure = data["main"]["pressure"]
sunrise = data["sys"]["sunrise"]
sunset = data["sys"]["sunset"]
wind_direction = data["wind"]["deg"]

sunrise_time = datetime.fromtimestamp(sunrise)
sunset_time = datetime.fromtimestamp(sunset)

print("City:", city, country)
print("Temperature:", temperature, "°C")
print("Minimum:", temp_min, "°C")
print("Maximum:", temp_max, "°C")
print("Feels like:", feels_like, "°C")
print("Humidity:", humidity, "%")
print("Wind speed:", wind_speed, "m/s")
print("Condition:", description)
print("Pressure:", pressure, "hPa")
print("Sunrise:", sunrise_time.strftime("%H:%M"))
print("Sunset:", sunset_time.strftime("%H:%M"))
print("Wind direction:", wind_direction, "°")
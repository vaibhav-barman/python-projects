import os
import requests
from dotenv import load_dotenv
from collections import Counter

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def make_request(url, city):

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

    except requests.exceptions.RequestException:
        return None, "Unable to connect to the weather service."

    if response.status_code == 404:
        return None, "City not found. Please check the city name and try again."

    if response.status_code == 401:
        return None, "Invalid API key. Please check your .env file."

    if response.status_code != 200:
        return None, "Something went wrong. Please try again."

    return response.json(), None

def get_weather(city):
    return make_request(BASE_URL, city)


def get_forecast(city):
    return make_request(FORECAST_URL, city)

def process_forecast(data):

    daily_forecast = {}

    for entry in data["list"]:

        date = entry["dt_txt"].split(" ")[0]

        temperature = entry["main"]["temp"]

        description = entry["weather"][0]["description"]

        icon = entry["weather"][0]["icon"]
        rain_probability = entry.get("pop", 0)
        
        if date not in daily_forecast:

            daily_forecast[date] = {
                "temperatures": [],
                "descriptions": [],
                "icons": [],
                "rain_probability": []
            }

        daily_forecast[date]["temperatures"].append(temperature)

        daily_forecast[date]["descriptions"].append(description)

        daily_forecast[date]["icons"].append(icon)
        daily_forecast[date]["rain_probability"].append(rain_probability)

    for date, forecast in daily_forecast.items():

        most_common_description = Counter(
            forecast["descriptions"]
        ).most_common(1)[0][0]

        most_common_icon = Counter(
            forecast["icons"]
        ).most_common(1)[0][0]

        forecast["description"] = most_common_description
        forecast["icon"] = most_common_icon

        forecast["minimum"] = min(forecast["temperatures"])
        forecast["maximum"] = max(forecast["temperatures"])
        forecast["rain_probability"] = sum(
            forecast["rain_probability"]
        ) / len(forecast["rain_probability"])

    return dict(list(daily_forecast.items())[1:6])
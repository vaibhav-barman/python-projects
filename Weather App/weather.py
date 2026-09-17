import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

    except requests.exceptions.RequestException:
        return None, "Unable to connect to the weather service."

    if response.status_code == 404:
        return None, "City not found. Please check the city name and try again."

    if response.status_code == 401:
        return None, "Invalid API key. Please check your .env file."

    if response.status_code != 200:
        return None, "Something went wrong. Please try again."

    return response.json(), None
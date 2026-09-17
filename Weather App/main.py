from weather import get_weather
from display import display_weather


city = input("Enter city name: ").strip()

if not city:
    print("City name cannot be empty.")
    exit()


data, error = get_weather(city)


if error:
    print(error)
    exit()


display_weather(data, city)
from weather import get_weather, get_forecast, process_forecast

from display import display_weather, display_forecast


city = input("Enter city name: ").strip()

if not city:

    print("City name cannot be empty.")

    exit()


data, error = get_weather(city)


if error:

    print(error)

    exit()


display_weather(data, city)


forecast_data, error = get_forecast(city)


if error:

    print(error)

    exit()


daily_forecast = process_forecast(forecast_data)

display_forecast(daily_forecast)
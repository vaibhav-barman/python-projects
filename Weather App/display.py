from datetime import datetime

def get_wind_direction(degrees):

    directions = [
        "N",
        "NE",
        "E",
        "SE",
        "S",
        "SW",
        "W",
        "NW"
    ]

    index = round(degrees / 45) % 8

    return directions[index]

def get_weather_icon(icon_code):

    icons = {
        "01d": "☀️",
        "01n": "🌙",
        "02d": "🌤️",
        "02n": "☁️",
        "03d": "☁️",
        "03n": "☁️",
        "04d": "☁️",
        "04n": "☁️",
        "09d": "🌧️",
        "09n": "🌧️",
        "10d": "🌦️",
        "10n": "🌧️",
        "11d": "⛈️",
        "11n": "⛈️",
        "13d": "❄️",
        "13n": "❄️",
        "50d": "🌫️",
        "50n": "🌫️"
    }

    return icons.get(icon_code, "🌡️")

def display_weather(data, city):

    temperature = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    feels_like = data["main"]["feels_like"]

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    wind_speed = data["wind"]["speed"]
    wind_degrees = data["wind"]["deg"]
    wind_direction = get_wind_direction(wind_degrees)

    description = data["weather"][0]["description"]

    icon_code = data["weather"][0]["icon"]
    weather_icon = get_weather_icon(icon_code)

    country = data["sys"]["country"]

    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]

    sunrise_time = datetime.fromtimestamp(sunrise)
    sunset_time = datetime.fromtimestamp(sunset)

    print()
    print("=" * 40)
    print(f"Weather for {city}, {country}")
    print("=" * 40)

    print(f"Temperature : {temperature} °C")
    print(f"Minimum     : {temp_min} °C")
    print(f"Maximum     : {temp_max} °C")
    print(f"Feels like  : {feels_like} °C")
    print(f"Condition   : {weather_icon} {description.title()}")

    print(f"Humidity    : {humidity}%")
    print(f"Pressure    : {pressure} hPa")

    print(f"Wind speed  : {wind_speed} m/s")
    print(f"Wind dir.   : {wind_direction} ({wind_degrees}°)")

    print(f"Sunrise     : {sunrise_time.strftime('%H:%M')}")
    print(f"Sunset      : {sunset_time.strftime('%H:%M')}")

    print("=" * 40)

def display_forecast(daily_forecast):

    print()
    print("=" * 40)
    print("5-DAY FORECAST")
    print("=" * 40)

    for date, forecast in daily_forecast.items():

        date_object = datetime.strptime(date, "%Y-%m-%d")

        formatted_date = date_object.strftime("%A, %d %B")

        minimum = forecast["minimum"]
        maximum = forecast["maximum"]

        description = forecast["description"]
        icon = get_weather_icon(forecast["icon"])

        print()
        print(formatted_date)
        print(f"{icon} {description.title()}")
        print(f"Temperature: {minimum:.1f}°C - {maximum:.1f}°C")

    print()
    print("=" * 40)
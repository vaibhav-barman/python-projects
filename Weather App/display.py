from datetime import datetime


def display_weather(data, city):

    temperature = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    feels_like = data["main"]["feels_like"]

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    wind_speed = data["wind"]["speed"]
    wind_direction = data["wind"]["deg"]

    description = data["weather"][0]["description"]

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
    print(f"Condition   : {description}")

    print(f"Humidity    : {humidity}%")
    print(f"Pressure    : {pressure} hPa")

    print(f"Wind speed  : {wind_speed} m/s")
    print(f"Wind dir.   : {wind_direction}°")

    print(f"Sunrise     : {sunrise_time.strftime('%H:%M')}")
    print(f"Sunset      : {sunset_time.strftime('%H:%M')}")

    print("=" * 40)
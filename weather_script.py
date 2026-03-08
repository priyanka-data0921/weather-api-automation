import requests
import schedule
import time
from plyer import notification
from datetime import datetime

API_KEY = "YOUR_API_KEY"
city = "London"

def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        message = f"Temp: {temp}°C | Weather: {weather} | Humidity: {humidity}%"

        print("\nWeather Update")
        print("Time:", datetime.now())
        print(message)

        notification.notify(
            title="Weather Update",
            message=message,
            timeout=10
        )

    else:
        print("API error:", data)

schedule.every(1).minutes.do(get_weather)

print("Weather scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)
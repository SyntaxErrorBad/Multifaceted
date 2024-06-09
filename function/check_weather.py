import os
from dotenv import load_dotenv
import requests
from ai_voice import speak

load_dotenv("data/.env")


def get_weather(city_name):
    api_key = os.getenv("API_WEATHER")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = float(main['temp']) - 273.15
        humidity = main['humidity']

        speak(f"Температура сьогодні {temperature}°C, а вологість {humidity}%")


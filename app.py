import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
user_input = input("enter city:")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)

if weather_data.status_code != 200:
    print("Error:", weather_data.json().get("message"))
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    x = round((temp - 32) * (5/9))

    print(f"the weather in {user_input} is: {weather}")
    print(f"the temperature in {user_input} is: {temp} fahrenheit or {x} celsius")
import requests

import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
user_input= input("enter city:")

weather_data= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(api_key)
print(weather_data.status_code, weather_data.json())

weather=weather_data.json()['weather'][0]['main']
temp=round(weather_data.json()['main']['temp'])

print(f"the weather in {user_input} is: {weather}")
x=round((temp-32)*(5/9))
print(f"the temperature in {user_input} is: {temp} farenheit or {x} celcius")

from decimal import Rounded
import requests

API_KEY = "4c516165eddb10e27acacd275164f49c" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter the city you want to know ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(f"weather: {weather}\ntemperature: {temperature} celsius")
else:
    print("an error accure")
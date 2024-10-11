import requests
from pprint import pprint

APIkey = 'da4aec418d6cc4b190dbbd283eda39f0'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+APIkey+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
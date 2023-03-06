import requests
import os
from datetime import datetime

user_api = os.environ['weatherAppKey']
location = input("Enter the city name: ")

# Make an api request by creating a complete link

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

# print(api_data)

if api_data['cod'] == '404':
    print("Invalid city: {}, Please check your city name".format(location))
else:
    # create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M: %S %p")

    Print("------------------------------")
    print(" Weather Stats for - {} || {}".format(location.upper(), date_time))
    Print("------------------------------")

    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather desc  :", weather_desc)
    print("Current humidity      :", hmdt, '%')
    print("Current wind speed    :", wind_spd, 'kmph')

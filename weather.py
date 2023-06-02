import requests
import os
from datetime import datetime
import argparse
import sys
def weather_report(args):
    complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q=' + str(args.o) + '&appid=' + "ff94743a8c7fba48f37b89783e263ee4"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    # create variables to store and display data
    if 'main' in api_data and 'temp' in api_data['main']:
        temp_city = ((api_data['main']['temp']) - 273.15)
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print("Current temperature is: ",(temp_city))
        print("Current weather desc  :", weather_desc)
        print("Current Humidity      :", hmdt, '%')
        print("Current wind speed    :", wind_spd, 'kmph')

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--o', type=str, help='please the correct city name')
    args=parser.parse_args()
    weather_report(args)
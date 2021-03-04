"""
Code for the weather integration with OpenWeatherMap
Input: lattitude, longitude, units (optional, default is metric) 
Output: temperature for given coordinates

"""


import requests
import os
from dotenv import load_dotenv
load_dotenv()

_weather_api = os.getenv("OPENWEATHER_API")

def get_weather_for_latlon(lat, lon, units="metric"):
    """
    Based on lat/lon returns temperature for given coordinates
    """
    # latlon for Viqtor Davis HQ below
    # lat = "52.097147"
    # lon = "5.065070"
    # units = "metric"
    exclude = "minutely,hourly,daily"

    response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&units={units}&appid={_weather_api}')

    weather_data = response.json()

    return weather_data['current']['temp']


print(get_weather_for_latlon("52.097147","5.065070"))
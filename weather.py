import requests

from config import Config
import cache

import json
from datetime import time

def get_city_weather(city_name, start_date=None, end_date=None):



    cached_data = cache.get_cached_city_weather(city_name)

    if cached_data is not None:
        return json.loads(cached_data)

    if start_date and end_date:
        url = f'{Config.WEATHER_BASE_URL}{city_name}/{start_date}/{end_date}?key={Config.WEATHER_API_KEY}'

    elif start_date and not end_date:
        url = f'{Config.WEATHER_BASE_URL}{city_name}/{start_date}?key={Config.WEATHER_API_KEY}'

    elif not start_date and not end_date:
        url = f'{Config.WEATHER_BASE_URL}{city_name}?key={Config.WEATHER_API_KEY}'

    try:
        response = requests.get(url)
        weather_data = response.json()

        # print(weather_data)

        cache.set_cached_city_weather(city_name, json.dumps(weather_data))
        print("HERE22")
    except Exception as e:
        print(f"failed API response: {e}")
        weather_data = None    

    return weather_data

    
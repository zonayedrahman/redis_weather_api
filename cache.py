import redis

from config import Config

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def set_cached_city_weather(city_name, weather_payload):
    r.set(city_name, weather_payload, ex=Config.CACHE_EXPIRATION)

def get_cached_city_weather(city_name):

    cached = r.get(city_name)

    if cached:
        print('CACHE HIT')
        return cached
    
    else:
        return None


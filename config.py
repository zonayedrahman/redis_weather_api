from dotenv import load_dotenv, dotenv_values 

import os



load_dotenv() 


class Config:

    WEATHER_BASE_URL=os.getenv("BASE_URL")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    
    CACHE_EXPIRATION = 7200
    RATE_LIMIT=100
from celery import shared_task
import requests
from .models import Weather

API_KEY = "c92f72b9b2b525803e5451eb76ecb95e"

@shared_task
def update_weather_data(city):
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    geo_res = requests.get(geocode_url).json()
    if not geo_res:
        return None
    
    lat, lon = geo_res[0]["lat"], geo_res[0]["lon"]
    print(lat, lon)
    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric"
    weather_res = requests.get(weather_url).json()

    data_res = {
        "city": city,
        "temperature": weather_res["current"]["temp"],
        "humidity": weather_res["current"]["humidity"],
        "wind_speed": weather_res["current"]["wind_speed"],
        "weather_condition": weather_res["current"]["weather"][0]["description"],
    }
    
    weather = Weather.objects.filter(city__iexact=city).first()
    
    if weather:
        weather.temperature = data_res['temperature']
        weather.humidity = data_res["humidity"]
        weather.wind_speed = data_res["wind_speed"]
        weather.weather_condition = data_res["weather_condition"]
        weather.save()
    
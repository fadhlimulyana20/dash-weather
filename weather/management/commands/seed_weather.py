import requests
from django.core.management.base import BaseCommand
from weather.models import Weather
from django.utils.timezone import now

from weather.views import get_weather_data

# OpenWeatherMap API Configuration
API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

# List of 10 major cities in Indonesia with lat/lon
CITIES = [
    "Jakarta",
    "Bandung",
]

class Command(BaseCommand):
    help = "Seed weather data for major cities in Indonesia"

    def handle(self, *args, **kwargs):
        for city in CITIES:
            data = get_weather_data(city)
            if data:
                weather = Weather.objects.filter(city__iexact=city).first()
                if weather:
                    weather.temperature = data['temperature']
                    weather.humidity = data["humidity"]
                    weather.wind_speed = data["wind_speed"]
                    weather.weather_condition = data["weather_condition"]
                    weather.save()
                else:
                    Weather.objects.create(**data)

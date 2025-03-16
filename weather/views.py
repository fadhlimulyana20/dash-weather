import requests
from django.shortcuts import render
from .models import Weather
from django.contrib.auth.decorators import login_required

API_KEY = "c92f72b9b2b525803e5451eb76ecb95e"

def get_weather_data(city):
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    geo_res = requests.get(geocode_url).json()
    if not geo_res:
        return None
    
    lat, lon = geo_res[0]["lat"], geo_res[0]["lon"]
    print(lat, lon)
    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric"
    weather_res = requests.get(weather_url).json()

    return {
        "city": city,
        "temperature": weather_res["current"]["temp"],
        "humidity": weather_res["current"]["humidity"],
        "wind_speed": weather_res["current"]["wind_speed"],
        "weather_condition": weather_res["current"]["weather"][0]["description"],
    }

@login_required
def fetch_and_store_weather(request):
    if request.method == "POST":
        city = request.POST.get("city")
        data = get_weather_data(city)
        if data:
            Weather.objects.create(**data)

    weather_data = Weather.objects.all().order_by("-timestamp")
    return render(request, "weather/dashboard.html", {"weather_data": weather_data})

from django.urls import path
from .views import fetch_and_store_weather, update_weather

urlpatterns = [
    path("", fetch_and_store_weather, name="dashboard"),
    path("update-weather/", update_weather, name="update_weather"),
]

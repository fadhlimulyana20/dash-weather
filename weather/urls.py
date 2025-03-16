from django.urls import path
from .views import fetch_and_store_weather

urlpatterns = [
    path("", fetch_and_store_weather, name="dashboard"),
]

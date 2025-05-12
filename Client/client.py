import requests
import os
from datetime import datetime

LAT = os.getenv("LAT", "52.23")
LON = os.getenv("LON", "21.01")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000/readings")

def fetch_weather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly=temperature_2m,surface_pressure&timezone=auto"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def fetch_air_quality():
    url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={LAT}&longitude={LON}&hourly=pm10,pm2_5&timezone=auto"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def build_reading(weather_data, air_data, index=0):
    return {
        "timestamp": weather_data["hourly"]["time"][index],
        "temperature_c": weather_data["hourly"]["temperature_2m"][index],
        "pressure_hp": weather_data["hourly"]["surface_pressure"][index],
        "pm10": air_data["hourly"]["pm10"][index],
        "pm2_5": air_data["hourly"]["pm2_5"][index]
    }
def send_to_backend(reading):
    r = requests.post(BACKEND_URL, json=reading)
    print("Send to backend:", r.status_code, r.text)

if __name__ == "__main__":
    weather = fetch_weather()
    air = fetch_air_quality()
    reading = build_reading(weather, air)
    send_to_backend(reading)

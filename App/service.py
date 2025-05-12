from datetime import datetime
from .models import AirQualityReading
from .storage import readings

def validate(data: dict) -> AirQualityReading:
    ts = datetime.fromisoformat(data['timestamp'])

    temp = float(data['temperature_c'])
    if not -50 <= temp <= 60:
        raise ValueError("Temperature out of realistic range")

    pressure = float(data['pressure_hp'])
    if not 800 <= pressure <= 1200:
        raise ValueError("Pressure out of realistic range")

    pm10 = float(data['pm10'])
    if pm10 < 0:
        raise ValueError("PM10 cannot be negative")

    return AirQualityReading(
        timestamp=ts,
        temperature=temp,
        presure_hpa=pressure,
        pm10=pm10,
        pm2_5=float(data['pm2_5'])
    )

def store_reading(reading: AirQualityReading) -> None:
    readings.append(reading)

def find_closest_reading(target_ts: datetime) -> AirQualityReading:
    return min(readings, key=lambda r: abs(r.timestamp - target_ts))
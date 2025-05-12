from datetime import datetime
from dataclasses import dataclass

@dataclass
class AirQualityReading:
    timestamp: datetime
    temperature: float
    presure_hpa: float
    pm10: float
    pm2_5: float

# ------------------ crud/weather.py ------------------
from sqlalchemy.orm import Session
from models import WeatherData
from datetime import datetime

# Insert or update weather data
def upsert_weather(db: Session, city: str, country: str, temperature: float):
    record = WeatherData(city=city, country=country, temperature_celsius=temperature, timestamp=datetime.utcnow())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

# Get latest weather data
def get_latest_weather(db: Session):
    return db.query(WeatherData).order_by(WeatherData.timestamp.desc()).limit(10).all()

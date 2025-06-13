# ------------------ models.py ------------------
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database.db import Base

class WeatherData(Base):
    __tablename__ = "weather_data"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50))
    country = Column(String(50))
    temperature_celsius = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

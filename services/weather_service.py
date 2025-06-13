# ------------------ scheduler/fetch_weather.py ------------------
import requests
import os
from dotenv import load_dotenv
from database.db import SessionLocal
from crud.weather import upsert_weather

# Load environment variables from .env file
load_dotenv()

# Fetch the API key securely from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

# List of cities and their countries
cities = [
    ("Mumbai", "India"),
    ("Delhi", "India"),
    ("California", "USA"),
    ("Sao Paulo", "Brazil"),
    ("Johannesburg", "South Africa"),
    ("Berlin", "Germany"),
    ("Madrid", "Spain"),
    ("Riyadh", "Saudi Arabia"),
    ("Dubai", "UAE"),
    ("Muscat", "Oman")
]

def fetch_and_store():
    db = SessionLocal()
    try:
        for city, country in cities:
            response = requests.get(API_URL.format(city=city, key=API_KEY))
            if response.status_code == 200:
                temp = response.json()['main']['temp']
                upsert_weather(db, city, country, temp)
    finally:
        db.close()

# You can use APScheduler or a cron job to call fetch_and_store() every minute
# ...existing code...

if __name__ == "__main__":
    fetch_and_store()
# ...existing code...s
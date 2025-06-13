# ------------------ main.py ------------------
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.db import SessionLocal, engine
import models
from crud import weather as weather_crud

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/weather/")
def read_weather(db: Session = Depends(get_db)):
    return weather_crud.get_latest_weather(db)

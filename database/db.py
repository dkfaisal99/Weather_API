import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load connection string
SQLALCHEMY_DATABASE_URL = os.getenv("MYSQL_DATABASE_URL")

# Check if the URL is None
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("MYSQL_DATABASE_URL not set in environment variables")

# Create engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
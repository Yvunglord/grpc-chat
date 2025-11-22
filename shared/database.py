from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import logging

from .config import settings

Base = declarative_base()

try:
    engine = create_engine(
        settings.DATABASE_URL,
        echo=True,
        pool_pre_ping=True,
        pool_recycle=300,
    )
    
    with engine.connect() as conn:
        logging.info("Database connection successful")
        
except Exception as e:
    logging.error(f"Database connection failed: {e}")
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=True,
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        logging.info("Database tables created successfully")
    except Exception as e:
        logging.error(f"Failed to create tables: {e}")
        raise

def init_db():
    create_tables()
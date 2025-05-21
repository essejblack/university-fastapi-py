from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import app.config.settings as settings
from app.models.init import Base
from sqlalchemy.orm import sessionmaker

global SessionLocal


def get_db_connection():
    global engine
    while True:
        try:
            engine = create_engine(f"postgresql+psycopg2://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:5432/{settings.DATABASE_NAME}")
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            Base.create_metadata(SessionLocal)
            print("Connection established")
            break
        except SQLAlchemyError as error:
            print("Error while connecting to PostgreSQL:", error)

        finally:
            # Dispose of the engine to close connections
            engine.dispose()
            print("Database connection closed.")
    return engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
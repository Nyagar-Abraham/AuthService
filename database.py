import os
from sqlmodel import create_engine, Session, SQLModel

from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Conditional connect_args (only for SQLite)
connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = Session(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

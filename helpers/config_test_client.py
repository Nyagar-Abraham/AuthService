from sqlalchemy import StaticPool
from starlette.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from main import app
from dependencies import get_session

engine = create_engine(
    "sqlite:///testing.db",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
SQLModel.metadata.create_all(engine)

def get_session_test():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = get_session_test
test_client = TestClient(app)
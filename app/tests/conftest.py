import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, close_all_sessions

from config import settings
from main import app


# DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(settings.DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    session = TestingSessionLocal()
    yield session
    session.close()
    close_all_sessions()


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def test_user(client):
    user_data = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "test_password",
    }
    client.post("users/signup", json=user_data)
    user_data.pop('email')
    access_token = client.post("auth/login", data=user_data).json()["access_token"]
    print(222, access_token)
    return user_data, access_token

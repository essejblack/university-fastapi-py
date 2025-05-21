import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from random import randint

from app.main import app
from app.database.db import get_db
from app.models.student import Student

@pytest.fixture(scope="module")
def override_get_db():
    mock_db = MagicMock()
    def fake_add(student_obj):
        student_obj.id = 123

    mock_db.add.side_effect = fake_add
    mock_db.commit.return_value = None
    mock_db.refresh.side_effect = lambda obj: None

    yield mock_db

@pytest.fixture(scope="module")
def client(override_get_db):
    app.dependency_overrides[get_db] = lambda: override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

def test_create_student_from_username(client):
    random = randint(1, 1000)
    first_name = f"John {random}"
    last_name = f"Doe {random}"
    response = client.post("/students/", json={"first_name": first_name, "last_name": last_name})
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == first_name
    assert data["last_name"] == last_name
    assert data["id"] is not None
from random import randint

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_app_running_status_return_ok(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "OK"
    assert data["status_code"] == 200


def test_create_student_from_username(client):
    random = randint(1, 1000)
    first_name = f"John {random}"
    last_name = f"Doe {random}"
    response = client.post("/students/", json={"first_name": first_name, "last_name": last_name})
    assert response.status_code == 201
    data = response.json()
    assert data["first_name"] == first_name
    assert data["last_name"] == last_name
    assert data["id"] is not None


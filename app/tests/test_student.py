import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from random import randint

from app.main import app
from app.models.student import Student
from app.database.db import get_db

@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def client(mock_db):
    app.dependency_overrides[get_db] = lambda: mock_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

def test_create_student(client, mock_db):
    random = randint(1, 1000)
    student_data = {"first_name": f"John {random}", "last_name": f"Doe {random}"}
    student_instance = Student(id=1, **student_data)

    mock_db.add.side_effect = lambda obj: setattr(obj, "id", 1)
    mock_db.refresh.side_effect = lambda obj: None
    mock_db.commit.return_value = None

    response = client.post("/students/", json=student_data)

    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == student_data["first_name"]
    assert data["last_name"] == student_data["last_name"]
    assert data["id"] == 1

def test_read_students(client, mock_db):
    students = [
        Student(id=1, first_name="Alice", last_name="Smith"),
        Student(id=2, first_name="Bob", last_name="Jones"),
    ]
    mock_query = MagicMock()
    mock_query.all.return_value = students
    mock_db.query.return_value = mock_query

    response = client.get("/students/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["first_name"] == "Alice"
    assert data[1]["last_name"] == "Jones"

def test_read_single_student_found(client, mock_db):
    student = Student(id=1, first_name="Test", last_name="Student")
    mock_query = MagicMock()
    mock_query.filter.return_value.first.return_value = student
    mock_db.query.return_value = mock_query

    response = client.get("/students/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["first_name"] == "Test"

def test_read_single_student_not_found(client, mock_db):
    mock_query = MagicMock()
    mock_query.filter.return_value.first.return_value = None
    mock_db.query.return_value = mock_query

    response = client.get("/students/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}

def test_delete_student_success(client, mock_db):
    student = Student(id=1, first_name="Test", last_name="Student")
    mock_query = MagicMock()
    mock_query.filter.return_value.first.return_value = student
    mock_db.query.return_value = mock_query

    response = client.delete("/students/1")

    assert response.status_code == 200
    assert response.json() == {"detail": "Student deleted successfully"}
    mock_db.delete.assert_called_once_with(student)
    mock_db.commit.assert_called_once()

def test_delete_student_not_found(client, mock_db):
    mock_query = MagicMock()
    mock_query.filter.return_value.first.return_value = None
    mock_db.query.return_value = mock_query

    response = client.delete("/students/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}

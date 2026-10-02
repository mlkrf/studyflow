from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSession = sessionmaker(bind=engine, autoflush=False)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

TASK = {"title": "Algorithms coursework", "course": "CS201", "due_date": "2026-11-01", "priority": 1}


def test_create_and_list():
    r = client.post("/tasks", json=TASK)
    assert r.status_code == 201
    assert r.json()["done"] is False
    assert any(t["title"] == TASK["title"] for t in client.get("/tasks").json())


def test_update_marks_done():
    task_id = client.post("/tasks", json=TASK).json()["id"]
    r = client.patch(f"/tasks/{task_id}", json={"done": True})
    assert r.json()["done"] is True


def test_delete_and_404():
    task_id = client.post("/tasks", json=TASK).json()["id"]
    assert client.delete(f"/tasks/{task_id}").status_code == 204
    assert client.patch(f"/tasks/{task_id}", json={"done": True}).status_code == 404


def test_validation_rejects_bad_priority():
    r = client.post("/tasks", json={**TASK, "priority": 9})
    assert r.status_code == 422

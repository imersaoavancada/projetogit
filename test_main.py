from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Funciona!"}


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": False}

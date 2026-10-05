from fastapi.testclient import TestClient

from pilume.main import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"
    assert response.json()["mode"] == "simulation"


def test_set_valid_light():
    command = {
        "brightness": 50,
        "red": 255,
        "green": 50,
        "blue": 0,
    }

    response = client.post("/api/light", json=command)
    result = response.json()

    assert response.status_code == 200
    assert result["power"] is True
    assert result["brightness"] == 50
    assert result["red"] == 255


def test_reject_invalid_brightness():
    command = {
        "brightness": 101,
        "red": 255,
        "green": 50,
        "blue": 0,
    }

    response = client.post("/api/light", json=command)

    assert response.status_code == 422


def test_reject_invalid_colour():
    command = {
        "brightness": 50,
        "red": 300,
        "green": 50,
        "blue": 0,
    }

    response = client.post("/api/light", json=command)

    assert response.status_code == 422


def test_switch_off():
    response = client.post("/api/light/off")
    result = response.json()

    assert response.status_code == 200
    assert result["power"] is False
    assert result["brightness"] == 0

import pytest
from fastapi.testclient import TestClient
from app import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def clean_state():
    main.items.clear()
    main.next_id = 1


def test_create_and_get_item():
    r = client.post("/api/items", json={"name": "Book"})
    assert r.status_code == 201
    item_id = r.json()["id"]
    r = client.get(f"/api/items/{item_id}")
    assert r.status_code == 200
    assert r.json()["name"] == "Book"


def test_get_missing_item_returns_404():
    assert client.get("/api/items/999").status_code == 404


def test_update_item():
    client.post("/api/items", json={"name": "Old"})
    r = client.put("/api/items/1", json={"name": "New"})
    assert r.status_code == 200
    assert r.json()["name"] == "New"


def test_delete_item():
    client.post("/api/items", json={"name": "X"})
    assert client.delete("/api/items/1").status_code == 204
    assert client.get("/api/items/1").status_code == 404

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Item 1", "price": 10.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Item 1"
    assert response.json()["price"] == 10.0
    assert "id" in response.json()

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert type(response.json()) == list

def test_read_item():
    response = client.post("/items/", json={"name": "Item 2", "price": 20.0})
    item_id = response.json()["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Item 2"

def test_update_item():
    response = client.post("/items/", json={"name": "Item 3", "price": 30.0})
    item_id = response.json()["id"]
    response = client.put(f"/items/{item_id}", json={"id": item_id, "name": "Updated Item 3", "price": 35.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item 3"
    assert response.json()["price"] == 35.0

def test_delete_item():
    response = client.post("/items/", json={"name": "Item 4", "price": 40.0})
    item_id = response.json()["id"]
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}

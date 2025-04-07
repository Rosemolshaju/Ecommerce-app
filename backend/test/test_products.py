from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product():
    new_product = {"name": "Test Product", "description": "Sample", "price": 25.99, "stock": 10}
    response = client.post("/products/", json=new_product)
    assert response.status_code == 200
    assert response.json()["message"] == "Product created successfully"

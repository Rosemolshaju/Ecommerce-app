def test_user_registration():
    response = client.post("/users/register", json={"username": "testuser", "email": "test@example.com", "password": "secure123"})
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

def test_user_login():
    response = client.post("/users/login", json={"username": "testuser", "password": "secure123"})
    assert response.status_code == 200
    assert "token" in response.json()

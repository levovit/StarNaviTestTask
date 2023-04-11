def test_create_user(client):
    user_data = {
        "username": "test_user_for_creating",
        "email": "test1@example.com",
        "password": "test1_password",
    }
    response = client.post("users/signup", json=user_data)
    assert response.status_code == 200

    created_user = response.json()
    assert created_user["username"] == user_data["username"]
    assert created_user["email"] == user_data["email"]


def test_login_user(client):
    user_data = {
        "username": "test_user_for_login",
        "email": "test2@example.com",
        "password": "test2_password",
    }
    client.post("users/signup", json=user_data)
    response = client.post("auth/login", data=user_data)

    assert response.status_code == 200
    assert "access_token" in response.json()

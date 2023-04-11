import pytest


def test_fetch_0_posts(client, test_user):
    user_data, access_token = test_user
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/posts/", headers=headers)

    assert response.status_code == 200
    assert len(response.json()) == 0


def test_create_post(client, test_user):
    user_data, access_token = test_user
    post_data = {
        "title": "Test Post",
        "content": "This is a test post.",
    }
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.post("/posts/", json=post_data, headers=headers)

    assert response.status_code == 200
    created_post = response.json()
    assert created_post["title"] == post_data["title"]
    assert created_post["content"] == post_data["content"]


def test_fetch_posts(client, test_user):
    user_data, access_token = test_user
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/posts/", headers=headers)

    assert response.status_code == 200
    assert len(response.json()) == 1

    post_data = {
        "title": "Test my second Post",
        "content": "This is a 2 test post.",
    }
    client.post("/posts/", json=post_data, headers=headers)

    response = client.get("/posts/", headers=headers)

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_like_not_existing_post(client, test_user):
    user_data, access_token = test_user
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 1000
    response = client.post(f"/posts/{post_id}/like", headers=headers)
    assert response.status_code == 404


def test_unlike_not_existing_post(client, test_user):
    user_data, access_token = test_user
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 1000
    response = client.post(f"/posts/{post_id}/unlike", headers=headers)
    assert response.status_code == 404


def test_like_post(client, test_user):
    user_data, access_token = test_user
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 1
    response = client.post(f"/posts/{post_id}/like", headers=headers)
    assert response.status_code == 200
    response = client.post(f"/posts/{post_id}/like", headers=headers)
    assert response.status_code == 400


def test_unlike_post(client, test_user):
    user_data, access_token = test_user
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 1
    response = client.post(f"/posts/{post_id}/unlike", headers=headers)
    assert response.status_code == 200
    response = client.post(f"/posts/{post_id}/unlike", headers=headers)
    assert response.status_code == 400


def test_like_unlike_post(client, test_user):
    user_data, access_token = test_user
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 1
    response = client.post(f"/posts/{post_id}/like", headers=headers)
    assert response.status_code == 200
    response = client.post(f"/posts/{post_id}/unlike", headers=headers)
    assert response.status_code == 200

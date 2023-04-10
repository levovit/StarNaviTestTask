import os
import uuid
import requests
from models import User, USERS


def create_user():
    username = f'bot_{uuid.uuid4()}'
    password = f'{uuid.uuid4()}'
    email = f'{uuid.uuid4()}@gmail.com'
    signup_url = f'{os.getenv("WEB_APP_URL")}/users/signup'
    signup_data = {
        "username": username,
        "email": email,
        "password": password
    }
    response = requests.post(signup_url, json=signup_data)
    if response.status_code == 200:
        user = User(username=username, password=password, email=email)
        login_user(user)


def login_user(user: User):
    login_url = f'{os.getenv("WEB_APP_URL")}/auth/login'

    login_data = {
        "username": user.username,
        "password": user.password
    }
    response = requests.post(login_url, data=login_data)
    if response.status_code == 200:
        user.access_token = response.json()['access_token']
        USERS[user.username] = user


def create_n_users(n: int) -> list[User]:
    USERS.clear()
    for _ in range(n):
        create_user()
    return USERS.values()

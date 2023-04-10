import os
import random
import string
import requests
from models import Post, User, POSTS, USERS


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def create_content():
    title = generate_random_string(10)
    content = generate_random_string(50)
    return title, content


def create_post(user: User) -> Post:
    title, content = create_content()

    create_post_url = f'{os.getenv("WEB_APP_URL")}/posts/'

    create_post_data = {
        'title': title,
        'content': content,
    }
    headers = {"Authorization": f"Bearer {user.access_token}"}
    response = requests.post(create_post_url, json=create_post_data, headers=headers)
    if response.status_code == 200:
        r_json = response.json()
        post = Post(title=r_json['title'], content=r_json['content'], post_id=r_json['id'])
        POSTS[post.post_id] = post
        return post


def create_n_post(user: User, posts_count: int) -> list[Post]:
    posts = []
    for _ in range(posts_count):
        post = create_post(user)
        posts.append(post)

    return posts


def create_up_to_n_posts_per_user(n: int) -> list[Post]:
    POSTS.clear()
    for user in USERS.values():
        posts = create_n_post(user, random.randint(1, n))
        user.posts = posts
    return POSTS.values()


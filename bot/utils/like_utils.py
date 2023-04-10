import os
import random
import requests
from models import POSTS, USERS, Post, User


def like_post(post_id: int, user: User) -> bool:
    like_post_url = f'{os.getenv("WEB_APP_URL")}/posts/{post_id}/like'

    headers = {"Authorization": f"Bearer {user.access_token}"}
    response = requests.post(like_post_url, headers=headers)
    if response.status_code == 200:
        POSTS[post_id].like_count += 1
        return True
    return False


def like_up_to_n_posts_per_user(up_to_n: int) -> int:
    posts = POSTS.values()
    total_likes = 0
    for user in USERS.values():
        n = random.randint(1, up_to_n)
        if len(posts) < n:
            sample_posts = posts
        else:
            sample_posts = random.sample(list(posts), n)
        for post in sample_posts:
            if like_post(post.post_id, user):
                total_likes += 1
    return total_likes

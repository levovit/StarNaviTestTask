from typing import Optional
from dataclasses import dataclass, field


@dataclass
class Post:
    post_id: int
    title: str
    content: str
    like_count: int = 0


@dataclass
class User:
    username: str
    email: str
    password: str
    access_token: Optional[str] = None
    posts: list[Post] = field(default_factory=list)


# No database is necessary, as the these dicts will suffice.
USERS: dict[str, User] = {}
POSTS: dict[int, Post] = {}

from typing import Optional
from dataclasses import dataclass


@dataclass
class User:
    username: str
    email: str
    password: str
    access_token: Optional[str] = None


USERS: dict[str, User] = {}  # No database is necessary, as the this dict will suffice.

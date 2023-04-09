from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    user_id: int
    created_at: datetime
    likes: int

    class Config:
        orm_mode = True

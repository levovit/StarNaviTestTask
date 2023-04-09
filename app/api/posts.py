from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import date
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.post import Post
from utils.auth_helpers import get_current_user
from utils.db import get_db
from schemas import post_scheme, user_scheme

router = APIRouter()


@router.post("/", response_model=post_scheme.Post)
async def create_post(post: post_scheme.PostCreate,
                      current_user: Annotated[user_scheme.User, Depends(get_current_user)],
                      db: Session = Depends(get_db)):
    new_post = Post(title=post.title, content=post.content, user_id=current_user)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/", response_model=list[post_scheme.Post])
async def get_all_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@router.post("/{post_id}/like", response_model=post_scheme.Post)
async def like_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    post.likes += 1
    db.commit()
    return post


@router.post("/{post_id}/unlike", response_model=post_scheme.Post)
async def unlike_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    if post.likes > 0:
        post.likes -= 1
        db.commit()

    return post


@router.get("/analytics")
async def get_analytics(date_from: date, date_to: date, db: Session = Depends(get_db)):
    analytics = (
        db.query(func.date(Post.created_at), func.count(Post.id))
        .filter(Post.created_at.between(date_from, date_to))
        .group_by(func.date(Post.created_at))
        .all()
    )
    return analytics

import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import date
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.post import Post, Like
from utils.auth_helpers import get_current_user
from utils.db import get_db
from schemas import post_scheme, user_scheme

router = APIRouter()


@router.post("/", response_model=post_scheme.Post)
async def create_post(post: post_scheme.PostCreate,
                      current_user: Annotated[user_scheme.User, Depends(get_current_user)],
                      db: Annotated[Session, Depends(get_db)]):
    new_post = Post(title=post.title, content=post.content, user_id=current_user)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/", response_model=list[post_scheme.Post])
async def get_all_posts(current_user: Annotated[user_scheme.User, Depends(get_current_user)],
                        db: Annotated[Session, Depends(get_db)]):
    return db.query(Post).all()


@router.post("/{post_id}/like", response_model=post_scheme.Post)
async def like_post(post_id: int,
                    current_user: Annotated[user_scheme.User, Depends(get_current_user)],
                    db: Annotated[Session, Depends(get_db)]):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )
    like = db.query(Like).filter(Like.post_id == post_id).first()
    if like:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You already liked this post",
        )
    new_like = Like(post_id=post_id, user_id=current_user)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return post


@router.post("/{post_id}/unlike", response_model=post_scheme.Post)
async def unlike_post(post_id: int,
                      current_user: Annotated[user_scheme.User, Depends(get_current_user)],
                      db: Annotated[Session, Depends(get_db)]):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    like = db.query(Like).filter(Like.post_id == post_id).first()
    if not like:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You didn't like this post",
        )
    db.delete(like)
    db.commit()
    return post


@router.get("/analytics")
async def get_analytics(date_from: date, date_to: date,
                        current_user: Annotated[user_scheme.User, Depends(get_current_user)],
                        db: Annotated[Session, Depends(get_db)]):
    delta = date_to - date_from
    dates = [date_to - datetime.timedelta(days=i) for i in range(delta.days + 1)]

    results = db.query(
        func.date(Post.created_at).label("date"),
        func.count(Post.id).label("posts"),
        func.count(Like.id).label("likes")
    ).outerjoin(Like).group_by("date").filter(Post.created_at.between(date_from, date_to)).all()

    analytics = {}
    for d in dates:
        analytics[d.strftime("%Y-%m-%d")] = {"likes": 0, "posts": 0}

    for row in results:
        date_str = row.date.strftime("%Y-%m-%d")
        analytics[date_str]["likes"] = row.likes
        analytics[date_str]["posts"] = row.posts

    return analytics

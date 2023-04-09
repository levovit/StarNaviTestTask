from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import date
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.post import Post
from app.utils.db import get_db

router = APIRouter()


@router.post("/")
async def create_post(post: Post, db: Session = Depends(get_db)):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@router.get("/")
async def get_all_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@router.post("/{post_id}/like")
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


@router.post("/{post_id}/unlike")
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

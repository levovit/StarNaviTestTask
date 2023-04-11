from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import date
from sqlalchemy.orm import Session

from utils.auth_utils import get_current_user
from utils.db_utils import get_db
from utils import post_utils
from schemas import post_scheme, user_scheme


router = APIRouter()


@router.post("/", response_model=post_scheme.Post)
def create_post_route(
    post: post_scheme.PostCreate,
    current_user: Annotated[user_scheme.User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    new_post = post_utils.create_post(db, post, current_user.id)
    return new_post


@router.get("/", response_model=list[post_scheme.Post])
def get_all_posts_route(
    current_user: Annotated[user_scheme.User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return post_utils.get_all_posts(db)


@router.post("/{post_id}/like", response_model=post_scheme.Post)
def like_post_route(
    post_id: int,
    current_user: Annotated[user_scheme.User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    post = post_utils.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )
    like = post_utils.get_like_by_post_and_user(db, post_id, current_user.id)
    if like:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You already liked this post",
        )
    post_utils.like_post(db, post_id, current_user.id)
    return post


@router.post("/{post_id}/unlike", response_model=post_scheme.Post)
def unlike_post_route(
    post_id: int,
    current_user: Annotated[user_scheme.User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    post = post_utils.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    like = post_utils.get_like_by_post_and_user(db, post_id, current_user.id)
    if not like:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You didn't like this post",
        )
    post_utils.unlike_post(db, like)
    return post


@router.get("/analytics")
def get_analytics_route(
    date_from: date,
    date_to: date,
    current_user: Annotated[user_scheme.User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return post_utils.get_analytics(db, date_from, date_to)

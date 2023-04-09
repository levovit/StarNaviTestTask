from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from schemas import user_scheme
from schemas.user_scheme import UserActivity
from utils.db import get_db

router = APIRouter()


@router.post("/signup", response_model=user_scheme.User)
async def create_user(user: user_scheme.UserCreate,
                      db: Annotated[Session, Depends(get_db)]) -> user_scheme.User:
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists",
        )

    new_user = User(username=user.username, email=user.email)
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("{user_id}/activity/", response_model=UserActivity)
async def get_user_activity(user_id: int,
                            db: Annotated[Session, Depends(get_db)]) -> UserActivity:
    user = db.query(User).filter(User.id == user_id).first()
    return UserActivity(
        last_login=user.last_login,
        last_request=user.last_request,
    )

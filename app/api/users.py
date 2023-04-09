from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import user_scheme
from app.utils.db import get_db


router = APIRouter()


@router.post("/signup", response_model=user_scheme.User)
async def create_user(user: user_scheme.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists",
        )

    user.set_password(user.password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

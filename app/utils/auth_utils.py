from typing import Optional, Annotated
from datetime import datetime, timedelta
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from config import settings
from models.user import User
from utils.db_utils import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except jwt.PyJWTError:
        raise ValueError("Invalid token")


def get_current_user(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_scheme)],
) -> User:
    try:
        payload = decode_jwt_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        user.last_request = datetime.utcnow()
        db.add(user)
        db.commit()
        return user
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = db.query(User).filter(User.username == username).first()
    if user and user.check_password(password):
        return user
    return None


def update_last_login(db: Session, user: User):
    user.last_login = datetime.utcnow()
    db.add(user)
    db.commit()

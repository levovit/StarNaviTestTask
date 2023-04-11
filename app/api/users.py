from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from schemas import user_scheme
from schemas.user_scheme import UserActivity
from utils.db_utils import get_db
from utils.logger_utils import get_logger
from utils.user_utils import get_existing_user, create_user, get_user_by_id


router = APIRouter()
logger = get_logger(__name__)


@router.post("/signup", response_model=user_scheme.User)
def create_user_route(
    user: user_scheme.UserCreate, db: Annotated[Session, Depends(get_db)]
) -> user_scheme.User:
    existing_user = get_existing_user(db, user.username, user.email)
    if existing_user:
        logger.info(f"User {user.username} failed to signup cause already exists")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists",
        )

    new_user = User(username=user.username, email=user.email)
    new_user.set_password(user.password)
    created_user = create_user(db, new_user)
    logger.info(f"User {user.username} created successfully.")
    return created_user


@router.get("{user_id}/activity/", response_model=UserActivity)
def get_user_activity(
    user_id: int, db: Annotated[Session, Depends(get_db)]
) -> UserActivity:
    user = get_user_by_id(db, user_id)
    return UserActivity(
        last_login=user.last_login,
        last_request=user.last_request,
    )

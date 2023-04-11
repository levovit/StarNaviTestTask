from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing_extensions import Annotated
from utils.auth_utils import (
    create_jwt_token,
    authenticate_user,
    update_last_login,
)
from utils.db_utils import get_db
from utils.logger_utils import get_logger


router = APIRouter()
logger = get_logger(__name__)


@router.post("/login")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        logger.warning(f"User {form_data.username} authentication failed")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_jwt_token({"sub": str(user.id)})
    update_last_login(db, user)
    logger.info(f"User {form_data.username} authentication successful")
    return {"access_token": access_token, "token_type": "bearer"}

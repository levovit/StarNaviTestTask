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


router = APIRouter()


@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
          db: Annotated[Session, Depends(get_db)]):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_jwt_token({"sub": str(user.id)})
    update_last_login(db, user)
    return {"access_token": access_token, "token_type": "bearer"}

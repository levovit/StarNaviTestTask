from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from app.models.user import User
from app.utils.auth_helpers import create_jwt_token, decode_jwt_token
from app.utils.db import get_db
from app.config import settings


router = APIRouter()


@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not user.check_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_jwt_token({"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

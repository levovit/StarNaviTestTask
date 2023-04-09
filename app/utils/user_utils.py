from sqlalchemy.orm import Session
from models.user import User


def get_existing_user(db: Session, username: str, email: str) -> User:
    return db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()


def create_user(db: Session, user_data: User) -> User:
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

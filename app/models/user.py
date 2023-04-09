from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from passlib.hash import bcrypt
from models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(100), nullable=False)
    last_login = Column(DateTime(timezone=True), nullable=True)
    last_request = Column(DateTime(timezone=True), nullable=True)

    likes = relationship("Like", back_populates="user")
    posts = relationship("Post", back_populates="user")

    def set_password(self, password: str):
        self.password_hash = bcrypt.hash(password)

    def check_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password_hash)

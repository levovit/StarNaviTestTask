from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from models.base import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

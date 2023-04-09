import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session
from models.post import Post, Like
from schemas import post_scheme


def create_post(db: Session, post_data: post_scheme.PostCreate, user_id: int) -> Post:
    new_post = Post(title=post_data.title, content=post_data.content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db: Session) -> list[Post]:
    return db.query(Post).all()


def like_post(db: Session, post_id: int, user_id: int) -> Post:
    new_like = Like(post_id=post_id, user_id=user_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like


def unlike_post(db: Session, like: Like) -> None:
    db.delete(like)
    db.commit()


def get_post_by_id(db: Session, post_id: int) -> Post:
    return db.query(Post).filter(Post.id == post_id).first()


def get_like_by_post_and_user(db: Session, post_id: int, user_id: int) -> Like:
    return db.query(Like).filter(Like.post_id == post_id, Like.user_id == user_id).first()


def get_analytics(db: Session, date_from, date_to):
    delta = date_to - date_from
    dates = [date_to - datetime.timedelta(days=i) for i in range(delta.days + 1)]

    results = db.query(
        func.date(Post.created_at).label("date"),
        func.count(Post.id).label("posts"),
        func.count(Like.id).label("likes")
    ).outerjoin(Like).group_by("date").filter(Post.created_at.between(date_from, date_to)).all()

    analytics = {}
    for d in dates:
        analytics[d.strftime("%Y-%m-%d")] = {"likes": 0, "posts": 0}

    for row in results:
        date_str = row.date.strftime("%Y-%m-%d")
        analytics[date_str]["likes"] = row.likes
        analytics[date_str]["posts"] = row.posts
    return analytics

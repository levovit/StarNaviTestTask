from fastapi import APIRouter

from api import auth, users, posts

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(posts.router, prefix="/posts", tags=["posts"])

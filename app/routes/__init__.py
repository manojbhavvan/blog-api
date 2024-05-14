from fastapi import APIRouter
from . import posts, comments, likes

router = APIRouter()

router.include_router(posts.router, tags=["Posts"])
router.include_router(comments.router,tags=["Comments"])
router.include_router(likes.router, tags=["Likes"])

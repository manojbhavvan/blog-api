from fastapi import APIRouter, HTTPException
from app import db
from app.models import Like

router = APIRouter()

@router.post("/posts/{post_id}/like/", response_model=Like)
async def like_post(post_id: str, like: Like):
    like.post_id = post_id
    existing_like = await db.likes.find_one({"post_id": post_id, "user_id": {"$ne": like.author_id}})
    if existing_like:
        post = await db.posts.find_one({"id": post_id})
        if post:
            await db.posts.update_one({"id": post_id}, {"$inc": {"like_count": 1}})
        else:
            raise HTTPException(status_code=404, detail="Post not found")
        return {"message": "Post liked successfully."}
    else:
        raise HTTPException(status_code=400, detail="Cannot like a post that is already liked by the same user.")

@router.post("/posts/{post_id}/dislike/", response_model=Like)
async def dislike_post(post_id: str, dislike: Like):
    dislike.post_id = post_id
    existing_like = await db.likes.find_one({"post_id": post_id, "user_id": {"$ne": dislike.author_id}})
    if existing_like:
        post = await db.posts.find_one({"id": post_id})
        if post:
            await db.posts.update_one({"id": post_id}, {"$inc": {"like_count": -1}})
        else:
            raise HTTPException(status_code=404, detail="Post not found")
        return {"message": "Post disliked successfully."}
    else:
        raise HTTPException(status_code=400, detail="Cannot dislike a post that is already disliked by the same user.")


from fastapi import APIRouter, HTTPException
from app import db
from app.models import Like

router = APIRouter()

@router.post("/posts/{post_id}/like/", response_model=Like)
async def like_post(post_id: str, like: Like):
    like.post_id = post_id
    existing_like = await db.likes.find_one({"post_id": post_id, "user_id": like.author_id})
    if existing_like:
        if like.liked_at:
            await db.likes.update_one({"_id": existing_like["_id"]}, {"$set": like.dict()})
            return {"message": "Post liked successfully."}
        else:
            await db.likes.delete_one({"_id": existing_like["_id"]})
            return {"message": "Like removed successfully."}
    else:
        if like.liked_at:
            new_like = await db.likes.insert_one(like.dict())
            return {**like.dict(), "id": str(new_like.inserted_id), "message": "Post liked successfully."}
        else:
            raise HTTPException(status_code=400, detail="Cannot dislike a post that is not liked.")

@router.post("/posts/{post_id}/dislike/", response_model=Like)
async def dislike_post(post_id: str, dislike: Like):
    dislike.post_id = post_id
    existing_like = await db.likes.find_one({"post_id": post_id, "user_id": dislike.author_id})
    if existing_like:
        if dislike.disliked_at:
            await db.likes.update_one({"_id": existing_like["_id"]}, {"$set": dislike.dict()})
            return {"message": "Post disliked successfully."}
        else:
            await db.likes.delete_one({"_id": existing_like["_id"]})
            return {"message": "Dislike removed successfully."}
    else:
        if dislike.disliked_at:
            new_dislike = await db.likes.insert_one(dislike.dict())
            return {**dislike.dict(), "id": str(new_dislike.inserted_id), "message": "Post disliked successfully."}
        else:
            raise HTTPException(status_code=400, detail="Cannot like a post that is not disliked.")

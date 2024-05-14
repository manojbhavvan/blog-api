from fastapi import APIRouter, HTTPException
from app import db
from app.models import Comment

router = APIRouter()

@router.post("/posts/{post_id}/comments/", response_model=Comment)
async def create_comment(post_id: str, comment: Comment):
    comment.post_id = post_id
    new_comment = await db.comments.insert_one(comment.dict(exclude_unset=True))
    return {**comment.dict(), "id": str(new_comment.inserted_id)}

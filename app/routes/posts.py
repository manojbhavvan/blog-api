from typing import List
from fastapi import APIRouter, HTTPException
from app import db
from app.models import Post, PostUpdate

from bson import ObjectId

router = APIRouter()

@router.get("/posts/", response_model=List[Post])
async def get_posts():
    posts = await db.posts.find().to_list(length=None)  # Set length=None to return all documents
    return posts

@router.post("/posts/", response_model=Post)
async def create_post(post: Post):
    new_post = await db.posts.insert_one(post.dict())
    return {**post.dict(), "id": str(new_post.inserted_id)}

@router.put("/posts/{post_id}/update/", response_model=Post)
async def update_post(post_id: str, post_data: PostUpdate):
    # Convert post_id to ObjectId
    post_oid = ObjectId(post_id)

    # Check if post exists
    existing_post = await db.posts.find_one({"_id": post_oid})
    if existing_post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    # Update the post data
    updated_data = post_data.dict(exclude_unset=True)  # Exclude unset fields (not provided in request)
    await db.posts.update_one({"_id": post_oid}, {"$set": updated_data})

    # Fetch the updated post
    updated_post = await db.posts.find_one({"_id": post_oid})
    return updated_post

@router.delete("/posts/{post_id}/delete/", response_model=str)
async def delete_post(post_id: str):
    # Convert post_id to ObjectId type
    post_object_id = ObjectId(post_id)
    
    deleted_post = await db.posts.delete_one({"_id": post_object_id})  # Use _id field for ObjectId search
    if deleted_post.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return f"Post with ID {post_id} deleted successfully"

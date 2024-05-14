from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Post(BaseModel):
    id: str
    title: str
    content: str
    author_id: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    like_count: int = 0
    
class PostUpdate(BaseModel):
    title: str = Field(None, title="Updated Title")
    content: str = Field(None, title="Updated Content")
    updated_at: datetime = Field(datetime.now(), title="Updated At")

class Comment(BaseModel):
    id: str
    post_id: str
    comment: str
    author_id: str
    created_at: datetime = datetime.now()

class Like(BaseModel):
    post_id: str
    author_id: str
    liked_at: Optional[datetime] = None
    disliked_at: Optional[datetime] = None

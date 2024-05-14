from fastapi import FastAPI
from app import app
from app.routes import posts, comments, likes

app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)

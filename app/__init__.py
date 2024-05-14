from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URI") # Create a .env under app and add your MongoDB URI 
client = AsyncIOMotorClient(MONGODB_URL)
db = client["Cluster0"] # Change the name of your cluster

# Import route handlers and include routers
from app.routes import router as api_router

app.include_router(api_router)

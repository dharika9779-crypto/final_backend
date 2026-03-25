"""
database.py
-----------
MongoDB connection for LabelLens
"""

from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_URL)
db = client["labellens"]
users_collection = db["users"]
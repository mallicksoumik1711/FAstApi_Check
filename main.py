from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from schemas import UserSchema, UpdateUserSchema
import crud

app = FastAPI()

# MongoDB Connection
MONGO_URI = "mongodb://127.0.0.1:27017"
DB_NAME = "fastapi_db"

client = AsyncIOMotorClient(MONGO_URI)
db: AsyncIOMotorDatabase = client[DB_NAME]

# Dependency to inject database
def get_db():
    return db

@app.post("/users/")
async def create_user(user: UserSchema, db: AsyncIOMotorDatabase = Depends(get_db)):
    return await crud.create_user(db, user)

@app.get("/users/")
async def get_users(db: AsyncIOMotorDatabase = Depends(get_db)):
    return await crud.get_users(db)

@app.put("/users/{user_id}")
async def update_user(user_id: str, user: UpdateUserSchema, db: AsyncIOMotorDatabase = Depends(get_db)):
    return await crud.update_user(db, user_id, user)

@app.delete("/users/{user_id}")
async def delete_user(user_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    return await crud.delete_user(db, user_id)

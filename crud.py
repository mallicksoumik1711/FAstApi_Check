from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from schemas import UserSchema, UserResponseSchema, UpdateUserSchema

# Create a new user
async def create_user(db: AsyncIOMotorDatabase, user: UserSchema):
    user_dict = user.dict()
    result = await db.users.insert_one(user_dict)
    
    # Rename _id to id for Pydantic schema validation
    user_dict["id"] = str(result.inserted_id)  
    user_dict.pop("_id", None)  # Remove _id if it exists
    user_node = user_dict.pop("_id", **user_dict)

    return UserResponseSchema(**user_dict)

# Get all users
async def get_users(db: AsyncIOMotorDatabase):
    users = await db.users.find().to_list(100)
    return [{**user, "_id": str(user["_id"])} for user in users]

# Get a single user by ID
async def get_user(db: AsyncIOMotorDatabase, user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return user
    return None

# Update user
async def update_user(db: AsyncIOMotorDatabase, user_id: str, user_data: UpdateUserSchema):
    user_dict = {k: v for k, v in user_data.model_dump().items() if v is not None}
    if not user_dict:
        return {"error": "No fields to update"}
    
    result = await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict})
    
    if result.modified_count:
        updated_user = await db.users.find_one({"_id": ObjectId(user_id)})
        updated_user["_id"] = str(updated_user["_id"])
        return updated_user
    return {"error": "User not found"}

# Delete user
async def delete_user(db: AsyncIOMotorDatabase, user_id: str):
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        return {"message": "User deleted"}
    return {"error": "User not found"}

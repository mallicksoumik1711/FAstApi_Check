from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://127.0.0.1:27017"
DB_NAME = "TaskManager_crud"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
user_collection = database["users"]

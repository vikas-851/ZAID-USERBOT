from typing import Dict, List, Union
from Zaid.database import dbb as db
from pymongo import MongoClient

# MongoDB URI
MONGO_DB_URI = "mongodb+srv://tanjiro1564:tanjiro1564@cluster0.pp5yz4e.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(MONGO_DB_URI)
db = client["MUK_users"]

# Collection for gmutes
gmute_db = db["gmute_db"]

# GMute Functions
def is_user_gmuted(user_id: int) -> bool:
    user = gmute_db.find_one({"user_id": user_id})
    return user is not None

def add_gmute(user_id: int):
    if not is_user_gmuted(user_id):
        gmute_db.insert_one({"user_id": user_id})

def remove_gmute(user_id: int):
    if is_user_gmuted(user_id):
        gmute_db.delete_one({"user_id": user_id})

def is_gmute(user_id: int) -> bool:
    return is_user_gmuted(user_id)

def get_gmute_list() -> List[dict]:
    return list(gmute_db.find({}))

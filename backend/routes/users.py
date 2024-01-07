from fastapi import APIRouter
from bson import ObjectId
from pymongo import ReturnDocument
from models.user import User
from config.database import users_collection
from schemas.user import userEntity, usersEntity

user_router = APIRouter(prefix="/users")


@user_router.get("/")
async def get_users():
    return usersEntity(users_collection.find())


@user_router.post("/")
async def add_user(user: User):
    return str(users_collection.insert_one(dict(user)).inserted_id)


@user_router.get("/{id}")
async def find_user(id: str):
    return userEntity(users_collection.find_one({"_id": ObjectId(id)}))


@user_router.put("/{id}")
async def update_user(id: str, user: User):
    return userEntity(
        users_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": dict(user)},
            return_document=ReturnDocument.AFTER,
        )
    )


@user_router.delete("/{id}")
async def delete_user(id: str):
    return userEntity(users_collection.find_one_and_delete({"_id": ObjectId(id)}))

from fastapi import APIRouter
from bson import ObjectId
from pymongo import ReturnDocument
from models.match import Official_Match, Custom_Match
from config.api import get_all_matches_league
from config.database import custom_matches_collection

match_router = APIRouter(prefix="/matches")


@match_router.get("/")
async def get_matches():
    return get_all_matches_league("australian-open")


@match_router.post("/custom")
async def post_custom_match(match: Custom_Match):
    return str(custom_matches_collection.insert_one(dict(match)).inserted_id)

from fastapi import APIRouter
from bson import ObjectId
from pymongo import ReturnDocument
from models.match import Match
from config.api import get_all_matches_league

match_router = APIRouter(prefix="/matches")


@match_router.get("/")
async def get_matches():
    return get_all_matches_league("australian-open")

import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ["API_KEY"]

Ccds = ["australian-open", "us-open", "wimbledon", "french-open"]


def get_all_matches_league(league: str) -> list:
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"

    querystring = {
        "Category": "tennis",
        "Ccd": league,
        "Scd": "mens-singles",
        "Timezone": "-3",
    }

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    matches = []
    for event in response.json()["Stages"][0]["Events"]:
        event.pop("Pids")
        event.pop("Sids")
        event.pop("Ecov")
        event.pop("ErnInf")
        event.pop("Et")
        event.pop("EO")
        event.pop("EOX")
        event.pop("Ehid")
        event.pop("Spid")
        event.pop("Pid")
        event["T1"][0].pop("Abr")
        event["T1"][0].pop("tbd")
        event["T1"][0].pop("Gd")
        event["T1"][0].pop("Pids")
        event["T1"][0].pop("HasVideo")
        event["T2"][0].pop("Abr")
        event["T2"][0].pop("tbd")
        event["T2"][0].pop("Gd")
        event["T2"][0].pop("Pids")
        event["T2"][0].pop("HasVideo")
        matches.append(event)
    return matches

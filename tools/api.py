from tools.utils import load_json_data
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
STEAMID = os.getenv("steamid")


def get_owned_games_api():
    """
    This function gets a list of owned games using the api key and steamid provided in the .env file

    :return: returns a list of owned games
    """

    try:
        url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        params = {"key": API_KEY, "steamid": STEAMID, "include_appinfo": "true", "format": "json"}

        response = requests.get(url, params=params)
        data = response.json()
        print("Successfully loaded JSON data from api")
        return data
    except Exception as e:
        print(f"Exception encountered getting owned games, did you set api key and steamid in .env file?: {e}")
        print("Loading mock data from JSON file as fallback.")
        return load_json_data(Path(__file__).parent.parent / "data" / "getownedgames.json")



def get_recent_games_api():
    """
    This function gets a list of games played in the last 2 weeks using the api key and steamid provided in the .env file

    :param count: the amount of recent games to get, if left empty 10 is used
    :return: returns a list of recently played games
    """

    try:
        url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/"
        params = {"key": API_KEY, "steamid": STEAMID, "format": "json"}

        response = requests.get(url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print(f"Exception encountered getting recent games, did you set api key and steamid in .env file?: {e}")
        print("Loading mock data from JSON file as fallback.")
        return load_json_data(Path(__file__).parent.parent / "data" / "getrecentlyplayed.json")



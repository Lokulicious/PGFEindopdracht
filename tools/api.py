import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
steamid = os.getenv("steamid")


def get_owned_games():
    """
    This function gets a list of owned games using the api key and steamid provided in the .env file

    :return: returns a list of owned games
    """

    try:
        url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        params = {"key": api_key, "steamid": steamid, "include_appinfo": "true", "format": "json"}

        response = requests.get(url, params=params)
        data = response.json()
        print("Successfully loaded JSON data from api")
        return data
    except Exception as e:
        print(f"Exception encountered getting owned games: {e}")
        print("Loading mock data from JSON file as fallback.")
        return load_mock_json_data(Path(__file__).parent.parent / "data" / "getownedgames.json")



def get_recent_games(count = 10):
    """
    This function gets a list of games played in the last 2 weeks using the api key and steamid provided in the .env file

    :param count: the amount of recent games to get, if left empty 10 is used
    :return: returns a list of recently played games
    """

    try:
        url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/"
        params = {"key": api_key, "steamid": steamid, "count": count, "format": "json"}

        response = requests.get(url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print(f"Exception encountered getting recent games: {e}")
        print("Loading mock data from JSON file as fallback.")
        return load_mock_json_data(Path(__file__).parent.parent / "data" / "getrecentlyplayed.json")


def load_mock_json_data(path):
    """
    returns mock JSON data from file in case api is not reachable

    :param path:
    :return: JSON Data from file
    """

    try:
        with open(path) as p:
            data = json.load(p)
        return data
    except Exception as e:
        print(f"Ran into problem fetching data from file: {e}")
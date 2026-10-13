import os
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
    # TODO: add error handling for empty/wrong api key/steamid
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    params = {"key": api_key, "steamid": steamid, "include_appinfo": "true", "format": "json"}

    response = requests.get(url, params=params)
    data = response.json()
    return data


def get_recent_games(count = 10):
    """
    This function gets a list of games played in the last 2 weeks using the api key and steamid provided in the .env file

    :param count: the amount of recent games to get, if left empty 10 is used
    :return: returns a list of recently played games
    """
    # TODO: add error handling for empty/wrong api key/steamid
    url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/"
    params = {"key": api_key, "steamid": steamid, "count": count, "format": "json"}

    response = requests.get(url, params=params)
    data = response.json()
    return data
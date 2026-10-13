import random

from tools import api




def get_owned_games():
    """Returns a usable list of owned games using the JSON api response"""
    owned_games_json = api.get_owned_games()
    return owned_games_json["response"]["games"]

def get_recent_games(count):
    """Returns a usable list of recently played (past 2 weeks) games using the JSON api response"""
    recent_games_json = api.get_recent_games(count)
    return recent_games_json["response"]["games"]

def get_random_game(game_list):
    """Returns random game from given list of games"""
    random_game = game_list[random.randint(0, len(game_list))]
    return random_game

def check_input(user_input, min_input, max_input):
    if not min_input <= user_input <= max_input:
        raise Exception(f"Input outside of allowed range (min: {min_input}, max: {max_input}")
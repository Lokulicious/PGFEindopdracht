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

def get_random_games(game_list, amount):
    """
    Returns random game from given list of games

    :param game_list:
    :param amount:
    :return:
    """
    # TODO: index is out of range when it shouldn't be, fix it
    i = 0
    return_list = []

    if amount == len(game_list):
        return game_list
    elif amount == 1:
        return_list.append(game_list[random.randint(0, len(game_list - 1))])
        return return_list
    else:
        return_list = game_list
        while len(return_list) > amount:
            del return_list[random.randint(0, len(return_list) - 1)]

        return return_list
        #
        # while i < amount:
        #     game = game_list[random.randint(0, len(game_list - 1))]
        #     if game not in return_list:
        #         return_list.append(game)
        #         i += 1

    # random_game = game_list[random.randint(0, len(game_list))]
    return return_list

def check_input(user_input, min_input, max_input):
    if not min_input <= user_input <= max_input:
        raise Exception(f"Input outside of allowed range (min: {min_input}, max: {max_input}")
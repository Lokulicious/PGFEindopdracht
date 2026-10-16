import random
from tools import utils
from tools import api

def show_recent_games(count):
    """
    Shows a list of given amount of games played in the last 2 weeks by owner of userid provided in .env

    :param count: amount of games to show
    """
    recent_games = get_recent_games()

    try:
        utils.check_input(count, 1, len(recent_games))
    except Exception as e:
        print(f"Invalid input: {e}")

    if len(recent_games) < count:
        count = len(recent_games)
        print(f"Only {count} games played in last 2 weeks found. \n")
    elif count <= 0:
        print("number of games has to be higher than 0")
        return

    utils.print_game_list(recent_games, count)
    print(f"These are the top {count} games you played in the last 2 weeks by playtime \n")

    return recent_games




def show_random_games(amount, game_list):
    """
    This function gets 1 or more random games from a given list of games

    :param amount: the amount of games to show
    :param game_list: the list which the games are selected from
    """
    try:
        utils.check_input(amount, 1, len(game_list))
    except Exception as e:
        print(f"Error: {e}")
    else:
        random_games = get_random_games(game_list, amount)
        utils.print_game_list(random_games, amount)
        return random_games






def get_owned_games():
    """
    Returns a usable list of owned games using the JSON api response
    :return:
    """
    # TODO: RENAME API METHODS TO NOT CONFLICT WITH THESE
    owned_games_json = api.get_owned_games()
    return owned_games_json["response"]["games"]

def get_recent_games():
    """
    Returns a usable list of recently played (past 2 weeks) games using the JSON api response

    :return:
    """
    # TODO: RENAME API METHODS TO NOT CONFLICT WITH THESE
    recent_games_json = api.get_recent_games()
    return recent_games_json["response"]["games"]


def get_random_games(game_list, amount):
    """
    Returns random game from given list of games

    :param game_list:
    :param amount:
    :return:
    """
    i = 0
    return_list = []

    if amount == len(game_list):
        return game_list
    elif amount == 1:
        return_list.append(game_list[random.randint(0, len(game_list) - 1)])
        return return_list
    else:
        return_list = game_list
        while len(return_list) > amount:
            del return_list[random.randint(0, len(return_list) - 1)]

        return return_list
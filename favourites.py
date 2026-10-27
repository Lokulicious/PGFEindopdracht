from pathlib import Path
from tools import utils
import logging

JSON_PATH = Path(__file__).parent / "data" / "favouritegames.json"
LOGGER = logging.getLogger(__name__)

def load_favourite_games():
    favourite_games = utils.load_json_data(JSON_PATH)
    return favourite_games

def save_favourite_game(game):
    favourite_games = load_favourite_games()
    if not favourite_games:
        utils.save_json_data(JSON_PATH, [game])
    elif game in favourite_games:
        print(f"{game["name"]} was already in favourites")
        LOGGER.warning(f"adding game to favourites failed, {game["name"]} was already in favourites")
    else:
        favourite_games.append(game)
        utils.save_json_data(JSON_PATH, favourite_games)
        print(f"Saved {game["name"]} to list of favourite games")

def remove_favourite_game(game_index):
    favourite_games = load_favourite_games()
    if not favourite_games:
        return
    else:
        print(f"Removed {favourite_games[game_index - 1]["name"]} from favourites")
        favourite_games.remove(favourite_games[game_index - 1])
        utils.save_json_data(JSON_PATH, favourite_games)


def show_favourite_games():
    favourite_games = load_favourite_games()
    if not favourite_games:
        print("You have not saved any favourite games yet.")
        return

    print("Your current list of favourite games:")
    utils.print_game_list(favourite_games, len(favourite_games))

def add_game_from_list(game_list, game_index):
    game = game_list[game_index]
    save_favourite_game(game)

def get_favourite_games_amount():
    favourite_games = load_favourite_games()
    return len(favourite_games)

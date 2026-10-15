from pathlib import Path
from tools import utils
import games

JSON_PATH = Path(__file__).parent / "data" / "favouritegames.json"

def load_favourite_games():
    favourite_games = utils.load_json_data(JSON_PATH)
    return favourite_games

def save_favourite_game(game):
    favourite_games = load_favourite_games()
    if not favourite_games:
        utils.save_json_data(JSON_PATH, [game])
    else:
        favourite_games.append(game)
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
    print(f"Saved {game["name"]} to list of favourite games")
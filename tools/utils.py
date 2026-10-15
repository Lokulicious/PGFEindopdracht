import json


def check_input(user_input, min_input, max_input):
    if not min_input <= user_input <= max_input:
        raise Exception(f"Input outside of allowed range (min: {min_input}, max: {max_input}")


def load_json_data(path):
    """
    loads JSON data from file and returns it

    :param path:
    :return: JSON Data from file
    """

    try:
        with open(path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File does not exist yet, no data to load")
    except Exception as e:
        print(f"Ran into problem fetching data from file: {e}")

def save_json_data(path, data):
    """
    saves data to existing JSON file or creates new file if it does not exist yet

    :param path:
    :param data:
    """

    try:
        with open(path, "w") as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Ran into problem saving JSON data to file: {e}")

def does_file_exist(path):
    return path.exists()

def print_game_list(game_list, count):
    """
    prints name and the total playtime of a given amount of games from a given list

    :param game_list:
    :param count:
    :return:
    """
    i = 0

    while i < count:
        game_string = f"{i + 1}. {game_list[i]["name"]}      Time played: {game_list[i]["playtime_forever"]} minutes"
        print(game_string)
        i += 1
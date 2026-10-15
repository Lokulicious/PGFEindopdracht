from tools import utils

def main():
    """
    Main application function
    """

    show_random_games(13, utils.get_recent_games(11))





def show_recent_games(count):
    """
    Shows a list of given amount of games played in the last 2 weeks by owner of userid provided in .env

    :param count: amount of games to show
    """
    recent_games = utils.get_recent_games(count)

    if len(recent_games) < count:
        count = len(recent_games)
        print(f"Only {count} games played in last 2 weeks found. \n")

    print_game_list(recent_games, count)

    print(f"These are the top {count} games you played in the last 2 weeks by playtime \n")




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
        # if amount == 1:
        #     utils.get_random_game(game_list)
        # else:
            # game_dict = {}
            # #     TODO: change amount of games to get system at request, not after
            # while len(game_dict) < amount:
            #     game = utils.get_random_game(game_list)
            #     game_dict.update({len(game_dict): game})
            #     # game_list.append({game["appid"]: game})
            #     print("added game to list")

        random_games = utils.get_random_games(game_list, amount)

        print_game_list(random_games, amount)



def print_game_list(game_list, count):
    """
    prints name and playtime in last 2 weeks of a given amount of games from a given list

    :param game_list:
    :param count:
    :return:
    """
    i = 0

    while i < count:
        game_string = f"{i + 1}. {game_list[i]["name"]}      playtime last 2 weeks: {game_list[i]["playtime_2weeks"]} minutes"
        print(game_string)
        i += 1

main()
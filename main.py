from tools import utils
import games
import favourites
import logging


def main():
    """
    Main application function
    """
    logging.basicConfig(filename="debug.log", encoding='utf_8', level=logging.DEBUG)

    show_main_menu()


def show_main_menu():
    """
    prints main menu and listens for user input
    :return:
    """

    while True:
        print("Main menu \n"
              "1. Search game(s) \n"
              "2. Favourite games \n"
              "0. Quit \n")
        choice = utils.get_user_input(0, 2)
        if choice == "":
            continue
        else:
            if choice == 1:
                show_games_menu()
            elif choice == 2:
                show_favourites_menu()
            elif choice == 0:
                break

def show_games_menu():
    """
    prints submenu with random game choices or recent games
    :return:
    """

    while True:
        print("Games menu: \n"
              "1. Random game(s) from library \n"
              "2. Random game(s) from favourite games \n"
              "3. Show most played games in the last 2 weeks \n"
              "0. Back to main menu \n")

        choice = utils.get_user_input(0, 3)
        if choice == "":
            continue
        else:
            if choice == 1:
                amount_of_games = int(input("How many games do you want to print?: "))
                random_games = games.show_random_games(amount_of_games, games.get_owned_games())
                add_game = utils.get_user_input(0, len(random_games), "Press enter to continue or enter the index of a game to add it to favourite games: ")
                if add_game == "":
                    continue
                else:
                    favourites.add_game_from_list(random_games, int(add_game) - 1) # -1 to compensate for input starting at 1 and index at 0
            elif choice == 2:
                amount_of_games = int(input("How many games do you want to print?: "))
                favourite_games = favourites.load_favourite_games()
                if favourite_games:
                    games.show_random_games(amount_of_games, favourite_games)
                else:
                    print("You currently do not have any favourite games")
            elif choice == 3:
                amount_of_games = int(input("How many games do you want to print?: "))
                recent_games = games.show_recent_games(amount_of_games)
                if  not recent_games:
                    continue
                add_game = input("Press enter to continue or enter the index of a game to add it to favourite games: ")
                if add_game == "":
                    continue
                else:
                    favourites.add_game_from_list(recent_games, int(add_game) - 1)
            elif choice == 0:
                break


def show_favourites_menu():
    """
    prints submenu with favourite game choices
    :return:
    """
    while True:
        print("Favourites menu: \n"
              "1. Show favourite games \n"
              "2. Remove favourite game \n"
              "0. Return to main menu \n")
        choice = utils.get_user_input(0, 2)
        if choice == "":
            continue
        else:
            if choice == 1:
                favourites.show_favourite_games()
            elif choice == 2:
                favourites.show_favourite_games()
                remove_game = utils.get_user_input(1, favourites.get_favourite_games_amount(), "Enter the index of a game to remove it from favourite games or press enter to cancel: ")
                if remove_game == "":
                    continue
                favourites.remove_favourite_game(int(remove_game))
            elif choice == 0:
                break






main()
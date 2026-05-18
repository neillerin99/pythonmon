"""
This is the main module of the whole program.
This is the main entry point of the system.
"""

__author__ = "NEIL EDRIANE LERIN"

from classes.pokemon import Pokemon
import utils  # import utils module
import pokedex  # import pokedex module
import game


def main_menu_selection(pokemons: list[Pokemon]):
    """
    This function process the menu selection of the user
    """
    running: bool = True  # variable to store the running state

    # while loop for the infinite execution
    while running == True:

        # display menu options
        print()
        utils.display_menu("Main Menu", ["Battle", "Pokedex", "Quit"])
        choice: int | None = utils.validate_input("Enter choice")  # take user input
        utils.clear_terminal()

        # switch to determine menu choice
        match choice:
            case 1:
                game.run_game(pokemons)
            case 2:
                pokedex.init_dex_menu(pokemons)
            case 3:
                print("So long Trainer!")
                running = False
            case _:
                print("Oak: Hmm? That option does not exist!")


def main():
    utils.clear_terminal()

    pokemons: list[Pokemon] = []

    utils.initialize_data(pokemons)  # initialize pokemon data
    main_menu_selection(pokemons)


if __name__ == "__main__":
    main()

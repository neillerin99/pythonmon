"""
This module contains the core functions of the Pokedex feature.
Think of it as an entry point for the Dex feature
"""

__author__ = "NEIL EDRIANE LERIN"

from classes.pokemon import Pokemon
import utils

MENU_WIDTH = 60


def display_all(pokemons: list[Pokemon]):
    """
    Function to list all the Pokemons. Iterates through the pokemons array,
    and uses the __str__ function of the Pokemon class to print
    """

    print("Pokedex Entries".center(MENU_WIDTH))

    # map through each pokemon
    for pokemon in pokemons:
        print(pokemon)


def find_by_id(pokemons: list[Pokemon], id: int | None):
    """
    This function searches the pokemons list for a specific id.

    NOTE: the search function uses linear search which is very slow,
    and this can be improved in the future
    """

    pokemon: Pokemon | None = None  # variable to store the searched pokemon.

    # if id is empty explicitly return
    if id == None:
        return

    # for loop iteration to traverse pokemons array
    for p in pokemons:
        if p.id == id:
            pokemon = p  # if pokemon is found assign p to pokemon variable

    # display dynamically
    if pokemon:
        print("Pokedex Entry".center(MENU_WIDTH))
        print(pokemon)
    else:
        print("Oak: Hmm? That Pokemon does not exist!")


def init_dex_menu(pokemons: list[Pokemon]):
    """
    This function process the menu selection of the user
    """
    running: bool = True  # variable to store the running state

    utils.clear_terminal()

    # while loop for the infinite execution
    while running == True:
        print()
        utils.display_menu("Pokedex", ["List", "Search by Id", "Quit"])
        choice: int | None = utils.validate_input("Enter choice")  # take user input
        utils.clear_terminal()

        # match user's choice
        match choice:
            case 1:
                display_all(pokemons)
            case 2:
                find_by_id(pokemons, utils.validate_input("Enter Pokemon Id"))
            case 3:
                print("Closing Pokedex! Bye!")
                running = False
            case _:
                print("Oak: Hmm? That option does not exist!")

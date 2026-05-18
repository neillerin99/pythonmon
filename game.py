"""
This module serves as the orchestrator of the Battle feature.

Think of it as an entry point
"""

__author__ = "NEIL EDRIANE LERIN"

from classes.pokemon import Pokemon
from classes.player import Player
from classes.battle import Battle
import copy
import utils

MENU_WIDTH = 60 # menu width constant variable


def find_by_id(pokemons: list[Pokemon], id: int | None) -> Pokemon | None:
    """
    This function searches the pokemons list for a specific id.

    NOTE: the search function uses linear search which is very slow,
    and this can be improved in the future
    """

    pokemon: Pokemon | None = None  # variable to store the searched pokemon.

    # for loop iteration to traverse pokemons array
    for p in pokemons:
        if p.id == id:
            pokemon = p  # if pokemon is found assign p to pokemon variable

    # display dynamically
    if pokemon:
        pokemons.remove(pokemon)
        return pokemon
    else:
        return None


def get_player_details(available_pokemons: list[Pokemon], is_player_two: bool = False) -> Player:
    """
    This function gets user details from the user
    """

    name: str  # variable to store the name of the user
    pokemon_id: int | None  # variable to store the pokemon id
    pokemon: Pokemon | None  # variable to store the searched pokemon

    # prompt the user for their name
    if not is_player_two:
        utils.slow_print("Oak: Now tell me... what was your name again?")
    else:
        utils.slow_print("Oak: Now... what was your opponent's name again?")

    name = input()

    utils.clear_terminal()  # clear terminal

    utils.slow_print(f"Oak: Ah yes! Welcome {name}! Now then choose your Pokémon\n")

    # map through each pokemon
    for pokemon in available_pokemons:
        print(pokemon)

    # constantly loop through user input to check pokemon is valid and existing.
    # If pokemon is existing exit of the loop
    while True:
        pokemon_id: int | None = utils.validate_input(
            "Enter the ID of the Pokémon you want to choose"
        )
        pokemon = find_by_id(available_pokemons, pokemon_id)

        if pokemon is not None:
            break
        else:
            print("Oak: Hmm? That Pokemon does not exist!")

    # return Player object
    return Player(name, pokemon)


def run_game(pokemons: list[Pokemon]):
    play_again: str = "y"

    while play_again == "y":
        # copy list of pokemons array
        available_pokemons: list[Pokemon] = copy.deepcopy(pokemons)

        # initialize player class
        player1: Player = get_player_details(available_pokemons)
        utils.clear_terminal()

        # initialize player class
        player2: Player = get_player_details(available_pokemons, True)
        utils.clear_terminal()

        battle = Battle(player1, player2)  # initialize battle class
        battle.start()  # start battle

        play_again = input("Do you want to play again? (y/n): ").lower()
        utils.clear_terminal()

    print("Oak: Farewell trainers!")

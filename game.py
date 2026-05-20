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
import random

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


def get_bot_details(available_pokemons: list[Pokemon]) -> Player:
    """
    This function creates a bot instance of the Player class
    """
    trainer_names: list[str] = [
        "Brock",
        "Misty",
        "Lt. Surge",
        "Erika",
        "Koga",
        "Sabrina",
        "Blaine",
        "Giovanni",
        "Gary"
    ]  # an array of tranier names to be picked randomly
    
    trainer = trainer_names[random.randint(0, len(trainer_names) - 1 )] # get name of the trainer based on the array
    pokemon = available_pokemons[random.randint(0, len(available_pokemons) - 1 )] # get random pokemon
    
    return Player(trainer, pokemon, True)


def initialize_players(available_pokemons: list[Pokemon], is_one_player = False):
    

    if is_one_player == True:
        # initialize player class
        player1: Player = get_player_details(available_pokemons, False)
        utils.clear_terminal()
    
        # initialize player class
        player2: Player = get_bot_details(available_pokemons)
        utils.clear_terminal()
    else:
        # initialize player class
        player1: Player = get_player_details(available_pokemons)
        utils.clear_terminal()
        
        # initialize player class
        player2: Player = get_player_details(available_pokemons, True)
        utils.clear_terminal()  

    
    battle = Battle(player1, player2)  # initialize battle class
    battle.start()  # start battle


def run_game(pokemons: list[Pokemon]):
    play_again: str = "y"

    while play_again == "y":
        # copy list of pokemons array
        available_pokemons: list[Pokemon] = copy.deepcopy(pokemons)
        player_number: int | None # the number of player   
        player_number_valid : bool = False # flag used for while loop
      
        # prompt user for player options 
        while player_number_valid == False:
            utils.display_menu("Player options!", ['1 Player', '2 Players'])
            player_number = utils.validate_input("Enter choice ")
            
            if player_number == None or not (player_number >= 1 and player_number <= 2) :
                print("Oak: Hmm? That is not a valid choice young trainer!")
            else:
                player_number_valid = True
            
        utils.clear_terminal() 
        match player_number:
            case 1: 
                initialize_players(available_pokemons, True)
            case 2:
                initialize_players(available_pokemons)
            case _:
                print("Invalid choice!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        utils.clear_terminal()

    print("Oak: Farewell trainers!")

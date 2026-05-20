"""
Module that contains utility functions to handle certain logis for the system
"""

__author__ = "NEIL EDRIANE LERIN"

from classes.pokemon import Pokemon
from classes.abilities import Ability
from constants.pokemon_data import POKEMON_DATA
from constants.type import TYPE
import os
import time
from colorama import Fore

def initialize_data(pokemon_list: list[Pokemon]):
    """
    This function initializes the Pokemon details of the system.
    This uses the POKEMON_DATA array which is a list of Pokemon dictionairies
    """
    for data in POKEMON_DATA:
        pokemon = Pokemon(**data)
        pokemon_list.append(pokemon)


def clear_terminal():
    """
    This function clears the terminal using the OS module
    """
    os.system("cls" if os.name == "nt" else "clear")


def display_menu(title: str, menus: list[str]):
    """
    Function to display the main menu of the application
    """
    MENU_WIDTH = 35  # constant variable width

    # code block to handle the menu printing
    print("-" * MENU_WIDTH)
    print("|" + title.center(MENU_WIDTH - 2) + "|")
    print("-" * MENU_WIDTH)
    for i, menu in enumerate(menus):
        print(f"| [{i+1}] {menu}".ljust(MENU_WIDTH - 1) + "|")
    print("-" * MENU_WIDTH)


def slow_print(text: str):
    """
    This function adds a typing effect on the print display
    """
    delay: float = 0.02
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def validate_input(text: str) -> int | None:
    """
    This function validates user inputs and checks for int validity
    """
    try:
        choice = int(input(f"{text}: "))
        return choice
    except Exception as ex:
        print("Invalid input!")

        
def format_color(text: str, color) -> str:
    """
    This function is used to dynamically handle formatting of color.
    
    This takes text and color (ex Fore.RED) from the colorama library.
    
    This returns a string wit the combined value of the text and the color.
    """
    
    return f"{color}{text}"


def format_ability_color(ability: Ability) -> str:
    """
    This function matches an ability type to the ability ENUM,
    and returns a specific color for each ability type.
    """
    
    text: str
    
    match ability.type:
        case TYPE.FIRE:
            text = format_color(ability.name, Fore.RED)
        case TYPE.GRASS:
            text = format_color(ability.name, Fore.GREEN)
        case TYPE.WATER:
            text = format_color(ability.name, Fore.BLUE)
        case TYPE.ELECTRIC:
            text = format_color(ability.name, Fore.LIGHTYELLOW_EX)
        case TYPE.NORMAL:
            text = format_color(ability.name, Fore.WHITE)
        case _:
            text = format_color(ability.name, Fore.WHITE)
    
    return text


def format_hp(pokemon: Pokemon) -> str:
    """
    This function formats the Pokemon's hp color base on the value
    """
    
    hp_text: str = f"HP: {pokemon.hp}/{pokemon.max_hp}" # current hp display
    
    if pokemon.hp <= 15:
        hp_text = format_color(hp_text, Fore.RED)
    else: 
        hp_text = format_color(hp_text, Fore.GREEN)
        
    return hp_text
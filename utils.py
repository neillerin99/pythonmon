"""
Module that contains utility functions to handle certain logis for the system
"""

__author__ = "NEIL EDRIANE LERIN"

from classes.pokemon import Pokemon
from constants.pokemon_data import POKEMON_DATA
import os
import time


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

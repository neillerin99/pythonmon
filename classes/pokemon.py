"""
This module contains the Pokemon dataclass which will be used in the system.
This serves as the blueprint for what a Pokemon entity should have
"""

__author__ = "NEIL EDRIANE LERIN"

from dataclasses import dataclass
from constants.type import TYPE
from classes.abilities import Ability


@dataclass
class Pokemon:
    id: int  # id of the pokemon
    name: str  # name of the pokemon
    description: str  # description of the pokemon
    defense: int  # defense stat of the pokemon
    attack: int  # attack stat of the pokemon
    speed: int  # speed stat of the pokemon
    type: TYPE  # the type of the pokemon
    hp: int  # current hp of the pokemon
    max_hp: int  # max hp of the pokemon
    abilities: list[Ability]  # the pokemon's abilities


    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        defense: int,
        attack: int,
        speed: int,
        type: TYPE,
        hp: int,
        max_hp: int,
        abilities: list[dict],
    ):
        """Init function"""
        
        self.id = id
        self.name = name
        self.description = description
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.type = type
        self.hp = hp
        self.max_hp = max_hp
        self.abilities = [Ability(**ability) for ability in abilities]


    def line(self, text: str, width: int):
        """
        Function to handle formatting options for the class display
        """
        return f"| {text.ljust(width - 4)} |\n"


    def __str__(self):
        """Function to print the Pokemon"""
        
        print()
        MENU_WIDTH = 60 # menu width constant variable
        
        # formatter options
        border = "=" * MENU_WIDTH
        name = "|" + f"{self.name} (#{self.id})".center(MENU_WIDTH - 2) + "|"
        abilities_text = ", ".join(ability.name for ability in self.abilities)

        return (
            f"{border}\n"
            f"{name}\n"
            f"{border}\n"
            f"{self.line('Description: ' + self.description[:30], MENU_WIDTH)}"
            f"{self.line(f'Type: {self.type}', MENU_WIDTH)}"
            f"{self.line(f'HP: {self.hp}/{self.max_hp}', MENU_WIDTH)}"
            f"{self.line(f'ATK: {self.attack}  DEF: {self.defense}  SPD: {self.speed}', MENU_WIDTH)}"
            f"{self.line(f'Abilities: {abilities_text}', MENU_WIDTH)}"
            f"{border}\n"
        )

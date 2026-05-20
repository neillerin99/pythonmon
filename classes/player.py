"""
This module contains the Player dataclass
"""

__author__ = "NEIL EDRIANE LERIN"

from dataclasses import dataclass
from classes.pokemon import Pokemon


@dataclass
class Player:
    name: str  # name of the player
    pokemon: Pokemon  # selected Pokemon of the player
    is_bot: bool = False # bot flag to identify if a player instance is a bot

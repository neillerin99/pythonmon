"""
This module defines the Ability.
This contains properties that an ability must have
"""

__author__ = "NEIL EDRIANE LERIN"

from dataclasses import dataclass
from constants.type import TYPE
import random


@dataclass
class Ability:
    index: int  # property to identify the ability
    name: str  # name of the ability
    damage: int  # damage value of the ability
    type: TYPE  # the type of the ability
    accuracy: int  # the accuracy of the ability
    description: str  # description of the ability
    critical: int  # crititcal chance of the ability

    def does_move_hit(self) -> bool:
        """
        Function to determine accuracy, this gets a random integer does a comparison the a move's accuracy
        If the random int is greater than the move accuracy, that means that the move misses.
        Returns a boolean
        """
        return random.randint(1, 100) <= self.accuracy


    def is_critical(self) -> bool:
        """
        Function to determine critical chance.
        If random int is greater than move crit change,
        this means that the move causes a critical
        """
        return random.randint(1, 90) <= self.critical

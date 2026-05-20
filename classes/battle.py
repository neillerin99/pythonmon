"""
This module contains the Battle dataclass.

This contains properties and methods for the Battle feature
"""

__author__ = "NEIL EDRIANE LERIN"

from dataclasses import dataclass
from classes.player import Player
from classes.pokemon import Pokemon
from classes.abilities import Ability
import utils
import game_ui
import random
import time

@dataclass
class Battle:
    player1: Player  # player 1 class
    player2: Player  # player 2 class
    attacker: Player  # current player as attacker
    defender: Player  # current player as defender


    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2


    def determine_first(self):
        """
        Function to check the first player to take turn first.
        This is based on the speed stat of the Pokemon
        """

        # variable to store the Pokemon of player 1
        pokemon_1: Pokemon = self.player1.pokemon

        # variable to store the Pokemon of player 2
        pokemon_2: Pokemon = self.player2.pokemon

        # condition to check if the speed of pokemon 1 is greater than pokemon 2
        if pokemon_1.speed >= pokemon_2.speed:
            self.attacker = self.player1  # assign player 1 as attacker
            self.defender = self.player2  # assign player 2 as defender
        else:
            self.attacker = self.player2  # assign player 2 as attacker
            self.defender = self.player1  # assign player 1 as defender


    def find_ability(self, choice: int) -> Ability | None:
        """Function to dynamically map the choosen ability to a pokemon's ability"""
        abilities: list[Ability] = self.attacker.pokemon.abilities

        # for loop to find ability
        for ability in abilities:
            # if ability index equals to user choice
            if ability.index == choice:
                return ability


    def random_ability(self) -> int:
        """
        This function, returns a random index on the Pokemon's ability.
        """
        
        return random.randint(1, len(self.attacker.pokemon.abilities))


    def calculate_damage(self, ability: Ability) -> int:
        """Calculates damage based on attacker and defender stats"""
        
        # calculate damage based on pokemon's attack stat, and defender pokemon's defense
        damage = round((self.attacker.pokemon.attack / self.defender.pokemon.defense)* ability.damage/ 10)

        # random multiplier between 85% and 100%
        damage *= random.uniform(0.85, 1.0)

        return round(damage)


    def handle_turn(self):
        """
        Function to handle the turn events of the battle
        """
        
        ability_choice: int | None  # variable to store the chosen ability of the pokemon
        game_ui.display_battle_details(self) # display battle details

        if self.attacker.is_bot == True:
            time.sleep(2)
            ability_choice = self.random_ability()
            print(ability_choice)
        else:
            # prompt user for ability choice
            ability_choice: int | None = utils.validate_input("Enter ability id")

            # ability checker 
            if ability_choice == None:
                return self.handle_turn()

        # find the ability on the on the pokemon's ability array
        ability = self.find_ability(ability_choice)

        utils.clear_terminal()

        # simple ability validation
        if ability != None:
            # if ability hits perform damage calculation,
            # else perform no damage calculation
            if ability.does_move_hit():
                damage = self.calculate_damage(ability)  # call calculate damage

                # call is_critical from ability class to determine crit change
                is_critical: bool = ability.is_critical()

                # if ability is critical multiple damage by 2
                if is_critical:
                    damage *= 2

                # deduct defender pokemon's hp from the damage
                self.defender.pokemon.hp -= damage

                # display battle ui
                game_ui.display_battle_log(self, ability.name, damage, is_critical)
            else:
                game_ui.display_battle_log(self, ability.name, 0, False, True)


    def check_fainted(self) -> bool:
        """
        Function to check if defender pokemon has fainted
        """
        is_fainted: bool = False

        # check if defender's pokemon hp is less than or equal to 0,
        # then set is_fainted to true meaning that the defender pokemon looses
        if self.defender.pokemon.hp <= 0:
            is_fainted = True

        return is_fainted


    def start(self):
        """
        Function to initialize the battle sequence
        """
        
        self.determine_first() # set first attacker pokemon 
        playing: bool = True  # variable to flag playing state

        game_ui.display_header() # display game header
        
        if self.player2.is_bot :
            game_ui.display_trainer_challenge(self.player2)
        
        # infinite loop for the battle sequence
        while playing == True:
            self.handle_turn()

            # determine if defender pokemon has fainted,
            # else continue the sequence by swapping attacker and defender
            if self.check_fainted():
                playing = False
            else:
                self.attacker, self.defender = self.defender, self.attacker

        game_ui.end_results(self)

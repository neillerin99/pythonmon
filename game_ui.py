"""
This module handles the battle featuire UI
"""

__author__ = "NEIL EDRIANE LERIN"

from colorama import Fore
from utils import format_color, format_ability_color, format_hp

MENU_WIDTH = 60


def display_header():
    """Display the inital header"""

    print(format_color("=" * MENU_WIDTH, Fore.YELLOW))
    print(format_color("POKEMON BATTLE!".center(MENU_WIDTH), Fore.YELLOW))
    print(format_color("=" * MENU_WIDTH, Fore.YELLOW))


# NOTE: I have remove the type safety here because python will result in a circular import error (battle: Battle)
def display_battle_details(battle):
    """Displas the trainer ui component which shows player and abilities details"""

    # printing of trainer names
    print()
    left = f"{battle.player1.name}'s {battle.player1.pokemon.name.upper()}"
    right = f"{battle.player2.name}'s {battle.player2.pokemon.name.upper()}"
    print(left + right.rjust(MENU_WIDTH - len(left)))

    # printing of pokemon HP's
    hp_left = format_hp(battle.player1.pokemon)
    hp_right = format_hp(battle.player2.pokemon)
    
    # use plain text for length calculation to avoid escape code issues
    plain_left = f"HP: {battle.player1.pokemon.hp}/{battle.player1.pokemon.max_hp}"

    print(hp_left + hp_right.rjust(MENU_WIDTH - len(plain_left)))
    print()

    # printing of pokemon's abilities
    print(format_color("-" * MENU_WIDTH, Fore.YELLOW))
    print()
    print(format_color(f"Trainer {battle.attacker.name}'s turn!", Fore.BLUE))
    print(format_color(f"What will {battle.attacker.pokemon.name.upper()} do?", Fore.BLUE))
    print()
    
    # dsplay pokemon ability details
    for ability in battle.attacker.pokemon.abilities:
        name = f"{ability.index} - {format_ability_color(ability)}"
        stats = f"(DMG: {ability.damage} | ACC: {ability.accuracy}% | CRIT: {ability.critical}%)"
        print(f"{name.ljust(30)}{stats}")

    print()
    print(format_color("-" * MENU_WIDTH, Fore.YELLOW))


# NOTE: I have remove the type safety here because python will result in a circular import error (battle: Battle)
def display_battle_log(
    battle,
    ability: str,
    damage: float,
    is_critical: bool = False,
    ability_miss: bool = False,
):
    """
    This function prints the UI of the battle log
    """

    print(format_color("-" * MENU_WIDTH, Fore.YELLOW))
    print(format_color(f"{battle.attacker.pokemon.name.upper()} used {ability}", Fore.WHITE))

    # dynamically print crit indicator when is_critical is true
    if is_critical:
        print(format_color("Critical hit!", Fore.YELLOW))

    # dynamically condition print if ability misses
    if not ability_miss:
        print(format_color(f"{battle.defender.pokemon.name.upper()} took {damage} damage!", Fore.RED))
    else:
        print(format_color("But it missed!", Fore.LIGHTBLACK_EX))

    print(format_color("-" * MENU_WIDTH, Fore.YELLOW))


# NOTE: I have remove the type safety here because python will result in a circular import error (battle: Battle)
def end_results(battle):
    """
    Function to display the winner of the game
    """
    
    print()
    print(format_color(f"{battle.defender.pokemon.name.upper()} fainted!", Fore.RED))
    print(format_color(f"Trainer {battle.attacker.name.upper()} and {battle.attacker.pokemon.name.upper()} won!", Fore.GREEN))
    print()

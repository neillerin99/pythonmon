"""
This module handles the battle featuire UI
"""

__author__ = "NEIL EDRIANE LERIN"

MENU_WIDTH = 60


def display_header():
    """Display the inital header"""

    print("=" * MENU_WIDTH)
    print("POKEMON BATTLE!".center(MENU_WIDTH))
    print("=" * MENU_WIDTH)


# NOTE: I have remove the type safety here because python will result in a circular import error (battle: Battle)
def display_battle_details(battle):
    """Displas the trainer ui component which shows player and abilities details"""

    # printing of trainer names
    print()
    left = f"{battle.player1.name}'s {battle.player1.pokemon.name.upper()}"
    right = f"{battle.player2.name}'s {battle.player2.pokemon.name.upper()}"
    print(left + right.rjust(MENU_WIDTH - len(left)))

    # printing of pokemon HP's
    hp_left = f"HP: {battle.player1.pokemon.hp}/{battle.player1.pokemon.max_hp}"
    hp_right = f"HP: {battle.player2.pokemon.hp}/{battle.player2.pokemon.max_hp}"
    print(hp_left + hp_right.rjust(MENU_WIDTH - len(hp_left)))
    print()

    # printing of pokemon's abilities
    print("-" * MENU_WIDTH)
    print()
    print(f"Trainer {battle.attacker.name}'s turn!")
    print(f"What will {battle.attacker.pokemon.name.upper()} do?")

    # dsplay pokemon ability details
    for ability in battle.attacker.pokemon.abilities:
        print(
            f"{ability.index} - {ability.name}   (DMG: {ability.damage} | ACC: {ability.accuracy}% | CRIT: {ability.critical}%)"
        )

    print()
    print("-" * MENU_WIDTH)


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

    print("-" * MENU_WIDTH)
    print(f"{battle.attacker.pokemon.name.upper()} used {ability}")

    # dynamically print crit indicator when is_critical is true
    if is_critical:
        print("Critical hit!")

    # dynamically condition print if ability misses
    if not ability_miss:
        print(f"{battle.defender.pokemon.name.upper()} took {damage} damage!")
    else:
        print("But it missed!")

    print("-" * MENU_WIDTH)


# NOTE: I have remove the type safety here because python will result in a circular import error (battle: Battle)
def end_results(battle):
    """
    Function to display the winner of the game
    """
    
    print()
    print(f"{battle.defender.pokemon.name.upper()} fainted!")
    print(
        f"Trainer {battle.attacker.name.upper()} and {battle.attacker.pokemon.name.upper()} won!"
    )
    print()

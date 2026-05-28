# PythonMon

A turn-based Pokémon battle simulator built with Python. Choose your Pokémon, challenge a friend, and battle it out in the terminal!

## Requirements

- Python 3.12

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd pythonmon
```

2. Run the game

```bash
pip install -r requirements.txt
python main.py
```

No external dependencies required.

## How to Play

1. Enter your trainer name when prompted
2. Choose your Pokémon from the Pokédex by entering its ID
3. Player 2 does the same
4. The Pokémon with the higher speed stat goes first
5. Each turn, choose an ability by entering its ID
6. The battle continues until one Pokémon faints
7. Play again or exit after the battle ends

## Available Pokémon

| ID | Name | Type | HP |
|----|------|------|----|
| 1 | Bulbasaur | Grass | 100 |
| 4 | Charmander | Fire | 100 |
| 7 | Squirtle | Water | 100 |
| 25 | Pikachu | Electric | 100 |

## Battle Mechanics

- **Speed** determines who attacks first
- **Damage** is calculated using the attacker's attack, defender's defense, and ability power
- **Accuracy** determines if a move hits — higher accuracy moves are more reliable
- **Critical hits** deal 1.5x damage and are based on each ability's critical chance
- **Miss** — some moves have a chance to miss entirely

## Features

- Two player local battles
- Pokédex to browse available Pokémon
- Unique abilities per Pokémon with accuracy and critical hit stats
- Typewriter-style text output for a classic RPG feel
- Play again prompt after each battle
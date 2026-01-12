🧙‍♂️ Hero vs. Evil Wizard – OOP Battle Game (Python)
📖 Introduction
Hero vs. Evil Wizard is a mini turn-based battle game built with Python to practice Object-Oriented Programming (OOP) concepts. Players create and control a hero character to battle a powerful Evil Wizard using attacks, special abilities, and healing mechanics.
The project emphasizes inheritance, class interactions, game logic design, and user interaction through a simple menu-driven system.

📚 Table of Contents

Introduction

Learning Objectives

Features

Project Requirements

Character Classes

Installation

Usage

Game Mechanics

Examples

Troubleshooting

Future Enhancements

Contributors

License

🎯 Learning Objectives

Apply OOP principles such as inheritance, methods, and encapsulation

Build an interactive, menu-driven Python program

Design turn-based combat logic

Implement randomness and state-based mechanics (health, shields, evasion)

✨ Features

Four playable character classes

Two unique abilities per character

Turn-based battle system

Randomized attack damage

Healing mechanics with max health limits

Evil Wizard AI with regeneration

Victory and defeat conditions

📋 Project Requirements
✔ Four character classes
✔ Two unique abilities per character
✔ Healing mechanic
✔ Randomized attack damage
✔ Turn-based menu system
✔ Evil Wizard attack & regeneration logic
✔ End-game victory/defeat messages

🧝 Character Classes
⚔️ Warrior
A strong melee fighter with high durability.

Power Strike – Deals bonus damage

Battle Cry – Increases attack power temporarily

🔮 Mage
A magic-based damage dealer.

Fireball – High magic damage

Mana Shield – Reduces incoming damage

🏹 Archer
A fast ranged attacker who relies on agility.

Quick Shot – Fires two arrows in one turn

Evade – Avoids the next incoming attack

🛡️ Paladin
A defensive hero with healing abilities.

Holy Strike – Deals bonus holy damage

Divine Shield – Blocks the next attack completely

⚙️ Installation
Prerequisites

Python 3.8 or higher

No external libraries required

Steps
git clone <your-repository-url>
cd hero-vs-evil-wizard
python main.py

▶️ Usage

Run the Python script.

Choose your character class.

Each turn, select an action:

Attack

Use Special Ability

Heal

View Stats

Defeat the Evil Wizard before your health reaches zero.

🕹️ Game Mechanics
🔁 Turn-Based System

Player acts first

Evil Wizard responds after each player turn

❤️ Healing

Restores health

Cannot exceed maximum HP

🎲 Random Damage

Attacks deal damage within a predefined range

Adds unpredictability to combat

🧙 Evil Wizard Logic

Attacks every turn

Regenerates health automatically

Wins if the player’s HP reaches zero

📌 Example Gameplay Flow
Choose an action:

1. Attack
2. Use Ability
3. Heal
4. View Stats

Outcome Messages

🏆 Victory! – You have defeated the Evil Wizard!

☠️ Defeat! – The Evil Wizard has overwhelmed you.

🛠️ Troubleshooting

Game crashes on input → Ensure valid menu choices are entered

Health exceeds max HP → Verify heal() method caps health

Abilities not triggering → Check method calls and class inheritance

🚀 Future Enhancements (Bonus Ideas)

Additional character classes (Rogue, Necromancer, Berserker)

Advanced Evil Wizard abilities (summoning minions, curses)

Critical hits and status effects

Save/load game progress

Graphical UI (Tkinter or Pygame)

👥 Contributors
Your Name Here

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute for educational purposes.

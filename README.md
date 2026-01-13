## Advanced Python Module Project: Defeat the Evil Wizard

## Overview

Hero vs. Evil Wizard is a mini turn-based battle game built with Python to practice Object-Oriented Programming (OOP) concepts. Players create and control a hero character to battle a powerful Evil Wizard using attacks, special abilities, and healing mechanics.
The project emphasizes inheritance, class interactions, game logic design, and user interaction through a simple menu-driven system.

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Heather-Rutherford/advanced-python-module-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd advanced-python-module-project
   ```

## Running the Application

Run the application using Python:

```bash
python defeat-the-evil-wizard.py
```

## How to Play

### Character Selection

When you start the game, you'll choose from 4 character classes:

1. **Warrior** - High health (140 HP), moderate attack (25 damage)

   - Best for: Beginners, defensive playstyle
   - Special abilities: None

2. **Mage** - Low health (100 HP), high attack (35 damage)

   - Best for: Aggressive playstyle, quick battles
   - Special abilities: None

3. **Archer** - Medium health (120 HP), variable attack (25-35 damage)

   - Best for: Strategic players
   - Special abilities:
     - **Quick Shot**: Attack twice in one turn
     - **Evade**: Dodge the wizard's next attack
   - Can heal: 20 HP per turn

4. **Paladin** - Highest health (160 HP), variable attack (17-27 damage)
   - Best for: Defensive and support playstyle
   - Special abilities:
     - **Holy Strike**: Deal bonus damage (35 total)
     - **Divine Shield**: Block the wizard's next attack
   - Can heal: 25 HP per turn

### Battle System

Each turn, you have 4 options:

1. **Attack** - Deal damage to the Evil Wizard
2. **Use Special Ability** - Use class-specific abilities (Archer/Paladin only)
3. **Heal** - Restore health (Archer/Paladin only)
4. **View Stats** - Check your current health and attack power

### The Evil Wizard

- Health: 150 HP
- Attack: 15 damage per turn
- Special ability: Regenerates 5 HP every turn

### Victory Conditions

- **You win** if you reduce the wizard's health to 0
- **You lose** if your health reaches 0

### Strategy Tips

- The wizard regenerates 5 HP per turn, so deal damage faster than he heals
- Use Archer's Evade or Paladin's Divine Shield to avoid damage during critical moments
- Time your healing to maximize survivability
- Paladin's Holy Strike deals massive damage - use it strategically

## License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute for educational purposes.

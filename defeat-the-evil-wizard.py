import random
from typing import Union

# ============= GAME BALANCE CONSTANTS =============
# Character Stats
WARRIOR_HEALTH = 140
WARRIOR_ATTACK = 25

MAGE_HEALTH = 100
MAGE_ATTACK = 35

ARCHER_HEALTH = 120
ARCHER_ATTACK = 30
ARCHER_DAMAGE_MIN_VARIANCE = 5
ARCHER_DAMAGE_MAX_VARIANCE = 5
ARCHER_HEAL_AMOUNT = 20

PALADIN_HEALTH = 160
PALADIN_ATTACK = 20
PALADIN_DAMAGE_MIN_VARIANCE = 3
PALADIN_DAMAGE_MAX_VARIANCE = 7
PALADIN_HEAL_AMOUNT = 25
PALADIN_HOLY_STRIKE_BONUS = 15

WIZARD_HEALTH = 150
WIZARD_ATTACK = 15
WIZARD_REGEN_AMOUNT = 5
# ================================================

# Base Character class
class Character:
    """Base class for all characters in the game."""
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        """Initialize character with name, health, and attack power."""
        self.name: str = name
        self.health: int = health
        self.attack_power: int = attack_power
        self.max_health: int = health
        self.is_evading: bool = False # Evasion status
        self.is_shielded: bool = False # Divine Shield status
        self.heal_amount: int = 0  # Default heal amount

    def attack(self, opponent: 'Character') -> None:
        """Attack an opponent, reducing their health."""
        if self._check_defenses(opponent):
            return
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self) -> None:
        """Heal the character, restoring health but not exceeding max health."""
        self.health += self.heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {self.heal_amount} health! Current health: {self.health}")

    def _check_defenses(self, opponent: 'Character') -> bool:
        """Check if opponent has active defenses and handle them."""
        if opponent.is_evading:
            print(f"{opponent.name} evaded the attack!")
            opponent.is_evading = False
            return True
        if opponent.is_shielded:
            print(f"{opponent.name}'s Divine Shield blocks the attack!")
            opponent.is_shielded = False
            return True
        return False

    def display_stats(self) -> None:
        """Display the character's current stats."""
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

class Warrior(Character):
    """Warrior class with high health and moderate attack power."""
    def __init__(self, name: str) -> None:
        """Initialize Warrior with specific health and attack power."""
        super().__init__(name, health=WARRIOR_HEALTH, attack_power=WARRIOR_ATTACK)

class Mage(Character):
    """Mage class with lower health but high attack power."""
    def __init__(self, name: str) -> None:
        """Initialize Mage with specific health and attack power."""
        super().__init__(name, health=MAGE_HEALTH, attack_power=MAGE_ATTACK)

class EvilWizard(Character):
    """Evil Wizard class with regeneration ability."""
    def __init__(self, name: str) -> None:
        """Initialize Evil Wizard with specific health and attack power."""
        super().__init__(name, health=WIZARD_HEALTH, attack_power=WIZARD_ATTACK)

    def regenerate(self) -> None:
        """Regenerate health each turn."""
        self.health += WIZARD_REGEN_AMOUNT
        print(f"{self.name} regenerates {WIZARD_REGEN_AMOUNT} health! Current health: {self.health}")

class Archer(Character):
    """Archer: A ranged attacker with abilities to shoot arrows and evade attacks."""
    def __init__(self, name: str) -> None:
        """Initialize Archer with specific health and attack power."""
        super().__init__(name, health=ARCHER_HEALTH, attack_power=ARCHER_ATTACK)
        self.heal_amount = ARCHER_HEAL_AMOUNT
        
    def attack(self, opponent: 'Character') -> None:
        if self._check_defenses(opponent):
            return
        damage = random.randint(self.attack_power - ARCHER_DAMAGE_MIN_VARIANCE, self.attack_power + ARCHER_DAMAGE_MAX_VARIANCE)
        opponent.health -= damage
        print(f"{self.name} shoots an arrow at {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"Opponent {opponent.name} has been defeated!")
        
    def quick_shot(self, opponent: 'Character') -> None:
        """Perform a quick shot that hits twice."""
        self.attack(opponent)
        if opponent.health > 0:
            self.attack(opponent)
            
    def evade(self) -> None:
        """Evade the next attack."""
        self.is_evading = True
        print(f"{self.name} takes an evasive stance, ready to dodge the next attack!")
        
class Paladin(Character):
    """Paladin: A defensive hero who can heal and shield against attacks."""
    def __init__(self, name: str) -> None:
        """Initialize Paladin with specific health and attack power."""
        super().__init__(name, health=PALADIN_HEALTH, attack_power=PALADIN_ATTACK)
        self.heal_amount = PALADIN_HEAL_AMOUNT
        
    def attack(self, opponent: 'Character') -> None:
        if self._check_defenses(opponent):
            return
        damage = random.randint(self.attack_power - PALADIN_DAMAGE_MIN_VARIANCE, self.attack_power + PALADIN_DAMAGE_MAX_VARIANCE)
        opponent.health -= damage
        print(f"{self.name} strikes {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"Opponent {opponent.name} has been defeated!")
            
    def holy_strike(self, opponent: 'Character') -> None:
        """Perform a holy strike that deals bonus damage."""
        if self._check_defenses(opponent):
            return
        bonus_damage = PALADIN_HOLY_STRIKE_BONUS
        total_damage = self.attack_power + bonus_damage
        opponent.health -= total_damage
        print(f"{self.name} performs a Holy Strike on {opponent.name} for {total_damage} damage!")
        if opponent.health <= 0:
            print(f"Opponent {opponent.name} has been defeated!")
    
    def divine_shield(self) -> None:
        """Activate Divine Shield to block the next attack."""
        self.is_shielded = True
        print(f"{self.name} raises a Divine Shield, ready to block the next attack!")

def create_character() -> Union[Warrior, Mage, Archer, Paladin]:
    """Create a character with input validation."""
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    # Validate class choice
    while True:
        class_choice = input("Enter the number of your class choice: ").strip()
        if class_choice in ['1', '2', '3', '4']:
            break
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
    
    # Validate name
    while True:
        name = input("Enter your character's name: ").strip()
        if name:  # Check if name is not empty
            break
        print("Name cannot be empty. Please enter a valid name.")

    # Return the chosen character class instance
    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    else:  # class_choice == '4'
        return Paladin(name)

def battle(player: Character, wizard: EvilWizard) -> None:
    """Main battle loop between player and evil wizard.
    
    Args:
        player: The player's chosen character
        wizard: The evil wizard opponent
    """
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ").strip()

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue  # Don't consume the turn, ask again

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                print("\nSpecial Abilities:")
                print("1. Quick Shot")
                print("2. Evade")
                ability_choice = input("Choose ability: ").strip()
                if ability_choice not in ['1', '2']:
                    print("Invalid ability. Please enter 1 or 2.")
                    continue  # Don't consume the turn
                if ability_choice == '1':
                    player.quick_shot(wizard)
                else:  # ability_choice == '2'
                    player.evade()
            elif isinstance(player, Paladin):
                print("\nSpecial Abilities:")
                print("1. Holy Strike")
                print("2. Divine Shield")
                ability_choice = input("Choose ability: ").strip()
                if ability_choice not in ['1', '2']:
                    print("Invalid ability. Please enter 1 or 2.")
                    continue  # Don't consume the turn
                if ability_choice == '1':
                    player.holy_strike(wizard)
                else:  # ability_choice == '2'
                    player.divine_shield()
            else:
                print("No special ability available for your class yet.")
        elif choice == '3':
            if player.heal_amount > 0:
                player.heal()
            else:
                print("Your class cannot heal.")
        elif choice == '4':
            player.display_stats()

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main() -> None:
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()

# Base Character class
class Character:
    # Base class for all characters in the game.
    def __init__(self, name, health, attack_power):
        """Initialize character with name, health, and attack power."""
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        """Attack an opponent, reducing their health."""
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        """Display the character's current stats."""
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    # Warrior class with high health and moderate attack power.
    def __init__(self, name):
        """Initialize Warrior with specific health and attack power."""
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    # Mage class with lower health but high attack power.
    def __init__(self, name):
        """Initialize Mage with specific health and attack power."""
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    # Evil Wizard class with regeneration ability.
    def __init__(self, name):
        """Initialize Evil Wizard with specific health and attack power."""
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        """Regenerate health each turn."""
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    # Archer: A ranged attacker with abilities to shoot arrows and evade attacks.
    def __init__(self, name):
        """Initialize Archer with specific health and attack power."""
        super().__init__(name, health=120, attack_power=30)
        self.is_evading = False
        
    # Modify the attack() method to deal random damage within a range.
    def attack(self, opponent):
        import random
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} shoots an arrow at {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"Opponent {opponent.name} has been defeated!")
        
    # "Quick Shot" (double arrow attack) 
    def quick_shot(self, opponent):
        """Perform a quick shot that hits twice."""
        self.attack(opponent)
        if opponent.health > 0:
            self.attack(opponent)
            
    # "Evade" (dodge the next attack).
    def evade(self):
        """Evade the next attack."""
        self.is_evading = True
        print(f"{self.name} takes an evasive stance, ready to dodge the next attack!")
        
    # Implement a heal() method that restores health but does not exceed the maximum.
    def heal(self):
        """Heal the Archer, restoring health but not exceeding max health."""
        heal_amount = 20
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")
        
# Create Paladin class 
class Paladin(Character):
    # Paladin: A defensive hero who can heal and shield against attacks.
    def __init__(self, name):
        """Initialize Paladin with specific health and attack power."""
        super().__init__(name, health=160, attack_power=20)
        self.is_shielded = False
        
    # Modify the attack() method to deal random damage within a range.
    def attack(self, opponent):
        import random
        damage = random.randint(self.attack_power - 3, self.attack_power + 7)
        opponent.health -= damage
        print(f"{self.name} strikes {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"Opponent {opponent.name} has been defeated!")
            
    # "Holy Strike" (bonus damage) 
    def holy_strike(self, opponent):
        """Perform a holy strike that deals bonus damage."""
        bonus_damage = 15
        total_damage = self.attack_power + bonus_damage
        opponent.health -= total_damage
        print(f"{self.name} performs a Holy Strike on {opponent.name} for {total_damage} damage!")
        if opponent.health <= 0:
            print(f"Opponent {opponent.name} has been defeated!")
    
    # "Divine Shield" (blocks the next attack).
    def divine_shield(self):
        """Activate Divine Shield to block the next attack."""
        self.is_shielded = True
        print(f"{self.name} raises a Divine Shield, ready to block the next attack!")
    
    # Implement a heal() method that restores health but does not exceed the maximum.
    def heal(self):
        """Heal the Paladin, restoring health but not exceeding max health."""
        heal_amount = 25
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

def create_character():
    # Function to create a character based on user choice.
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                print("\nSpecial Abilities:")
                print("1. Quick Shot")
                print("2. Evade")
                ability_choice = input("Choose ability: ")
                if ability_choice == '1':
                    player.quick_shot(wizard)
                elif ability_choice == '2':
                    player.evade()
                else:
                    print("Invalid ability choice.")
            elif isinstance(player, Paladin):
                print("\nSpecial Abilities:")
                print("1. Holy Strike")
                print("2. Divine Shield")
                ability_choice = input("Choose ability: ")
                if ability_choice == '1':
                    player.holy_strike(wizard)
                elif ability_choice == '2':
                    player.divine_shield()
                else:
                    print("Invalid ability choice.")
            else:
                print("No special ability available for your class yet.")
        elif choice == '3': # Implement heal option
            if isinstance(player, Archer) or isinstance(player, Paladin):
                player.heal()
            else:
                print("Your class cannot heal.")
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()

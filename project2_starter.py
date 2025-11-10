"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Tashe Graham]
Date: [11/10/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
        pass
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        
        """
        
        damage = self.strength #Calculates damage based on strength
        target.take_damage(damage) # Apply damage to target
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.health == 0: #If characetr has 0 health, then they are defeated
            print(f"{target.name} has been defeated!")
        
        pass
        
    def take_damage(self, damage):
         
        self.health -= damage # Reduces character health by damage amount
        if self.health < 0: # Makes sure health doesn't go below 0
            self.health = 0 
        
        pass
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"Stats for: {self.name}")
        print(f"-"*25)
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")
        
        pass

class Player(Character): # Inherits from Character class
    """
    
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        #Initializes player character
        super().__init__(name, health, strength, magic) 
        self.character_class = character_class # Stores character_class
        # Player specific attributes
        self.level = 1
        self.experience = 0
        
        pass
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        super().display_stats() #Calls display_stats method
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"EXP: {self.experience}")
        pass

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        # Creates a warrior with suggested stats
        super().__init__(name=name, health=120, strength=15, magic=5, character_class='Warrior')
        
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # AI use-Google Gemini was used to properly override the basic attack
        import random
        bonus = random.randint(1, 5) # Chooses random integer to add
        damage = self.strength + bonus # Extra damage
        target.take_damage(damage)
        print(f"{self.name} aims their bow at {target.name} for {damage} damage!")
        if target.health == 0:
            print(f"{target.name} has been defeated!")

        pass
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = self.strength * 2 # Extra damage
        target.take_damage(damage)
        print(f"{self.name} use POWER STRIKE one {target.name} for {damage} damage")
        
        pass

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        
        """
        # Creates a mage with suggested stats
        super().__init__(name=name, health=80, strength=8, magic=20, character_class='Mage')
        
        pass
        
    def attack(self, target):
        """
        
        """
        damage = self.magic # Uses magic instead of strength
        target.take_damage(damage)
        print(f"{self.name} casts a magic spell at {target.name} for {damage} damage!")
        
        pass
        
    def fireball(self, target):
        """
        Special mage ability 
        """
        # Creates fireball spell
        damage = self.magic + 10 # Extra damage
        target.take_damage(damage)
        print(f"{self.name} throws a FIREBALL at {target.name} for {damage} damage!")
        if target.health == 0:
            print(f"{target.name} has been defeated!")
        
        pass

class Rogue(Player):
    
    
    def __init__(self, name):
        
        # Creates a rogue with suggested stats
        super().__init__(name=name, health=90, strength=12, magic=10, character_class='Rogue')
        #
        pass
        
    def attack(self, target):
        
        # Rogue attack
        base_damage = self.strength
        damage = base_damage
        import random
        if random.randint(1, 10) <= 3: # Adds a chance for critical hit
            damage = base_damage * 2 #Double damage
            print(f"{self.name} attacks {target.name} with a CRITICAL HIT!!")
        target.take_damage(damage)
        print(f"{self.name} shoots {target.name} for {damage} damage!")

        if target.strength == 0:
            print(f"{target.name} has been defeated!")
      
        pass
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        # Sneak attack
        damage = self.strength * 2 #Double damage
        target.take_damage(damage)
        print(f"{self.name} uses SNEAK ATTACK on {target.name} for {damage} damage!")
        if target.strength == 0:
            print(f"{target.name} has been defeated!")
        
        pass

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        
        # Creates a weapon with a name and damage bonus.
        
        # Stores weapon name and damage bonus
        pass
        self.name = name
        self.damage_bonus = damage_bonus
    def display_info(self):
        
        # Outputs weapon name and damage
        print(f"Weapon: {self.name} (Damage: +{self.damage_bonus})")
        pass

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    warrior = Warrior('Joseph Joestar')
    mage = Mage('Jolyne Cujoh')
    rogue = Rogue('Giorno Giovanna')
    
    
    # TODO: Display their stats
    print("\n Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    
    # TODO: Test polymorphism - same method call, different behavior
    print("\n Testing Polymorphism {basic_attack}")
    dummy_target = Character('Target Dummy', 100, 0, 0)
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy: ---")
        character.basic_attack(dummy_target)
        dummy_target.health = 100 # Reset dummy health
    
    
    # TODO: Test special abilities
    print(f"\n Testing Special Abilities:")
    target1 = Character('Enemy1', 50, 0, 0)
    target2 = Character('Enemy2', 50, 0, 0)
    target3 = Character('Enemy3', 50, 0, 0)
    print("\n--- Warrior's Ability ---")
    warrior.power_strike(target1)

    print("\n--- Mage's Ability ---")
    mage.fireball(target2)

    print("\n--- Rogue's Ability ---")
    rogue.sneak_attack(target3)
    
    
    # TODO: Test composition with weapons
    print("\n Testing Weapon Composition:")
    bow = Weapon('Iron Bow', 10)
    spell = Weapon('Magic Spell', 15)
    pistol = Weapon('Steel Pistol', 8)
    bow.display_info()
    spell.display_info()
    pistol.display_info()
    
    # TODO: Test the battle system
    print("\n Testing Batle Systen:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")



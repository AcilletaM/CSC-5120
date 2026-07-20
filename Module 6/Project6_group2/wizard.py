# CSC 5120 Module 6 Project
# Andrew Davis

# Load the Character and Die classes.
from character import Character
from die import Die

class Wizard(Character):
    """Magical wizard.  Can be controlled by the player or AI."""
    def __init__(self, isplayer): # for homework 4 #, aiController:bool):
        super().__init__(isplayer)

        # Wizard-specific dice, the rest come from the Character class
        self.d6 = Die(6)
        self.d12 = Die(12)

        # Wizard uses six d10 to calculate its starting hit points.
        self.maxhitpoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitpoints = self.maxhitpoints
        self.bonechill = False

    def _promptforattack(self) -> int:
        """Ask the player if they wish to use the firebolt, bonechill, or heal."""
        choice = 0
        while choice < 1 or choice > 3:
            choice = int(input("How would you like the Wizard to attack?\n"
                               "1. Firebolt.\n"
                               "2. Bonechill.\n"
                               "3. Heal.\n"
                               "Enter choice: "))

        return choice

    def _chooseaiattack(self) -> int:
        """The AI will determine how the Wizard behaves. 1 for firebolt (60%), 2 for bonechill (25%), and 3 to heal (15%)."""
        roll = self.d20.roll()
        if roll <= 12:
            return 1
        elif roll <= 17:
            return 2
        else:
            return 3

    def _performattack(self,attacktype: int) -> int:
        """Execute the Wizard's attack!"""
        damage = 0

        # 1 = firebolt, needs to roll a 13 or more to hit, can cause up to 12 hp of damage.
        if (attacktype == 1):
            if (self.d20.roll() >= 13):
                damage = self.d12.roll()
                print(f"The Wizard hits with its firebolt for {damage}")
            else:
                print("The Wizard misses with its firebolt")
        # 2 = bonechill, needs to roll a 16 or more to hit, can cause up to 18 hp of damage.
        elif (attacktype == 2):
            if self.bonechill==True:
                self.bonechill = False
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()
                print(f"The Wizard hits with bonechill for {damage}")
            else:
                self.bonechill = True
                print("The Wizard charges bonechill")
        # 3 = heals, can heal up to 6 hp.
        else:
            damage = -1 * self.d6.roll()
            print(f"The Wizard heals for {-1*damage}")

        return damage
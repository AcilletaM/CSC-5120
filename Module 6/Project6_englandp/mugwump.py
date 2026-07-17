# CSC 5120 Module 4 Project
# Paul England
# Instructions
# The goal of the fourth project is to review the concepts we have learned thus far. We will apply the concepts of
# inheritance (also called duck typing) and testing to the Battle Sim example Lab we worked through in class. Your
# project will have several files.
#
# This file contains the refactored Mugwump class definitions.  It contains the constructor, _promptforattack,
# _chooseaiattack, and _performattack methods that are specific to the Mugwump class.  It is based on the mugwump file
# developed in class.

# Load the Character and Die classes.
from character import Character
from die import Die

class Mugwump(Character):
    """Fierce Mugwump looking for a fight.  Can be controlled by the player or AI."""
    winmessages = {
        ("player",   "Warrior"): "You chose the path of evil -- and it paid off. You have vanquished the valiant warrior.  A meal of villagers awaits you.",
        ("player",   "Mugwump"):  "Two mugwumps clashed in the dark and you proved the mightier beast.  You feast on your fallen rival, while the villagers cower in fear, awaiting their fate.",
        ("player",   "Druid"):  "You, a merciless beast, are a force of nature the druids cannot contain.  You feast on druid for lunch, giving thanks their Vegan lifestyle produces such excellent flavor.",
        ("player",   "Salamanda"):  "Two beasts clashed and you were the strongest.  Then you remember salamandas do not taste good.",
        ("player",   "Wizard"):  "They tried to tame the beast with spells and illusions.  Instead, they disappeared into your belly.",
        ("computer", "Warrior"): "You chose to play the monster, but good still triumphed.  Villagers have little to be thankful for but for today, they are thankful to be alive.",
        ("computer", "Mugwump"):  "You chose the way of the monster and met a heinous fate.  No one will remember you or this battle.",
        ("computer", "Druid"):  "Nature is a powerful force and Druids are masters of that force. You have no choice but to leave, with nothing but a handful of locusts to satiate your hunger.",
        ("computer", "Salamanda"):  "You tangled with a salamanda and lost on purpose.  Salamandas do not taste good.",
        ("computer", "Wizard"):  "The powers of this wizard were too much for you.  Magic burns and creates scars you never forget.",
    }

    def __init__(self, isplayer): # for homework 4 #, aiController:bool):
        super().__init__(isplayer)

        # Mugwump-specific dice, the rest come from the Character class
        self.d6 = Die(6)

        # Mugwump uses six d10 to calculate its starting hit points.
        self.maxhitpoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitpoints = self.maxhitpoints

    def _promptforattack(self) -> int:
        """Ask the player if they wish to use the claws, fangs, or heal."""
        choice = 0
        while choice < 1 or choice > 3:
            choice = int(input("How would you like the Mugwump to attack?\n"
                               "1. Razor-sharp claws.\n"
                               "2. Piercing fangs.\n"
                               "3. Lick wounds and heal.\n"
                               "Enter choice: "))

        return choice

    def _chooseaiattack(self) -> int:
        """The AI will determine how the Mugwump behaves. 1 for claws (60%), 2 for fangs (25%), and 3 to heal (15%)."""
        roll = self.d20.roll()
        if roll <= 12:
            return 1
        elif roll <= 17:
            return 2
        else:
            return 3

    def _performattack(self,attacktype: int) -> int:
        """Execute the Mugwump's attack!"""
        damage = 0

        # 1 = claws, needs to roll a 13 or more to hit, can cause up to 12 hp of damage.
        if (attacktype == 1):
            if (self.d20.roll() >= 13):
                damage = self.d6.roll() + self.d6.roll()
                print(f"The Mugwump hits with its claws for {damage}")
            else:
                print("The Mugwump misses with its claws")
        # 2 = fangs, needs to roll a 16 or more to hit, can cause up to 18 hp of damage.
        elif (attacktype == 2):
            if (self.d20.roll() >= 16):
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()
                print(f"The Mugwump hits with its fangs for {damage}")
            else:
                print("The Mugwump misses with its fangs")
        # 3 = heals, can heal up to 6 hp.
        else:
            damage = -1 * self.d6.roll()
            print(f"The Mugwump heals for {-1*damage}")

        return damage
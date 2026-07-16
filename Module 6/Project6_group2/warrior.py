# CSC 5120 Module 4 Project
# Paul England
# Instructions
# The goal of the fourth project is to review the concepts we have learned thus far. We will apply the concepts of
# inheritance (also called duck typing) and testing to the Battle Sim example Lab we worked through in class. Your
# project will have several files.
#
# This file contains the refactored Warrior class definitions.  It contains the constructor, _promptforattack,
# _chooseaiattack, and _performattack methods that are specific to the Warrior class.  It is based on the warrior file
# developed in class.

# Load the Character and Die classes.
from character import Character
from die import Die

class Warrior(Character):
    """Mighty fighter looking for adventure and treasure.  Can be controlled by the player or AI."""

    def __init__(self, isplayer):
        super().__init__(isplayer)

        # Warrior-specific dice, the rest come from the Character class
        self.d8 = Die(8)
        self.d4 = Die(4)

        # Warrior uses four d10 to calculate their starting hit points.
        self.maxhitpoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitpoints = self.maxhitpoints

    def _promptforattack(self) -> int:
        """Ask the player if they wish to use the sword or shield."""
        choice = 0
        while choice != 1 and choice != 2:
            choice = int(input("How would you like the Warrior to attack?\n"
                      "1. Trusty Sword\n"
                      "2. Shield of Light\n"
                      "Enter choice: "))

        return choice

    def _chooseaiattack(self) -> int:
        """Our robot Overlords shall choose an attack. 1 for sword and 2 for shield."""
        roll = self.d20.roll()
        if roll <= 13:
            return 1
        else:
            return 2

    def _performattack(self,attacktype: int) -> int:
        """Execute the warrior's attack!"""
        damage = 0

        # 1 = sword, needs to roll a 12 or more to hit, can cause up to 16 hp of damage.
        if (attacktype == 1):
            if (self.d20.roll() >= 12):
                damage = self.d8.roll() + self.d8.roll()
                print(f"The Warrior hits with the Trusty Sword for {damage}")
            else:
                print("The Warrior swings and misses with the Trusty Sword!")
        # 2 = shield of light, needs to roll a 6 or more to hit, can cause up to 4 hp of damage.
        else:
            if (self.d20.roll() >= 6):
                damage = self.d4.roll()
                print(f"The Warrior hits with the Shield Of Light for {damage}")
            else:
                print("The Warrior misses with the Shield Of Light!")
        return damage
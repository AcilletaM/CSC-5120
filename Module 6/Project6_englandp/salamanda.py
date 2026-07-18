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

class Salamanda(Character):
    """Slimy Salamanda looking to slither"""

    winmessages = {
        ("player",   "Warrior"): "The salamanda slurped the warrior for breakfast, eessssuuurrrpppp",
        ("player",   "Mugwump"):  "another one bites the dust, and this time its the mugwump and not brian may",
        ("player",   "Druid"):  "Druid, more like Sous vide, because the slamanda cooked him good in this battle",
        ("player",   "Salamanda"):  "Two slithery slimes, there can only be one!",
        ("player",   "Wizard"):  "I cast you away with my slimy tail, e-slimy-amous!!!",
        ("computer", "Warrior"): "some consider AI warriors to be data centers, too bad they don't work when everything is covered in slime",
        ("computer", "Mugwump"):  "the digital mugwump was overtaken by the salamanda, wump wump wumpppppp",
        ("computer", "Druid"):  "the salamanda thought the 'Druid' was a 'Droid' and deflected the laser with with his lightsaber like tail for win. ",
        ("computer", "Salamanda"):  "Real slime is always better than digital slime, the real slime wins",
        ("computer", "Wizard"):  "The digital wizard tried to win with a spell made of ones and zeros, but it was not very effective!",
    }


    def __init__(self, isplayer): # for homework 4 #, aiController:bool):
        super().__init__(isplayer)

        # slamanda-specific dice, the rest come from the Character class
        self.d6 = Die(6)

        # Salamanda uses six d10 to calculate its starting hit points.
        self.maxhitpoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitpoints = self.maxhitpoints
        self.heal = False

    def _promptforattack(self) -> int:
        """Ask the player if they wish to use the tail, slime ball, or heal."""
        choice = 0
        while choice < 1 or choice > 3:
            choice = int(input("How would you like the Salamanda to attack?\n"
                               "1. 360 + 180 Reverse Tail Swipe\n"
                               "2. Gooey Slime Ball \n"
                               "3. Shed and then Eat Skin to heal (must select twice in order to do full heal)\n"
                               "Enter choice: "))

        return choice

    def _chooseaiattack(self) -> int:
        """The AI will determine how the Mugwump behaves. 1 for tail (33%), 2 for gooey slime ball (33%), and 3 to heal (33%)."""
        roll = self.d20.roll()
        if roll <= 7:
            return 1
        elif roll <= 13:
            return 2
        else:
            return 3

    def _performattack(self,attacktype: int) -> int:
        """Execute the Salamandas attack!"""
        damage = 0

        # 1 = tail, due to rotation has a large miss percentage (66%)
        # however if it hits 33% will cause guranteed 20 damage
        if (attacktype == 1):
            if (self.d20.roll() <= 7):
                damage = 20
                print(f"The Salamanda rotates 540 degrees and smacks with large tail for {damage}")
            else:
                print("The Salamanda misses and is dizzy")

        # 2 = gooey ball, needs to roll a 5 or more to hit, can cause up to 12 hp of damage.
        elif (attacktype == 2):
            if (self.d20.roll() >= 5):
                damage = self.d6.roll() + self.d6.roll()
                print(f"The Salamanda hits with its Gooey slime ball for {damage}")
            else:
                print("The Salamanda misses with its Gooey slime ball")

        # 3 = heals, takes two turns to do a full heal, can
        else:

            if(self.heal == False):
                self.heal = True
                print(f"The Salamanda sheds skin...")
            else:
                self.heal = False
                #perform a full heal
                damage = -1 * (self.maxhitpoints - self.hitpoints)
                print(f"The Salamanda eats skin for {-1*damage}")


        return damage
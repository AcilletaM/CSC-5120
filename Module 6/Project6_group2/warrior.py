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
    winmessages = {
        ("player",   "Warrior"): "Two valiant warriors, fighting for pride instead of principle.  Still you prevailed. Your opponent flees, forever branded a coward.",
        ("player",   "Mugwump"):  "You, the valiant Warrior, have slain the evil Mugwump! The citizens cheer and lay out a feast -- the kingdom is saved (again)!",
        ("player",   "Druid"):  "You, a valiant warrior, fighting for people not nature.  You have easily overcome the feeble druid. Your opponent runs away, cursing your name.",
        ("player",   "Salamanda"):  "All manner of foul beasts roam this world.  Thank the old gods you are there to protect the weak and powerless.",
        ("player",   "Wizard"):  "Everybody wants to be powerful but true power doesn't come from books, it comes from hard training and discipline.  You have put in the work and it shows.",
        ("computer", "Warrior"): "Two valiant warriors turned on each other, and you broke.  You slink away branded a coward while the other claims a pyrrhic victory.",
        ("computer", "Mugwump"):  "You chose to play the monster, but good still triumphed.  Villagers have little to be thankful for, but for today, they are thankful to be alive.",
        ("computer", "Druid"):  "Nature is being destroyed by the thoughtless villagers, but their warrior has protected them. You must return to the woods to meditate with nature.",
        ("computer", "Salamanda"):  "You thought this village would provide an easy meal.  Their warrior dissuaded you from that idea.",
        ("computer", "Wizard"):  "The warrior has bested you, mocking your feeble defense as they smack you on the back of the head with their sword.  Pathetic.",
    }

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
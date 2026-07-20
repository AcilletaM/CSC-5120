# CSC 5120 Module 6 Project
# Paul England
# Instructions
# The goal of the sixth project is to review the concepts we have learned thus far. We will apply the concepts of
# inheritance (also called duck typing) and testing to the Battle Sim example Lab we worked through in class. Your
# project will have several files.
#
# This file contains the refactored Warrior class definitions.  It contains the constructor, _promptforattack,
# _chooseaiattack, and _performattack methods that are specific to the Warrior class.  It is based on the warrior file
# developed in class.

# Load the Character and Die classes.
from character import Character
from die import Die

class Druid(Character):
    """Timid person of nature looking to restore balance to a chaotic world.  Can be controlled by the player or AI."""

    winmessages = {
        ("player",   "Warrior"): "Wisdom has triumphed over the blade.  Bards will sing songs of this day.",
        ("player",   "Mugwump"):  "You have confronted the wildling and it is the one who ran off in fear.  The others will look upon you with wonder.",
        ("player",   "Druid"):  "Two spiritual Druids, clashing to show who loves their goddess most.  You have earned her blessing. Your opponent breaks down in tears, spirit broken.",
        ("player",   "Salamanda"):  "You, a man of nature, have exerted your influence over the lowly salamanda.  You watch as it slithers off into the underbrush.",
        ("player",   "Wizard"):  "True belief can expose those who hope to deceive through simple parlor tricks.  Begone trickster!",
        ("computer", "Warrior"): "On this day it was brains over brawn as the mighty warrior was the smitee.",
        ("computer", "Mugwump"):  "You wanted lunch!  You have no choice but to leave, with nothing but a handful of locusts to satiate your hunger.",
        ("computer", "Druid"):  "Two kindly Druids, instead of helping each other, tried to curry favor more than the other, and you didn't do enough.  Your faith is shaken.",
        ("computer", "Salamanda"):  "A lover of nature has defeated a freak of nature most foul.  Life is hard.",
        ("computer", "Wizard"):  "Magic clashed with belief and belief won out.  Your next trick was making yourself disappear.",
    }

    def __init__(self, isplayer):
        super().__init__(isplayer)


        # Druid-specific dice, the rest come from the Character class
        self.d8 = Die(8)
        self.d6 = Die(6)
        self.d4 = Die(4)

        # Warrior uses three d8 to calculate their starting hit points.
        self.maxhitpoints = self.d8.roll() + self.d8.roll() + self.d8.roll()
        self.hitpoints = self.maxhitpoints

    def _promptforattack(self) -> int:
        """Ask the player if they wish to use the spell, club, or heal."""
        choice = 0
        while choice < 1 or choice > 3:
            choice = int(input("How would you like the Druid to act?\n"
                      "1. Summon a swarm of locusts\n"
                      "2. Swing a club gifted from a kindly oak tree\n"
                      "3. Pray to the goddess of nature and heal\n"
                      "Enter choice: "))

        return choice

    def _chooseaiattack(self) -> int:
        """Our robot Overlords shall choose an attack. 1 for locust spell, 2 for club, and 3 to heal."""
        roll = self.d20.roll()
        if roll > 13:
            return 1
        elif roll > 5:
            return 2
        else:
            return 3

    def _performattack(self,attacktype: int) -> int:
        """Execute the druid's attack!"""
        damage = 0
        attackroll = self.d20.roll()

        # 1 = locust swarm, needs to roll a 10 or more to hit, can cause up to 12 hp of damage unless they roll a 20,
        #     then it causes up to 18 HP of damage.
        if (attacktype == 1):
            if (attackroll == 20):
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()
                print(f"The Druid chants loudly and the sky darkens as thousands of locusts swarm the opponent causing {damage} hp of damage.")
            elif (attackroll >= 10):
                damage = self.d6.roll() + self.d6.roll()
                print(f"The Druid chants softly as the air buzzes with hundreds of locusts, causing {damage} hp of damage.")
            else:
                print("The Druid mumbles and nothing happens.  Everyone is confused.")
        # 2 = club, needs to roll a 8 or more to hit, can cause up to 4 hp of damage, up to 8 hp on a natural 20.
        elif (attacktype == 2):
            if (attackroll == 20):
                damage = self.d4.roll() + self.d4.roll()
                print(f"The Druid takes a mighty swing with the club and hits for {damage} hp of damage.")
            elif (attackroll >= 10):
                damage = self.d4.roll()
                print(f"The Druid strikes with the club and hits for {damage} hp of damage.")
            else:
                print("The Druid swings and misses with the club!")
        # 3 = heal, needs to roll a 15 or more to heal, can heal up to 6 hp, up to 12 hp on a natural 20.
        else:
            if (attackroll == 20):
                damage = -1 * (self.d6.roll() + self.d6.roll())
                print(f"The Druid closes their eyes, prays, and is rewarded by the goddess of nature, healing by {-1*damage} HPs")
            elif (attackroll >= 12):
                damage = -1 * self.d6.roll()
                print(f"The Druid drinks a potion and heals for {-1*damage}")
            else:
                print("The Druid rubs a salve on their wounds to ease the pain, but it doesn't work!")
        return damage
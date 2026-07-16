# CSC 5120 Module 4 Project
# Paul England
# Instructions
# The goal of the fourth project is to review the concepts we have learned thus far. We will apply the concepts of
# inheritance (also called duck typing) and testing to the Battle Sim example Lab we worked through in class. Your
# project will have several files.
#
# This file contains the definitions of the abstract character class.  It contains the constructor, takedamage, attack,
# _promptforattack, _chooseaiattack, and _performattack methods.  It is based on the warrior and mugwump files provided
# in class.

# We are using an abstract base method for this exercise.  Load the Die class as the character classes need it.
from abc import ABC, abstractmethod
from die import Die

class Character(ABC):
    """Abstract base class shared by every combatant."""

    def __init__(self, isplayer, name="Hal 9000"):
        self.isplayer = isplayer
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.maxhitpoints = 0
        self.hitpoints = 0
        self.name = name

    def takedamage(self, amount):
        """Apply damage from the attack or the healing.  Either the attack takes the HP to 0 or the character is healed up to the max HP."""
        if (self.hitpoints >= amount):
            self.hitpoints -= amount
            if (self.hitpoints > self.maxhitpoints):  # healed past full
                self.hitpoints = self.maxhitpoints
        else:
            self.hitpoints = 0

    def attack(self) -> int:
        """Prompt the user for an attack choice or let the AI choose and then perform the attack chosen."""
        if self.isplayer:
            attacktype = self._promptforattack()
        else:
            attacktype = self._chooseaiattack()
        return self._performattack(attacktype)

    @abstractmethod
    def _promptforattack(self) -> int:
        """Ask the human player which attack to use and return its number."""
        ...

    @abstractmethod
    def _chooseaiattack(self) -> int:
        """We have reached the Singularity and AI is now in charge.  It will choose opponents doom."""
        ...

    @abstractmethod
    def _performattack(self, attacktype) -> int:
        """Roll for the chosen attack and return the damage or healing dealt."""
        ...

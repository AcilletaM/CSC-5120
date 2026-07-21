# CSC 5120 Module 6 Project
# Paul England
# Andrew Davis
# James Splingaire
#
# Instructions
# The goal of the sixth project is to modify your Mugwump project from Module 4 with a group, using a Git repository to collaborate on the code.
#
# This file contains the definitions of the die class.  It contains the constructor, roll, and getCurrentValue
# methods.  It is based on the file provided in class with tweaks.

# Load random for the random number generator used to simulate a roll.
from random import Random

class Die:
    """Simulates a die with an user inputted number of sides."""

    def __init__(self, numsides):
        self.__numsides = numsides
        self.__currentvalue = 0
        self.__generator = Random()

    def roll(self):
        """Simulates a die roll by returning a random integer between 1 and the user inputted number of sides."""
        self.__currentvalue = self.__generator.randint(1, self.__numsides)
        return self.__currentvalue

    def getcurrentvalue(self):
        """Returns the last value of the die or 0 if never rolled."""
        return self.__currentvalue





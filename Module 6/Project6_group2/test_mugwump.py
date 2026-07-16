# CSC 5120 Module 4 Project
# Paul England
# Instructions
# The goal of the fourth project is to review the concepts we have learned thus far. We will apply the concepts of
# inheritance (also called duck typing) and testing to the Battle Sim example Lab we worked through in class. Your
# project will have several files.
#
# This file contains the tests of the Mugwump and Character classes.  We are testing:
# - A new mugwump is created.
# - A mugwump is a Character.
# - The starting hp of a mugwump is in the expected range.
# - The damage caused by a mugwump attack is in the expected range.
# - The "AI" determins a valid attack for a mugwump attack.
# - The damage taken by a mugwump attack is in the expected range.

# Load pytest, Mugwump, and Character.
import pytest
from mugwump import Mugwump
from character import Character


@pytest.fixture
def mugwump():
    """Provide a fresh computer-controlled Mugwump for each test (fixture)."""
    return Mugwump(False, "test")


def testmugwumpisacharacter(mugwump):
    """A Mugwump is a Character through inheritance (fixture)."""
    assert isinstance(mugwump, Character)


def teststartinghitpointsinrange(mugwump):
    """Six d10 give a Mugwump between 6 and 60 starting hit points (fixture)."""
    assert 6 <= mugwump.maxhitpoints <= 60
    assert mugwump.hitpoints == mugwump.maxhitpoints


def testattackdamageinrange(mugwump):
    """Across many attacks, damage stays within the -6..18 range (fixture)."""
    for _ in range(1000):
        damage = mugwump.attack()
        assert -6 <= damage <= 18


def testaireturnsvalidattacktype(mugwump):
    """The AI only ever chooses attack types 1, 2, or 3 (fixture)."""
    for _ in range(1000):
        # _chooseaiattack is a protected hook; a test may reach past the public API
        assert mugwump._chooseaiattack() in (1, 2, 3)


@pytest.mark.parametrize(
    "starthp, maxhp, amount, expected",
    [
        (50, 60, 10, 40),    # ordinary hit
        (5, 60, 10, 0),      # overkill is clamped to 0
        (0, 60, 5, 0),       # already down stays down
        (30, 60, -10, 40),   # negative amount heals
        (55, 60, -10, 60),   # healing cannot exceed the maximum
    ],
)
def testtakedamage(mugwump, starthp, maxhp, amount, expected):
    """takedamage handles hits, overkill, and capped healing (fixture + parameterize)."""
    mugwump.maxhitpoints = maxhp
    mugwump.hitpoints = starthp
    mugwump.takedamage(amount)
    assert mugwump.hitpoints == expected

# CSC 5120 Module 6 Project
# Paul England
# Andrew Davis
# James Splingaire
#
# Instructions
# The goal of the sixth project is modify your Mugwump project from Module 4 with a group, using a Git repository to collaborate on the code.
#
# This file contains the tests of the Mugwump and Character classes.  We are testing:
# - A new mugwump is created.
# - A mugwump is a Character.
# - The starting hp of a mugwump is in the expected range.
# - The damage caused by a mugwump attack is in the expected range.
# - The "AI" determines a valid attack for a mugwump attack.
# - The damage taken by a mugwump attack is in the expected range.
# - There are win messages for every match-up combination.
# - The Defeats method returns the valide win message.

# Load pytest, Mugwump, Salamanda, and Character.
import pytest
from mugwump import Mugwump
from salamanda import Salamanda
from character import Character


@pytest.fixture
def mugwump():
    """Provide a fresh computer-controlled Mugwump for each test (fixture)."""
    return Mugwump(False)


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


def testwinmessagesexist():
    """Validate a win message exists for each player/computer/opponent class combinations."""
    for controller in ("player", "computer"):
        for opponent in ("Warrior", "Mugwump", "Druid", "Salamanda", "Wizard"):
            assert (controller, opponent) in Mugwump.winmessages

def testdefeatsmessages(mugwump):
    """Defeats finds the appropriate message for the matchup (fixture)."""
    loser = Mugwump(False)
    assert mugwump.defeats(loser, "player") == Mugwump.winmessages[("player", "Mugwump")]
    assert mugwump.defeats(loser, "computer") == Mugwump.winmessages[("computer", "Mugwump")]
    loser = Salamanda(False)
    assert mugwump.defeats(loser, "player") == Mugwump.winmessages[("player", "Salamanda")]
    assert mugwump.defeats(loser, "computer") == Mugwump.winmessages[("computer", "Salamanda")]

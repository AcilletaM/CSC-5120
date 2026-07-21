# CSC 5120 Module 6 Project
# Paul England
# Andrew Davis
# James Splingaire
#
# Instructions
# The goal of the sixth project is to modify your Mugwump project from Module 4 with a group, using a Git repository to collaborate on the code.
#
# This file contains the tests of the Warrior and Character classes.  We are testing:
# - A new warrior is created.
# - A warrior is a Character.
# - The starting hp of a warrior is in the expected range.
# - The damage caused by a warrior attack is in the expected range.
# - The "AI" determines a valid attack for a warrior attack.
# - The damage taken by a warrior attack is in the expected range.
# - There are win messages for every match-up combination.
# - The Defeats method returns the valide win message.

# Load pytest, Warrior, Salamanda, and Character.
import pytest
from warrior import Warrior
from salamanda import Salamanda
from character import Character


@pytest.fixture
def warrior():
    """Provide a fresh computer-controlled Warrior for each test (fixture)."""
    return Warrior(False)


def testwarriorisacharacter(warrior):
    """A Warrior is a Character through inheritance (fixture)."""
    assert isinstance(warrior, Character)


def teststartinghitpointsinrange(warrior):
    """Four d10 give a Warrior between 4 and 40 starting hit points (fixture)."""
    assert 4 <= warrior.maxhitpoints <= 40
    assert warrior.hitpoints == warrior.maxhitpoints


def testattackdamageinrange(warrior):
    """Across many attacks, damage stays within the -6..16 range (fixture)."""
    for _ in range(1000):
        damage = warrior.attack()
        assert 0 <= damage <= 16


def testaireturnsvalidattacktype(warrior):
    """The AI only ever chooses attack types 1, or 2 (fixture)."""
    for _ in range(1000):
        # _chooseaiattack is a protected hook; a test may reach past the public API
        assert warrior._chooseaiattack() in (1, 2)


@pytest.mark.parametrize(
    "starthp, maxhp, amount, expected",
    [
        (30, 40, 10, 20),    # ordinary hit
        (5, 40, 10, 0),      # overkill is clamped to 0
        (0, 40, 5, 0),       # already down stays down
    ],
)
def testtakedamage(warrior, starthp, maxhp, amount, expected):
    """takedamage handles hits, overkill, and capped healing (fixture + parameterize)."""
    warrior.maxhitpoints = maxhp
    warrior.hitpoints = starthp
    warrior.takedamage(amount)
    assert warrior.hitpoints == expected


def testwinmessagesexist():
    """Validate a win message exists for each player/computer/opponent class combinations."""
    for controller in ("player", "computer"):
        for opponent in ("Warrior", "Mugwump", "Druid", "Salamanda", "Wizard"):
            assert (controller, opponent) in Warrior.winmessages

def testdefeatsmessages(warrior):
    """Defeats finds the appropriate message for the matchup (fixture)."""
    loser = Warrior(False)
    assert warrior.defeats(loser, "player") == Warrior.winmessages[("player", "Warrior")]
    assert warrior.defeats(loser, "computer") == Warrior.winmessages[("computer", "Warrior")]
    loser = Salamanda(False)
    assert warrior.defeats(loser, "player") == Warrior.winmessages[("player", "Salamanda")]
    assert warrior.defeats(loser, "computer") == Warrior.winmessages[("computer", "Salamanda")]

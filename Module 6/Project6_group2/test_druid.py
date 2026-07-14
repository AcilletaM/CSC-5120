# CSC 5120 Module 4 Project
# Paul England
# Instructions
# The goal of the fourth project is to review the concepts we have learned thus far. We will apply the concepts of
# inheritance (also called duck typing) and testing to the Battle Sim example Lab we worked through in class. Your
# project will have several files.
#
# This file contains the tests of the Druid and Character classes.  We are testing:
# - A new druid is created.
# - A druid is a Character.
# - The starting hp of a druid is in the expected range.
# - The damage caused by a druid attack is in the expected range.
# - The "AI" determins a valid attack for a druid attack.
# - The damage taken by a druid attack is in the expected range.

# Load pytest, Druid, and Character.
import pytest
from druid import Druid
from character import Character


@pytest.fixture
def druid():
    """Provide a fresh computer-controlled Druid for each test (fixture)."""
    return Druid(False)


def testdruidisacharacter(druid):
    """A Druid is a Character through inheritance (fixture)."""
    assert isinstance(druid, Character)


def teststartinghitpointsinrange(druid):
    """Three d8 give a Druid between 3 and 24 starting hit points (fixture)."""
    assert 3 <= druid.maxhitpoints <= 24
    assert druid.hitpoints == druid.maxhitpoints


def testattackdamageinrange(druid):
    """Across many attacks, damage stays within the -12..18 range (fixture)."""
    for _ in range(1000):
        damage = druid.attack()
        assert -12 <= damage <= 18


def testaireturnsvalidattacktype(druid):
    """The AI only ever chooses attack types 1, 2, or 3 (fixture)."""
    for _ in range(1000):
        # _chooseaiattack is a protected hook; a test may reach past the public API
        assert druid._chooseaiattack() in (1, 2, 3)


@pytest.mark.parametrize(
    "starthp, maxhp, amount, expected",
    [
        (20, 24, 10, 10),    # ordinary hit
        (5, 24, 10, 0),      # overkill is clamped to 0
        (0, 24, 5, 0),       # already down stays down
        (10, 24, -6, 16),   # negative amount heals
        (20, 24, -12, 24),   # healing cannot exceed the maximum
    ],
)
def testtakedamage(druid, starthp, maxhp, amount, expected):
    """takedamage handles hits, overkill, and capped healing (fixture + parameterize)."""
    druid.maxhitpoints = maxhp
    druid.hitpoints = starthp
    druid.takedamage(amount)
    assert druid.hitpoints == expected

# CSC 5120 Module 4 Project
# Paul England
# Instructions
# The goal of the fourth project is to review the concepts we have learned thus far. We will apply the concepts of
# inheritance (also called duck typing) and testing to the Battle Sim example Lab we worked through in class. Your
# project will have several files.
#
# This file contains the tests of the die class.  We are testing:
# - A new die value is 0 if not rolled.
# - A die value is in the expected range.
# - A die value is updated each time the die is rolled.
# - A die value is in the range passed in.

# Load pytest and Die.
import pytest
from die import Die


@pytest.fixture
def d6():
    """Provide a fresh six-sided die for each test (fixture)."""
    return Die(6)


def testinitialvalueiszero():
    """A new die reports a current value of 0 before being rolled."""
    die = Die(20)
    assert die.getcurrentvalue() == 0


def testrollreturnsvalueinrange(d6):
    """Rolling a d6 returns a value between 1 and 6 (fixture)."""
    for _ in range(1000):
        result = d6.roll()
        assert 1 <= result <= 6


def testrollupdatescurrentvalue(d6):
    """roll() and getcurrentvalue() agree on the most recent result (fixture)."""
    for _ in range(1000):
        result = d6.roll()
        assert d6.getcurrentvalue() == result


@pytest.mark.parametrize("sides", [4, 6, 8, 10, 20, 100])
def testalldicestayinrange(sides):
    """Every die type rolls only within [1, sides] (parameterize)."""
    die = Die(sides)
    for _ in range(1000):
        result = die.roll()
        assert 1 <= result <= sides

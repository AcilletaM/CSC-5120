# CSC 5120 Module 4 Project
# Paul England
# Andrew Davis

# Load pytest, Mugwump, and Character.
import pytest
from wizard import Wizard
from character import Character


@pytest.fixture
def wizard():
    """Provide a fresh computer-controlled Wizard for each test (fixture)."""
    return Wizard(False, "test")


def testwizardisacharacter(wizard):
    """A Wizard is a Character through inheritance (fixture)."""
    assert isinstance(wizard, Character)


def teststartinghitpointsinrange(wizard):
    """Six d10 give a Wizard between 6 and 60 starting hit points (fixture)."""
    assert 6 <= wizard.maxhitpoints <= 60
    assert wizard.hitpoints == wizard.maxhitpoints


def testattackdamageinrange(wizard):
    """Across many attacks, damage stays within the -6..18 range (fixture)."""
    for _ in range(1000):
        damage = wizard.attack()
        assert -6 <= damage <= 18


def testaireturnsvalidattacktype(wizard):
    """The AI only ever chooses attack types 1, 2, or 3 (fixture)."""
    for _ in range(1000):
        # _chooseaiattack is a protected hook; a test may reach past the public API
        assert wizard._chooseaiattack() in (1, 2, 3)


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
def testtakedamage(wizard, starthp, maxhp, amount, expected):
    """takedamage handles hits, overkill, and capped healing (fixture + parameterize)."""
    wizard.maxhitpoints = maxhp
    wizard.hitpoints = starthp
    wizard.takedamage(amount)
    assert wizard.hitpoints == expected

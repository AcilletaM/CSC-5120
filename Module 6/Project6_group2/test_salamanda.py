# James Splingaire
#salamanda test file
import random

import pytest
from character import Character
from salamanda import Salamanda

@pytest.fixture
def my_salamanda():
    """Provide a fresh computer-controlled salamanda for each test (fixture)."""
    isplayer = True
    temp_instance_test = Salamanda(isplayer)
    temp_instance_test.name = "test"
    return temp_instance_test


def testsalamandaisacharacter(my_salamanda):
    """A salamanda is a Character through inheritance (fixture)."""
    assert isinstance(my_salamanda, Character)


def teststartinghitpointsinrange(my_salamanda):
    """Six d10 give a salamanda between 6 and 60 starting hit points (fixture)."""
    assert 6 <= my_salamanda.maxhitpoints <= 60
    assert my_salamanda.hitpoints == my_salamanda.maxhitpoints


def testattackdamageinrange(my_salamanda):
    """Across many attacks, damage stays within the -6..18 range (fixture)."""
    for i in range(50):
        #for attack type 1, damage is either 20 or 0
        damage = my_salamanda._performattack(1)
        assert damage == 0 or damage == 20

    for i in range(50):
        #for attack type 2, damage is between 2 and 12, or 0
        damage = my_salamanda._performattack(2)
        assert 2 <= damage <= 12 or damage == 0

    my_salamanda.hitpoints = 0
    my_salamanda.maxhitpoints = 40
    for i in range(40):
        #for attack type 2, damage is

        damage = my_salamanda._performattack(3)
        damage = my_salamanda._performattack(3)

        my_salamanda.hitpoints +=1

        assert 0 >= damage >= -40


def testaireturnsvalidattacktype(my_salamanda):
    """The AI only ever chooses attack types 1, 2, or 3 (fixture)."""
    for i in range(1000):
        # _chooseaiattack is a protected hook; a test may reach past the public API
        assert my_salamanda._chooseaiattack() in (1, 2, 3)


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
def testtakedamage(my_salamanda, starthp, maxhp, amount, expected):
    """takedamage handles hits, overkill, and capped healing (fixture + parameterize)."""
    my_salamanda.maxhitpoints = maxhp
    my_salamanda.hitpoints = starthp
    my_salamanda.takedamage(amount)
    assert my_salamanda.hitpoints == expected

def testprompt_for_attack(my_salamanda, monkeypatch):
    list1 = ["1","2","3"]

    for i in range(1000):
        input = random.choice(list1)
        monkeypatch.setattr('builtins.input', lambda _: input)
        assert my_salamanda._promptforattack() in (1,2,3)



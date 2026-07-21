# CSC 5120 Module 6 Project
# Paul England
# Instructions
# Design and code 3 or more new playable characters that will use inheritance (or a protocol) similar to the warrior and mugwump classes in Project 4.
#   - New characters show follow the Protocol or inherit from the base class as was done in Project 4 with mugwump and warrior. Enforce protocols with isinstance in a test.
#   - New characters should have at least 2 attacks and 1 heal
#   - Also incorporate at least 1 other special ability, like charging up to make the next attack more powerful, or always hit, or having an attack that requires 2 or more turns to prepare, etc.
#   - Create/update tests for all functions, and include a test_classname for each class. The instructor may also provide some tests classes to use/test you code with.
#
# I have created the attacks to be nature based:
#   1 - Summon a swarm of locusts.
#   2 - Use a club.  Druids are forbidden to cut (similar to clerics in pre-1st edition AD&D versions).
#   3 - Cause convulsions.  I'm combining a bit of Age of Empires here with what is said and causing damage instead of
#       converting to my cause.  This takes 3 rounds to accomplish, which is a big risk because Druids are generally weak.
#   4 - Heal.
#   5 - AI only option.  Reached by choosing to heal when already at max HP.
#
# This file contains the tests of the Druid and Character classes.  We are testing:
# - A new druid is created.
# - A druid is a Character.
# - A druid has a name.
# - The starting hp of a druid is in the expected range.
# - The damage caused by a druid attack is in the expected range.
# - The "AI" determines a valid attack for a druid attack.
# - There are win messages for every match-up combination.
# - The Defeats method returns the valide win message.
# - Players can only choose an attack between 1 and 4.
# - Damage in a single round attack is in the expected range.
# - Convulsion attack takes three rounds to complete and resets.
# - Convulsion attack resets if another attack is chosen before three rounds.
# - AI completes a convulsion attack if it happens to choose that attack.
# - AI can choose to heal when hurt and actually heal.
# - AI attacks with a weak club attack if it chooses to heal while already at max HP.
# - The damage taken by a druid attack is in the expected range.

# Load pytest, Druid, and Character.
import pytest
from druid import Druid
from character import Character
from salamanda import Salamanda


# Test initial Druid setup.
@pytest.fixture
def druid():
    """Provide a fresh computer-controlled Druid for each test (fixture)."""
    return Druid(False)

def testdruidisacharacter(druid):
    """A Druid is a Character through inheritance (fixture)."""
    assert isinstance(druid, Character)

def testdruidhasaname(druid):
    """A Druid has the inherited default name that can also be overwritten (fixture)."""
    assert druid.name == "Hal 9000"
    druid.name = "Druid McDruidface"
    assert druid.name == "Druid McDruidface"

def teststartinghitpointsinrange(druid):
    """Three d8 give a Druid between 3 and 24 starting hit points (fixture)."""
    assert 3 <= druid.maxhitpoints <= 24
    assert druid.hitpoints == druid.maxhitpoints

# Test basic attack logic.
def testattackdamageinrange(druid):
    """Across many attacks, damage stays within the -12..30 range (fixture)."""
    for _ in range(1000):
        damage = druid.attack()
        assert -12 <= damage <= 30

def testaireturnsvalidattacktype(druid):
    """The AI only ever chooses attack types 1, 2, 3, or 5 (fixture)."""
    for _ in range(1000):
        # _chooseaiattack is a protected hook; a test may reach past the public API
        assert druid._chooseaiattack() in (1, 2, 3, 5)

def testwinmessagesexist():
    """Validate a win message exists for each player/computer/opponent class combinations."""
    for controller in ("player", "computer"):
        for opponent in ("Warrior", "Mugwump", "Druid", "Salamanda", "Wizard"):
            assert (controller, opponent) in Druid.winmessages

def testdefeatsmessages(druid):
    """Defeats finds the appropriate message for the matchup (fixture)."""
    loser = Druid(False)
    assert druid.defeats(loser, "player") == Druid.winmessages[("player", "Druid")]
    assert druid.defeats(loser, "computer") == Druid.winmessages[("computer", "Druid")]
    loser = Salamanda(False)
    assert druid.defeats(loser, "player") == Druid.winmessages[("player", "Salamanda")]
    assert druid.defeats(loser, "computer") == Druid.winmessages[("computer", "Salamanda")]

@pytest.mark.parametrize(
    "attacktype",
    [
        "1",    # locust swarm
        "2",    # club
        "3",    # convulse
        "4",    # heal
    ],
)
def testplayerchoices(monkeypatch, druid, attacktype):
    """The player prompt ignores bad choices and returns the valid number the player enters (fixture + monkeypatch)."""
    answers = iter(["club", "0", "5", attacktype])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    # _promptforattack is a protected hook; a test may reach past the public API
    assert druid._promptforattack() == int(attacktype)

# Test the single round attacks.
@pytest.mark.parametrize(
    "attacktype, lowest, highest",
    [
        (1, 0, 18),    # locust swarm: miss, 2d6 on a hit, or 3d6 on a natural 20
        (2, 0, 8),     # club: miss, 1d4 on a hit, or 2d4 on a natural 20
        (4, -12, 0),   # heal: nothing, -1d6 on success, or -2d6 on a natural 20
        (5, 0, 4),     # AI-only weak club: miss or 1d4, with no natural 20 bonus
    ],
)
def testperformattackdamageinrange(druid, attacktype, lowest, highest):
    """Validate the single-round attack types stays within its own damage range (fixture + parameterize)."""
    for _ in range(1000):
        # _performattack is a protected hook; a test may reach past the public API
        damage = druid._performattack(attacktype)
        assert lowest <= damage <= highest

# Test the special multi-round woolooolooo attack.
def testwooloolooattacktakesthreerounds(druid):
    """Validate the multi-round attack.  The convulsion does nothing for two rounds, fires for exactly 30, then resets (fixture)."""
    # _performattack is a protected hook; a test may reach past the public API
    assert druid._performattack(3) == 0
    assert druid._performattack(3) == 0
    assert druid._performattack(3) == 30
    # Validate the attack resets and takes 3 turns again.
    assert druid._performattack(3) == 0
    assert druid._performattack(3) == 0
    assert druid._performattack(3) == 30

@pytest.mark.parametrize("interruption", [1, 2, 4, 5])   # locusts, club, heal, and the weak club all break the chant
def testwooloolooattackresets(druid, interruption):
    """Validate any other attack resets the convulsion attack (fixture + parameterize)."""
    # _performattack is a protected hook; a test may reach past the public API
    assert druid._performattack(3) == 0
    druid._performattack(interruption)
    assert druid._performattack(3) == 0
    assert druid._performattack(3) == 0
    assert druid._performattack(3) == 30

def testaicommitstowooloooloooattack(druid):
    """Once the chant has started, the AI keeps choosing attacktype 3 until complete. (fixture)."""
    # _chooseaiattack is a protected hook; a test may reach past the public API
    druid.wooloolooattack = 1
    assert druid._chooseaiattack() == 3
    druid.wooloolooattack = 2
    assert druid._chooseaiattack() == 3

# Test the AI heals when hurt but attacks when at full HP.
def testaicanhealswhenhurt(druid):
    """If the AI is not at the max HP, it can heal. (fixture)."""
    druid.hitpoints = 1
    choices = set()
    for _ in range(1000):
        # _chooseaiattack is a protected hook; a test may reach past the public API
        choices.add(druid._chooseaiattack())
    assert choices == {1, 2, 3, 4}

def testfullhealthonlyattacks(druid):
    """If the AI is already at the max HP, it switches to a weak club attack when choosing to heal. (fixture)."""
    choices = set()
    for _ in range(1000):
        # _chooseaiattack is a protected hook; a test may reach past the public API
        choices.add(druid._chooseaiattack())
    assert choices == {1, 2, 3, 5}

# Validate the Druid takes damage properly.
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

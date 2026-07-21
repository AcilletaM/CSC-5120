# CSC 5120 Module 6 Project
# Paul England
# Andrew Davis
# James Splingaire
#
# Instructions
# The goal of the sixth project is to modify your Mugwump project from Module 4 with a group, using a Git repository to collaborate on the code.
#
# This file contains the tests of the battle_sim program.  We are testing:
# - An initiative role returns 1 or 2.
# - Validates the playagain method.
# - Validates the choosecombatant method.
# - If two computers fight each other they finish correctly.
# - Validate the victory messages reflect who won and what class.
# - Test for a warrior's cowardice.

# Load pytest, Mugwump, and Character.
import pytest
import battle_sim
from warrior import Warrior
from mugwump import Mugwump


def testinitiativereturnsoneortwo():
    """initiative() always resolves a tie and returns 1 or 2."""
    for _ in range(1000):
        assert battle_sim.initiative() in (1, 2)


@pytest.mark.parametrize(
    "usertext, expected",
    [
        ("yes", True),
        ("y", True),
        ("YES", True),
        ("Yes", True),
        ("no", False),
        ("n", False),
        ("nope", False),
        ("", False),
    ],
)
def testplayagain(monkeypatch, usertext, expected):
    """playagain() reads the user's answer and maps it to a boolean (monkeypatch + parameterize)."""
    # swap the built-in input so the test feeds a canned answer instead of blocking
    monkeypatch.setattr("builtins.input", lambda *args, **kwargs: usertext)
    assert battle_sim.playagain() == expected


@pytest.mark.parametrize(
    "userchoice, expectedtype, isplayer",
    [
        ("1", Warrior, True),
        ("2", Mugwump, True),
        ("1", Warrior, False),
        ("2", Mugwump, False),
    ],
)
def testchoosecombatant(monkeypatch, userchoice, expectedtype, isplayer):
    """chooseCombatant() builds the requested character with the right control flag (monkeypatch + parameterize)."""
    monkeypatch.setattr("builtins.input", lambda *args, **kwargs: userchoice)
    combatant = battle_sim.choosecombatant("test role", isplayer)
    assert isinstance(combatant, expectedtype)
    assert combatant.isplayer == isplayer


def testtwocomputersfighttoafinish():
    """A full computer-vs-computer battle reaches a winner (integration smoke test)."""
    player = Mugwump(False, "test")
    computer = Warrior(False, "test")
    victor = "none"
    rounds = 0
    while victor == "none" and rounds < 10000:
        victor = battle_sim.battle(player, computer)
        rounds += 1
    assert victor in ("player", "computer")
    assert (player.hitpoints <= 0) or (computer.hitpoints <= 0)


@pytest.mark.parametrize(
    "playerclass, computerclass, victor, keyword",
    [
        (Warrior, Mugwump, "player", "citizens"),
        (Warrior, Mugwump, "computer", "weeps"),
        (Mugwump, Warrior, "player", "vanquished"),
        (Mugwump, Warrior, "computer", "triumphed"),
        (Warrior, Warrior, "player", "flees"),
        (Warrior, Warrior, "computer", "pyrrhic"),
        (Mugwump, Mugwump, "player", "mightier"),
        (Mugwump, Mugwump, "computer", "heinous"),
    ],
)
def testvictorymessage(capsys, playerclass, computerclass, victor, keyword):
    """victory prints the message matching the matchup and outcome (capsys + parameterize)."""
    player = playerclass(True, "test")
    computer = computerclass(False, "test")
    battle_sim.victory(player, computer, victor)
    captured = capsys.readouterr()
    assert keyword in captured.out


@pytest.mark.parametrize("victor", ["player", "computer"])
def testtwowarriorsbrandacoward(capsys, victor):
    """In a Warrior-vs-Warrior duel, someone is always branded a coward (capsys + parameterize)."""
    battle_sim.victory(Warrior(True, "test"), Warrior(False, "test"), victor)
    captured = capsys.readouterr()
    assert "coward" in captured.out

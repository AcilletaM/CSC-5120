# CSC 5120 Module 6 Project
# Paul England
# Andrew Davis
# James Splingaire
#
# Instructions
# The goal of the sixth project is to modify your Mugwump project from Module 4 with a group, using a Git repository to collaborate on the code.
# - Create/update tests for all functions, and include a test_classname for each class. The instructor may also provide some tests classes to use/test you code with.
#
# This file contains the tests of the battle_sim program.  We are testing:
# - An initiative roll returns 1 or 2.
# - Validates the playagain function.
# - Validate the choosecombatant function creates the correct character and with a name.
# - Validate the choosecombatant function loads the correct character from a csv file.
# - If two computers fight each other they finish correctly, using all classes.
# - Validate the victory messages reflect who won and what class.
# - Test for a warrior's cowardice.

# Load pytest, battle_sim, Character, and the combatant classes.
import pytest
import battle_sim
from warrior import Warrior
from mugwump import Mugwump
from druid import Druid
from salamanda import Salamanda
from wizard import Wizard


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


@pytest.mark.parametrize("isplayer", [True, False])
@pytest.mark.parametrize(
    "menuchoice, expectedtype",
    [
        ("1", Warrior),
        ("2", Druid),
        ("3", Mugwump),
        ("4", Salamanda),
        ("5", Wizard),
    ],
)
def testchoosecombatantnewcharacter(monkeypatch, menuchoice, expectedtype, isplayer):
    """chooseCombatant() builds the requested character class with a name (monkeypatch + parameterize)."""
    # This function changed to be 2 levels, not 1.  2 forces it to create a new character.
    # This should reject 0, banana, and 3 at the load from csv/create new character prompt.
    # 2 is valid for create new character and goes to the character class choice prompt.
    # xyx, 0, and 6 are rejected at that prompt before getting valid character prompts and a name.
    answers = iter(["0", "banana", "3", "2", "xyz", "0", "6", menuchoice, "Testy McTestface"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    combatant = battle_sim.choosecombatant("test role", isplayer)
    assert isinstance(combatant, expectedtype)
    assert combatant.isplayer == isplayer
    assert combatant.name == "Testy McTestface"

# New function added to load from .csv file.  I personally found this test interesting to learn - PE.
def testchoosecombatantloadsfromcsv(monkeypatch, tmp_path):
    """choosecombatant loads a saved character's class, name, and hit points from the CSV (monkeypatch + tmp_path)."""
    # This generates a file only for testing.  It does not use our pre-defined .csv file.
    savefile = tmp_path / "character_save_file.csv"
    savefile.write_text(
        "Character Name,Max Hitpoints,Class Type\n"
        "john,40,Warrior\n"
        "The Wiz,44,Wizard\n",
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
 
    # This test is a direct result of my initial testing loading characters from csv.  I entered the characters name because I didn't read the instructions, because what to enter was implied.
    # 1 picks Load from CSV.
    # "The Wiz", 3, and 0 are handled and don't select a row from the csv.
    # 2 picks the second saved character.
    answers = iter(["1", "The Wiz", "3", "0", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    combatant = battle_sim.choosecombatant("test role", False)
    assert isinstance(combatant, Wizard)
    assert combatant.name == "The Wiz"
    assert combatant.maxhitpoints == 44
    assert combatant.hitpoints == 44

# This function was never tested in Module 4.  It can, using monkeypatch.
def testresolveturn(monkeypatch):
    """resolveturn positive values damage the defender, negative values heal the attacker, and 0 does nothing. (monkeypatch)."""
    attacker, defender = Warrior(False), Warrior(False)
    attacker.maxhitpoints = 30
    defender.maxhitpoints = 30
    attacker.hitpoints = 20
    defender.hitpoints = 30

    # Defender takes damage.
    monkeypatch.setattr(attacker, "attack", lambda: 5)
    battle_sim.resolveturn(attacker, defender)
    assert (attacker.hitpoints, defender.hitpoints) == (20, 25)

    # Attacker heals.
    monkeypatch.setattr(attacker, "attack", lambda: -3)
    battle_sim.resolveturn(attacker, defender)
    assert (attacker.hitpoints, defender.hitpoints) == (23, 25)

    # No change in HP.
    monkeypatch.setattr(attacker, "attack", lambda: 0)
    battle_sim.resolveturn(attacker, defender)
    assert (attacker.hitpoints, defender.hitpoints) == (23, 25)

@pytest.mark.parametrize(
    "playerclass, computerclass",
    [
        (Warrior, Mugwump),
        (Warrior, Warrior),
        (Warrior, Druid),
        (Warrior, Salamanda),
        (Warrior, Wizard),
        (Mugwump, Mugwump),
        (Mugwump, Druid),
        (Mugwump, Salamanda),
        (Mugwump, Wizard),
        (Druid, Druid),
        (Druid, Salamanda),
        (Druid, Wizard),
        (Salamanda, Salamanda),
        (Salamanda, Wizard),
        (Wizard, Wizard),
    ],
)
def testtwocomputersfighttoafinish(playerclass, computerclass):
    """A full computer-vs-computer battle reaches a winner.  The original only tested the Warrior and Mugwump.  Changed to test the every class match-up. (integration smoke test)."""
    player = playerclass(False)
    computer = computerclass(False)
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
    player = playerclass(True)
    computer = computerclass(False)
    battle_sim.victory(player, computer, victor)
    captured = capsys.readouterr()
    assert keyword in captured.out


@pytest.mark.parametrize("victor", ["player", "computer"])
def testtwowarriorsbrandacoward(capsys, victor):
    """In a Warrior-vs-Warrior duel, someone is always branded a coward (capsys + parameterize)."""
    battle_sim.victory(Warrior(True), Warrior(False), victor)
    captured = capsys.readouterr()
    assert "coward" in captured.out

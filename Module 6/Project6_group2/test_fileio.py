# CSC 5120 Module 6 Project
# Paul England
# Andrew Davis
# James Splingaire
#
# Instructions
# The goal of the sixth project is to modify your Mugwump project from Module 4 with a group, using a Git repository to collaborate on the code.
# - Create/update tests for all functions, and include a test_classname for each class. The instructor may also provide some tests classes to use/test you code with.
#
# This file contains the tests of the fileio module.  We are testing:
# - Saving to a file adds a row to the end.
# - save_data can save a row to a file and then choosecombatant can read it immediately with no issues.

# Load pytest, fileio, battle_sim, and the character classes.
import pytest
import fileio
import battle_sim
from warrior import Warrior
from mugwump import Mugwump

def testsavedataappendsrows(monkeypatch, tmp_path):
    """save_data appends a new row with the name, max hitpoints, and class.  Make sure it adds to the end and doesn't affect existing rows (monkeypatch + tmp_path)."""
    savefile = tmp_path / "character_save_file.csv"
    savefile.write_text(
        "Character Name,Max Hitpoints,Class Type\n"
        "john,40,Warrior\n",
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)  # save_data opens the CSV relative to the working directory
 
    first = Warrior(False)
    first.name = "Savey McSaveface"
    fileio.save_data(first)
    second = Mugwump(False)
    second.name = "Wumpy"
    fileio.save_data(second)
 
    lines = savefile.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "Character Name,Max Hitpoints,Class Type"
    assert lines[1] == "john,40,Warrior"
    assert lines[2] == f"Savey McSaveface,{first.maxhitpoints},Warrior"
    assert lines[3] == f"Wumpy,{second.maxhitpoints},Mugwump"
    assert len(lines) == 4

def testsavethenload(monkeypatch, tmp_path):
    """A character saved to the existing save file can be loaded back through the menu (monkeypatch + tmp_path)."""
    # The csv logic is designed with a save file already in place, so the test seeds one
    # with the header, matching the file that ships with the game.
    savefile = tmp_path / "character_save_file.csv"
    savefile.write_text("Character Name,Max Hitpoints,Class Type\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    player = Warrior(False)
    player.name = "Paul England"
    fileio.save_data(player)

    # 1 picks Load from CSV, then 1 picks the only saved row
    answers = iter(["1", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    loaded = battle_sim.choosecombatant("test role", False)
    assert isinstance(loaded, Warrior)
    assert loaded.name == "Paul England"
    assert loaded.maxhitpoints == player.maxhitpoints
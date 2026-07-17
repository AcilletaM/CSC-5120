# CSC 5120 Module 4 Project
# Paul England
# Instructions
# The goal of the fourth project is to review the concepts we have learned thus far. We will apply the concepts of
# inheritance (also called duck typing) and testing to the Battle Sim example Lab we worked through in class. Your
# project will have several files.
#
# This file is the driver file that handles the user interaction and the Character creation.
# - Copy in the battlesim, die, mugwump, and warrior classes we worked on in class as a starting place.
#   Based on what we learned in a class and the material on Canvas and in the book, add code to ensure your project
#   satisfies all the requirements listed below.
#   - 20 points: Choose whether you will use duck typing (Protocol) or base class  (Character parent class) for
#     refactoring the mugwump and warrior classes. If using a protocol, enforce it with isinstance or function signature
#     hints. The goal is to have use two object references player (player controlled) and computer(computer controlled),
#     which can each be either a warrior or a mugwump, and then allow the user to play out the game in the same ways as
#     they did before.
#   - 30 points: Present the user with a choice for each of the two player objects *so it could be a player controlled
#     warrior vs. an ai controlled mugwump, or two mugwumps, two warriors, player mugwump and ai warrior).
# The game should play out the same once the user has made the initial choices about player types.

# Bring in the class definitions
from warrior import Warrior
from mugwump import Mugwump
from druid import Druid
from salamanda import Salamanda
#from wizard import Wizard
from character import Character
from die import Die

# The dungeon master uses a 10-sided die to roll for initiative each round.
d10 = Die(10)

def main():  # not testable
    """Run the Battle Simulator 3000 game loop."""
    keep_playing = True
    turns = 1

    while keep_playing:
        intro(turns)
        turns = turns + 1

        # let the user decide what the player and the computer each are;
        # any of the four combinations is possible
        player = choosecombatant("PLAYER (you control)", True)
        computer = choosecombatant("COMPUTER (AI controls)", False)

        # Make sure both references are Characters
        assert isinstance(player, Character)
        assert isinstance(computer, Character)

        # Show initial hit points and then battle until someone falls
        print("\nLet the epic battle begin!")

        victor = "none"
        while victor == "none":
            report(player, computer)
            victor = battle(player, computer)

            # Declare the winner and prompt to play again.
            if (victor != "none"):
                report(player, computer)
                victory(player, computer, victor)
                keep_playing = playagain()

    print("\nThank you for playing Battle Simulator 3000!")

def intro(turns):  # not testable
    """Display the introduction and rules of the game."""

    # Just because it's low tech doesn't mean it can't have a little ASCII art style.
    oldskooltitlescreen = r"""
    ==============================================================================
                        ______  ___ _____ _____ _      _____
                        | ___ \/ _ \_   _|_   _| |    |  ___|
                        | |_/ / /_\ \| |   | | | |    | |__
                        | ___ \  _  || |   | | | |    |  __|
                        | |_/ / | | || |   | | | |____| |___
                        \____/\_| |_/\_/   \_/ \_____/\____/

                _____ ________  ____   _ _       ___ _____ ___________
               /  ___|_   _|  \/  | | | | |     / _ \_   _|  _  | ___ \
               \ `--.  | | | .  . | | | | |    / /_\ \| | | | | | |_/ /
                `--. \ | | | |\/| | | | | |    |  _  || | | | | |    /
               /\__/ /_| |_| |  | | |_| | |____| | | || | \ \_/ / |\ \
               \____/ \___/\_|  |_/\___/\_____/\_| |_/\_/  \___/\_| \_|

                              _____  _____  _____  _____
                             |____ ||  _  ||  _  ||  _  |
                                 / /| |/' || |/' || |/' |
       o==[]::::::::::::::>      \ \|  /| ||  /| ||  /| |  <::::::::::::::[]==o
                             .___/ /\ |_/ /\ |_/ /\ |_/ /
                             \____/  \___/  \___/  \___/

                 Warriors * Druids * Mugwumps * Salamandas * Wizards
                    ~ The World's Most Low-Tech Battle Simulator ~
    =============================================================================="""

    if turns == 1:
        print(f"{oldskooltitlescreen}")
        print("Valiant Warriors, Neutral Druids, Slippery Salamanda, Powerful Wizards, and Evil Mugwumps face off in epic combat.")

    print("\nYou choose what the player and the computer each fight as, then trade blows until only one stands.\n\n"
          "The Characters:\n"
          "The Warrior swings a Trusty Sword (2d8) or raises a Shield of Light (1d4).\n"
          "The Druid summons a swarm of locusts (2d6), swings a might oak club (2d4), or heals through natural medicines.\n"
          "The Salamanda smacks with its large tail (20), spits a slime ball (2d6), or sheds its skin to heal over two rounds.\n"
          "The Wizard burns with a firebolt spell (1d12), casts bonechill (3d6), or heals through magical means.\n")


def choosecombatant(rolename: str, isplayer: bool) -> Character:  # testable
    """Ask which character type to use for a role and return the new combatant."""
    choice = 0
    while choice <= 0 or choice > 5:
        choice = int(input(f"Choose the {rolename} character:\n"
                           "1. Warrior\n"
                           "2. Druid\n"
                           "3. Mugwump\n"
                           "4. Salamanda\n"
                           "5. Wizard\n"
                           "Enter choice: "))

    if choice == 1:
        return Warrior(isplayer)
    elif choice == 2:
        return Druid(isplayer)
    elif choice == 3:
        return Mugwump(isplayer)
    elif choice == 4:
        return Salamanda(isplayer)
#    else:
#        return Wizard(isplayer)

def battle(player: Character, computer: Character) -> str:  # not testable (randomness + I/O)
    """Individual round of combat.  Returns 'player' or 'computer' if they are the victor otherwise it returns 'none'."""
    # Roll for initiative
    currentinitiative = initiative()

    # Player first
    if (currentinitiative == 1):
        print("\nThe player attacks first!")
        resolveturn(player, computer)
        if (computer.hitpoints <= 0):
            return "player"
        resolveturn(computer, player)
        if (player.hitpoints <= 0):
            return "computer"
    # Computer first
    else:
        print("\nThe computer attacks first!")
        resolveturn(computer, player)
        if (player.hitpoints <= 0):
            return "computer"
        resolveturn(player, computer)
        if (computer.hitpoints <= 0):
            return "player"

    # if neither combatant is defeated, the battle rages on!
    return "none"

def resolveturn(attacker: Character, defender: Character) -> None:  # not testable (randomness + I/O)
    """Resolve one attack by a Character. Either the defender will take damage or the attacker will heal."""
    damage = attacker.attack()

    # Damage can be positive or negative, depending on if it is inflicted damage or healing.
    if (damage > 0):
        defender.takedamage(damage)
    else:
        attacker.takedamage(damage)

def report(player: Character, computer: Character) -> None:  # not testable
    """Report the current hit points of both combatants."""
    print(f"Player:  {type(player).__name__} HP: {player.hitpoints}")
    print(f"Computer:  {type(computer).__name__} HP: {computer.hitpoints}")

def initiative() -> int:  # testable (returns 1 or 2)
    """Roll for initiative.  If the player and computer tie then they re-roll. Return 1 for player otherwise 2 for computer."""
    playerinitiative = d10.roll()
    computerinitiative = d10.roll()

    # Re-roll any ties.  Someone must win.
    while playerinitiative == computerinitiative:
        playerinitiative = d10.roll()
        computerinitiative = d10.roll()

    # We have a winning roll.  Return 1 for the player and 2 for the computer.
    if playerinitiative > computerinitiative:
        return 1
    return 2

def victory(player: Character, computer: Character, victor: str) -> None:  # not testable
    """Announce the winner, keeping in mind the player vs computer battle and the different combinations possible."""
    if victor == "player":
        winner, loser = player, computer
    else:
        winner, loser = computer, player

    print(winner.defeats(loser, victor))

def playagain() -> bool:  # testable
    """Ask whether to play again; return True for yes, False otherwise."""
    choice = input("Would you like to play again (yes/no)? ")
    if str.lower(choice) == "y" or str.lower(choice) == "yes":
        return True
    return False

if __name__ == "__main__":
    main()

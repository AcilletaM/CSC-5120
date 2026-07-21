# CSC 5120 Module 6 Project
# Paul England - Druid
# Andrew Davis - Wizard
# James Splingaire - Salamanda
#
# Instructions
# The goal of the sixth project is to modify your Mugwump project from Module 4 with a group, using a Git repository to collaborate on the code.
#
# - You and a partners should create a GitHub repository, and add the professor as a third/additional member. Use GitHub username jonathonflynn
# - You and your partners should decide whose Module 4 code to use as a base, and add that to the repository as an initial commit. You can use the main branch for everything.
# - Perform a code cleanup/refactoring as needed.
#   - and commit and push those changes
#   - I strongly recommend using an abstract base class with @abstractmethod tags if using inheritance, see: https://docs.python.org/3/library/abc.html
# - Design and code 3 or more new playable characters that will use inheritance (or a protocol) similar to the warrior and mugwump classes in Project 4.
#   - New characters show follow the Protocol or inherit from the base class as was done in Project 4 with mugwump and warrior. Enforce protocols with isinstance in a test.
#   - New characters should have at least 2 attacks and 1 heal
#   - Also incorporate at least 1 other special ability, like charging up to make the next attack more powerful, or always hit, or having an attack that requires 2 or more turns to prepare, etc.
#   - All characters should now have a name attribute, which the player can enter when they choose their character
# - Design and code character saving functionality and allow the user to save their character at the end of the fight.
#   - allow saving of name, max hitpoints, and "class" meaning warrior/mugwump/etc, along with any of information needed
#   - I recommend using a CSV file, see: https://docs.python.org/3/library/csv.html
#      - but you can also use JSON or plain text
# - Allow the user to load a character from a save file instead of choosing to create a new one as part of the initial menu
# - Each group member should be solely responsible for coding at least one of the new characters, and assist with the save/load code and other updates to the driver. Each group member should commit and push code they work on individually.
# - Create/update tests for all functions, and include a test_classname for each class. The instructor may also provide some tests classes to use/test you code with.
# - Submit a link to your repository when finished.
#
# This file is the driver file that handles the user interaction and the Character creation.

# Bring in the class definitions
from warrior import Warrior
from mugwump import Mugwump
from druid import Druid

from salamanda import Salamanda
from wizard import Wizard

from character import Character
from die import Die


import fileio

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




                choice_save_player = input(f"Would you like to save player info for {type(player).__name__} (yes/no)? ")
                if str.lower(choice_save_player) == "y" or str.lower(choice_save_player) == "yes":
                    fileio.save_data(player)

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
          "The Druid summons a swarm of locusts (2d6), swings a might oak club (2d4), cause convulsions (30), or heals through natural medicines.\n"
          "The Salamanda smacks with its large tail (20), spits a slime ball (2d6), or sheds its skin to heal over two rounds.\n"
          "The Wizard burns with a firebolt spell (1d12), casts bonechill (3d6), or heals through magical means.\n")

def choosecombatant(rolename: str, isplayer: bool) -> Character:  # testable
    """Ask which character type to use for a role and return the new combatant."""

    temp_instance = None
    extract_character_type = None
    choice_select = 0
    row_num = 1

    while choice_select != 1 and choice_select != 2:
            response = input(f"Choose the {rolename} character, choose to load from existing characters OR define a new charater:\n"
                           "1. Load from CSV\n"
                           "2. Make New Character\n"
                           "Enter choice: ")
            if response.isdigit():
                choice_select = int(response)

    if(choice_select == 1): #import an existing character
        #allow saving of name, max hitpoints, and "class" meaning warrior/mugwump/etc, along with any of information needed
        print(f"selected load {rolename} character from CSV file\n")
        choice_csv = 0

        import csv
        with open('character_save_file.csv', newline='', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"{row_num}.)", "|| Character Name:", row["Character Name"], "|| Max Hitpoints:", row["Max Hitpoints"], "|| Class Type:", row["Class Type"], "\n")
                row_num += 1

        num_characters = row_num - 1  # row_num was actually the number of characters in the file plus 1
        while choice_csv <= 0 or choice_csv > num_characters:
            response = input(f"Choose the {rolename} character:\n"
            "Enter choice: ")
            if response.isdigit():
                choice_csv = int(response)

        #set row equal to what the person just chose
        row_num = 1
        with open('character_save_file.csv', newline='', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row_num == choice_csv:
                    extract_character_type = str(row["Class Type"])

                    if extract_character_type == "Warrior":
                        temp_instance = Warrior(isplayer)
                    elif extract_character_type == "Druid":
                        temp_instance = Druid(isplayer)
                    elif extract_character_type == "Mugwump":
                        temp_instance = Mugwump(isplayer)
                    elif extract_character_type == "Salamanda":
                        temp_instance = Salamanda(isplayer)
                    else:
                        temp_instance =  Wizard(isplayer)

                    #make sure the temporary instance has hitpoints loaded from CSV file
                    temp_instance.maxhitpoints = int(row["Max Hitpoints"])
                    temp_instance.hitpoints = temp_instance.maxhitpoints
                    temp_instance.name = row["Character Name"]
                    print(f"loading character type: {extract_character_type}")
                    print(f"loading hitpoints: {temp_instance.maxhitpoints}")
                    print(f"loading name: {temp_instance.name}")

                    return temp_instance

                row_num += 1
    else: #make a new character
        print(f"selected create new {rolename} character \n")
        choice = 0
        name = "None"
        while choice <= 0 or choice > 5:
            response = input(f"Choose the {rolename} character:\n"
                               "1. Warrior\n"
                               "2. Druid\n"
                               "3. Mugwump\n"
                               "4. Salamanda\n"
                               "5. Wizard\n"
                               "Enter choice: ")
            if response.isdigit():
                choice = int(response)

        while name == "None":
            name = str(input(f"Enter a Name for the {rolename} character:\n"
                               "Enter custom name: "))
        if choice == 1:
            temp_instance = Warrior(isplayer)
        elif choice == 2:
            temp_instance = Druid(isplayer)
        elif choice == 3:
            temp_instance = Mugwump(isplayer)
        elif choice == 4:
            temp_instance = Salamanda(isplayer)
        else:
            temp_instance =  Wizard(isplayer)

        temp_instance.name = name

        return temp_instance

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
    print(f"Player: {type(player).__name__} || HP: {player.hitpoints} || Name: {player.name}")
    print(f"Computer:  {type(computer).__name__} ||  HP: {computer.hitpoints} || Name: {computer.name}")

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

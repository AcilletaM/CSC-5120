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
from character import Character
from die import Die

# The dungeon master uses a 10-sided die to roll for initiative each round.
d10 = Die(10)

def main():  # not testable
    """Run the Battle Simulator 3000 game loop."""
    keep_playing = True

    while keep_playing:
        intro()

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

    print("Thank you for playing Battle Simulator 3000!")

def intro():  # not testable
    """Display the introduction and rules of the game."""
    print("Welcome to Battle Simulator 3000! The world's most low-tech battle simulator!\n"
          "Valiant Warriors, Neutral Druids, and Evil Mugwumps face off in epic combat.\n"
          "You choose what the player and the computer each fight as,\n"
          "then trade blows until only one stands.\n"
          "\nThe Warrior swings a Trusty Sword (2d8) or raises a Shield of Light (1d4).\n"
          "The Mugwump rends with Razor-Sharp Claws (2d6), bites with Fangs of Death (3d6),\n"
          "or licks its wounds to heal.\n"
          "The Druid summons a swarm of locusts (2d6), swings a might oak club (2d4),\n"
          "or heals through natural medicines.\n")


def choosecombatant(rolename: str, isplayer: bool) -> Character:  # testable
    """Ask which character type to use for a role and return the new combatant."""
    choice = 0
    while choice <= 0 or choice > 2:
        choice = int(input(f"Choose the {rolename} character:\n"
                           "1. Warrior\n"
                           "2. Druid\n"
                           "3. Mugwump\n"
                           "Enter choice: "))

    if choice == 1:
        return Warrior(isplayer)
    elif choice == 2:
        return Druid(isplayer)
    else:
        return Mugwump(isplayer)

def battle(player: Character, computer: Character) -> str:  # not testable (randomness + I/O)
    """Individual round of combat.  Returns 'player' or 'computer' if they are the victor otherwise it returns 'none'."""
    # Roll for initiative
    currentinitiative = initiative()

    # Player first
    if (currentinitiative == 1):
        print("The player attacks first!")
        resolveturn(player, computer)
        if (computer.hitpoints <= 0):
            return "player"
        resolveturn(computer, player)
        if (player.hitpoints <= 0):
            return "computer"
    # Computer first
    else:
        print("The computer attacks first!")
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
    print(f"{type(player).__name__} HP: {player.hitpoints}")
    print(f"{type(computer).__name__} HP: {computer.hitpoints}")

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
    playerwon = (victor == "player")
    playeriswarrior = isinstance(player, Warrior)
    playerisdruid = isinstance(player, Druid)
    opponentiswarrior = isinstance(computer, Warrior)
    opponentisdruid = isinstance(computer, Druid)

    if playeriswarrior and not opponentiswarrior and not opponentisdruid:
        # The Valiant Warrior (player) against an evil Mugwump (AI)
        if playerwon:
            print("You, the Valiant Warrior, have slain the evil Mugwump! The citizens "
                  "cheer and lay out a feast -- the kingdom is saved (again)!")
        else:
            print("The evil Mugwump has bested you, Valiant Warrior, mocking your feeble "
                  "defense as it feasts on the villagers. The kingdom weeps.")
    elif not playeriswarrior and opponentiswarrior and not opponentisdruid:
        # The Valiant Warrior (AI) against an evil Mugwump (player)
        if playerwon:
            print("You chose the path of evil -- and it paid off. You have vanquished "
                  "the Valiant Warrior.  A meal of villagers awaits you.")
        else:
            print("You chose to play the monster, but good still triumphed. "
                  "No villagers will be eaten, at least for today. "
                  "It was rough back then.")
    elif playeriswarrior and opponentiswarrior:
        # The Valiant Warrior (player) against another Valiant Warrior (AI)
        if playerwon:
            print("Two Valiant Warriors, fighting for pride instead of principle.  Still "
                  "you prevailed. Your opponent flees, forever branded a coward.")
        else:
            print("Two Valiant Warriors turned on each other, and you broke. "
                  "You slink away branded a coward while the other claims a "
                  "pyrrhic victory.")
    elif playeriswarrior and opponentisdruid:
        # The Valiant Warrior (player) against Neutral Druid (AI)
        if playerwon:
            print("You, a Valiant Warrior, fighting for people not nature.  You have easily "
                  "overcome the feeble Druid. Your opponent runs away, cursing your name.")
        else:
            print("Nature is being destroyed by the thoughtless villagers, but their Warrior has protected them. "
                  "You must return to the woods to meditate with nature.")
    elif playerisdruid and opponentisdruid:
        # The Neutral Druid (player) against another Neutral Druid (AI)
        if playerwon:
            print("Two spiritual Druids, clashing to show who loves their goddess most.  "
                  "You have earned her blessing. Your opponent breaks down in tears, spirit broken.")
        else:
            print("Two kindly Druids, instead of helping each other, tried to curry favor more than the other, and you "
                  "didn't do enough.  Your faith is shaken.")
    else:
        # An evil Mugwump (player) against an evil Mugwump (AI)
        if playerwon:
            print("Two Mugwumps clashed in the dark and you proved the mightier beast. "
                  "You feast on your fallen rival, while the villagers cower in fear, awaiting "
                  "their fate.")
        else:
            print("You chose the way of the monster and met a heinous fate. "
                  "No one will remember you or this battle.")

def playagain() -> bool:  # testable
    """Ask whether to play again; return True for yes, False otherwise."""
    choice = input("Would you like to play again (yes/no)? ")
    if str.lower(choice) == "y" or str.lower(choice) == "yes":
        return True
    return False

if __name__ == "__main__":
    main()

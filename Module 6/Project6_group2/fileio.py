# Andrew Davis
import csv

from character import Character

def save_data(player):
    """Save the player's data to a CSV file."""
    assert isinstance(player, Character)

    # name our csv file test, and open it for writing (w)
    # this creates the file if it doesn't exist
    # and the current code OVERWRITES a file if it does exist

    with open('character_save_file.csv', mode='a', newline='') as csvfile:


        writer = csv.writer(csvfile)

        print(f"storing character details: || player name: {player.name} || player hitpoints: {player.maxhitpoints} || class type: {type(player).__name__} ")
        writer.writerow([player.name, player.maxhitpoints, type(player).__name__])
        csvfile.close()



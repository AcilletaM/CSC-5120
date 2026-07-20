# Andrew Davis
import csv

from character import Character

def save_data(player):
    """Save the player's data to a CSV file."""
    assert isinstance(player, Character)

    # name our csv file test, and open it for writing (w)
    # this creates the file if it doesn't exist
    # and the current code OVERWRITES a file if it does exist
    csvfile = open('savedata.csv', 'w')
    writer = csv.writer(csvfile)

    writer.writerow(['Name', 'Class', 'Max Hit Points'])
    writer.writerow([player.name, type(player).__name__, player.maxhitpoints])
    csvfile.close()

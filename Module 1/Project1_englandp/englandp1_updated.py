# CSC 5120 Module 1 Project
# Paul England
# This program needs to:
    # - Load in the autos.json data file Download autos.json data file and verify by printing out the number of cars loaded into the DataFrame.
    # - Print a list of the data, that includes the index and a couple of other fields so the user can make a choice.
    # - Ask the user to enter the index of the car they would like to look at, use a while loop to ensure the user enters a valid index, and keep looping until they do. You can assume the user enters a int value, but it may not be in the valid range of indexes.
    # - Using the index the user provides, print out all the details about the car stored at that index.
    # - Ask the user the percentage of city driving for the car (ensure the user enters a valid number from 0 to 100. You can assume the user enters a int value (or valid float value, just make it clear to the user what you expect)
    # - Use a function that takes the car index , DataFrame of cars, and percentage of city driving as inputs, and returns the combined highway and city mpg estimate as output, and print the result. combinedMPG is percentCity * city-mpg + percentHighway*highway-mpg.
    # - Calculate the overall average city-mpg and overall average-highway-mpg of all cars (so all the values in the file averaged together into one value for city and one value for highway) using a for loop and print the result, use an if statement to determine of the user's chosen car has higher, lower or the same city-mpg as the average and print an appropriate message.

# Using more functions than required as practice.

# Defining a function for the getting the user input of their car choice.  205 cars is a lot to display so let's
# make this a little interactive
def ChooseCar(autos_df):
    # Declare the variables
    lowerbound = 300
    upperbound = 300
    carchoice = 300

    # Get the lowerbound for the car list
    while lowerbound < 0 or lowerbound > 203:
        try:
            lowerbound = int(input("Please enter the lower bound for the car list.  It must be between 0 to 203: "))
        except ValueError:
            print("That is not a valid number.  Please try again.")

    # Get the upperbound for the car list
    while lowerbound >= upperbound or upperbound > 204:
        try:
            upperbound = int(input("Please enter the upper bound for the car list.  It must be between 1 to 204 and greater than the lower bound: "))
        except ValueError:
            print("That is not a valid number.  Please try again.")

    # Show the list of cars within the selection
    print("\n",autos_df.loc[lowerbound:upperbound,["aspiration","make","body-style","city-mpg","highway-mpg"]].to_string(),"\n")

    # Get the user's valid car choice
    while lowerbound > carchoice or upperbound < carchoice:
        try:
            carchoice = int(input("Please enter your car choice from the list shown: "))
        except ValueError:
            print("That is not a valid number.  Please try again.")

    return carchoice

# Defining a function for the getting the user's city driving percentage.
def GetCityPercentage():
    # declare the var
    citypct = 300

    # Get a valid percentage of city driving
    while citypct < 0 or citypct > 100:
        try:
            citypct = int(input("Please enter the percentage of city driving for the car.  It must be between 0 to 100: "))
        except ValueError:
            print("That is not a valid number.  Please try again.")

    return citypct

# Define a function that takes the user's car choice, the dataframe of autos, and the user's city driving percentage
# and determine the combined mpg.
def GetCombinedMPG(carchoice,autos_df,citypct,debug):
    # Start with the city and highway mpg for the car choice
    citympg = autos_df.loc[carchoice]["city-mpg"]
    highwaympg = autos_df.loc[carchoice]["highway-mpg"]

    # Determine the highway percentage
    citympgpct = citypct/100
    highwaympgpct = 1.0-citypct/100

    # Do the math
    finalvalue = citympgpct*citympg + highwaympgpct*highwaympg

    # Show your work
    if debug:
        print("citympg:  ",citympg)
        print("highwaympg: ",highwaympg)
        print("citympgpct: ",citympgpct)
        print("highwaympgpct: ",highwaympgpct)
        print("finalvalue: ",finalvalue)

    return finalvalue

# Define a function that determines the average city mpg and highway mpg for all cars
def AverageMPG(autos_df,debug):
    # Define the vars
    totalcity = 0
    totalhighway = 0

    # Use a for loop to calculate the total city and highway mpg
    for i in range(len(autos_df)):
        totalcity += autos_df.loc[i,"city-mpg"]
        totalhighway += autos_df.loc[i,"highway-mpg"]

    # Determine the average
    avgcity = int(totalcity/len(autos_df))
    avghighway = int(totalhighway/len(autos_df))

    # Show the work
    if debug:
        print("Overall average city mpg:  ",avgcity)
        print("Overall average highway mpg:  ",avghighway)

    return avgcity,avghighway


# Start of the main portion of the program
# Loading autos.json into a dataframe
import pandas as pd
df = pd.read_json("autos.json")

# Print the number of cars in the autos.json file - should be 205.  Doing two ways as a double check and practice.
print(f"Number of cars in autos.json:  {df["make"].count()} = {len(df)}\n")

# Call the ChooseCar function to display a list of cars and get the user's choice
carChoice = ChooseCar(df)
print("\nYou chose ",carChoice)

# Show all the details of the user's car choice
print("\nThese are all the details for your car choice:")
print(df.iloc[carChoice],"\n")

# Call the GetCityPercentage function to get the city driving percentage from the user
CityPercentage = GetCityPercentage()
print(f"\nYou chose {CityPercentage}%\n")

# Call GetCombinedMPG to calculate the combined mpg
carchoicempg = GetCombinedMPG(carChoice,df,CityPercentage,True)
print(f"\nThe combined mpg is {carchoicempg}\n")

# Call AverageMPG to calculate the average city and highway mpg
averagecity,averagehighway = AverageMPG(df,False)
print("Average city mpg for all cars:  ",averagecity)
print("Doublecheck average city mpg for all cars:  ",int(df["city-mpg"].mean()))
print(f"Average highway mpg for all cars:  ",averagehighway)
print(f"Doublecheck average highway mpg for all cars:  {int(df["highway-mpg"].mean())}\n")

# Compare the averages to the user's car choice.  Doing both city and highway for practice.
if df.iloc[carChoice]['city-mpg'] > averagecity:
    print(f"Your car's city mpg ({df.iloc[carChoice]['city-mpg']}) is HIGHER than the fleet average.")
elif df.iloc[carChoice]['city-mpg'] < averagecity:
    print(f"Your car's city mpg ({df.iloc[carChoice]['city-mpg']}) is LOWER than the fleet average.")
else:
    print(f"Your car's city mpg ({df.iloc[carChoice]['city-mpg']}) is the SAME as the fleet average.")

if df.iloc[carChoice]['highway-mpg'] > averagehighway:
    print(f"Your car's highway mpg ({df.iloc[carChoice]['highway-mpg']}) is HIGHER than the fleet average.")
elif df.iloc[carChoice]['highway-mpg'] < averagehighway:
    print(f"Your car's highway mpg ({df.iloc[carChoice]['highway-mpg']}) is LOWER than the fleet average.")
else:
    print(f"Your car's highway mpg ({df.iloc[carChoice]['highway-mpg']}) is the SAME as the fleet average.")

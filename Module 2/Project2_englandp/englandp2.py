# CSC 5120 Module 2 Project
# Paul England
# This program needs to:
# - Follow coding "best practices" as discussed in class for this project (use descriptive variable names, no break or continue in loops, multi-line preferred to complicated single lines of code. Aim for readability/understandably by another python developer)
# - Create a Car class file (car.py) which stores all the information about a car, plus a nickname which is set to "none" until updated later.
# - Load in the autos.json data fileDownload autos.json data file (use pandas dataframe or json load to list etc)
# - Using a for loop, and the data stored in the DataFrame, create a list of Car objects that stores all the cars as separate instances of the Car class. Do not use the DataFrame again after this step (except to graph at the end).  All other operations should use your list of Car objects.
# - Using a for loop, prompt the user the enter a nickname for each of the first 5 cars stored in your car list. If the nickname is less than 2 characters long, continue to prompt the user with a while loop until they enter a nickname 2 or more characters long.
# - Print out the first 5 cars with nickname and a couple other relevant pieces of info (city-mpg, make, and price for example).
# - Calculate the average, min and max price of all cars using a for loop and print the results.
# - Graph the price vs. horsepower for all cars (you can use the DataFrame again for this).

# Load Car, pandas, and matplotlib
from car import Car
import pandas as pd
import matplotlib.pyplot as plt

# This function will take the dataframe of autos and populate the Car class list
def CreateCarList(autos_df, debug=False):
    """This function will take the dataframe of autos and populate the Car class list."""
    # Declare the list
    carlist = []

    # Use the passed in dataframe to populate all of the cars into the carlist
    for i in range(len(autos_df)):
        currentcar = autos_df.loc[i]
        newcar = Car(aspiration=currentcar["aspiration"],
                     bodystyle=currentcar["body-style"],
                     bore=currentcar["bore"],
                     citympg=currentcar["city-mpg"],
                     compressionratio=currentcar["compression-ratio"],
                     curbweight=currentcar["curb-weight"],
                     drivewheels=currentcar["drive-wheels"],
                     enginelocation=currentcar["engine-location"],
                     enginesize=currentcar["engine-size"],
                     enginetype=currentcar["engine-type"],
                     fuelsystem=currentcar["fuel-system"],
                     fueltype=currentcar["fuel-type"],
                     height=currentcar["height"],
                     highwaympg=currentcar["highway-mpg"],
                     horsepower=currentcar["horsepower"],
                     length=currentcar["length"],
                     make=currentcar["make"],
                     normalizedlosses=currentcar["normalized-losses"],
                     numofcylinders=currentcar["num-of-cylinders"],
                     numofdoors=currentcar["num-of-doors"],
                     peakrpm=currentcar["peak-rpm"],
                     price=currentcar["price"],
                     stroke=currentcar["stroke"],
                     symboling=currentcar["symboling"],
                     wheelbase=currentcar["wheel-base"],
                     width=currentcar["width"])
        carlist.append(newcar)

    if debug:
        if len(autos_df) == len(carlist):
            print(f"There are {len(carlist)} cars in the list of cars.\n")
        else:
            print(f"There was an issue loading all of the cars: {len(autos_df)} vs {len(carlist)}\n")

    return carlist

# Function assigns a nickname to a car, making sure it is a valid length
def GetNickname(car, carnumber):
    """Function assigns a nickname to a car.  The nickname must be at least 2 characters long."""
    # Start with an empty nickname so the while loop runs at least once
    nickname = ""

    # Loop until the nickname is 2 or more characters
    while len(nickname) < 2:
        nickname = input(f"Please enter a nickname for car #{carnumber} ({car.make}): ")
        # Only show the warning when the entry is actually too short
        if len(nickname) < 2:
            print("Nickname must be at least 2 characters.  Please try again.")

    return nickname

# Function for printing the first x number of cars
def PrintFirstCars(carlist, numbertoprint):
    """Function for printing the first x number of cars."""
    print(f"\nHere are the first {numbertoprint} cars:")
    for i in range(numbertoprint):
        # This should use the Car class __str__ method
        print(carlist[i])

# Function determines the average, minimum, and maximum price across the car list; cars with no price are skipped.
def CalculatePriceStats(carlist, debug=False):
    """Function determines the average, minimum, and maximum price across the car list; cars with no price are skipped."""
    # Declare the variables
    totalprice = 0.0
    avgprice = 0.0
    # Setting MinPrice and MaxPrice to None instead of 0.0 because they could be any value, including 0
    minprice = None
    maxprice = None
    pricedcars = 0
    carswithnoprice = 0

    # Loop through the list of cars.  Ignore any car that has no listed price (NaN).
    for currentcar in carlist:
        if pd.notna(currentcar.price):
            totalprice += currentcar.price
            pricedcars += 1
            if minprice is None or currentcar.price < minprice:
                minprice = currentcar.price
            if maxprice is None or currentcar.price > maxprice:
                maxprice = currentcar.price
        else:
            carswithnoprice += 1

    # Determine the average
    if pricedcars != 0:
        avgprice = totalprice / pricedcars

    # Show the work when debug is on, same idea as Module 1
    if debug:
        print("\ntotalprice:  ", totalprice)
        print("avgprice:  ", avgprice)
        print("minprice:  ", minprice)
        print("maxprice:  ", maxprice)
        print("pricedcars:  ", pricedcars)
        print("carswithnoprice:  ", carswithnoprice)
        print(f"Total Cars In List:  {pricedcars+carswithnoprice}\n")

    return avgprice, minprice, maxprice

# Display a scatter plot of price vs. horsepower for all cars.
def CreatePriceVsHorsepowerPlot(autos_df):
    """Display a scatter plot of price vs. horsepower for all cars."""
    # Cars missing a price or horsepower are simply left off the plot
    plt.figure(figsize=(10, 6))
    plt.scatter(autos_df["horsepower"], autos_df["price"])
    plt.title("Car Price vs. Horsepower")
    plt.xlabel("Horsepower")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Start of the main portion of the program
# Loading autos.json into a dataframe
cars_df = pd.read_json("autos.json")

# Print the number of cars in the autos.json file - should be 205.  Doing two ways as a double check and practice.
print(f"Number of cars in autos.json:  {cars_df["make"].count()} = {len(cars_df)}\n")

# Load the dataframe of autos into a list
CarList = CreateCarList(cars_df,True)
print(f"Number of cars in CarList and Car.NumberOfCars:  {len(CarList)} = {Car.NumberOfCars}\n")

# Assign nicknames to the first 5 autos in the list.  Not going to be fancy and let the user decide how many.
NumberOfNicknames = 5
for i in range(NumberOfNicknames):
    NewNickname = GetNickname(CarList[i], i + 1)
    CarList[i].updatenickname(NewNickname)

# Print the first 5 autos with nicknames
PrintFirstCars(CarList, NumberOfNicknames)

# Calculate and print the average, minimum, and max price of all cars
AveragePrice, MinimumPrice, MaximumPrice = CalculatePriceStats(CarList, True)
print(f"Price stats across all {len(CarList)} cars (cars with no listed price are skipped):")
print(f"  Average price:  ${AveragePrice:,.2f}")
print(f"  Minimum price:  ${MinimumPrice:,.2f}")
print(f"  Maximum price:  ${MaximumPrice:,.2f}\n")

# Show the honksat method
for i in range(NumberOfNicknames-1):
    CarList[i].honksat(CarList[i+1])
CarList[4].honksat(CarList[0])
print("Ope, looks like a traffic jam!\n")

# Display the price versus horsepower scatter plot.
CreatePriceVsHorsepowerPlot(cars_df)

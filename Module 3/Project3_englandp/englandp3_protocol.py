# CSC 5120 Module 3 Project
# Paul England
# Instructions
# The goal of the third project is to explore the concepts of duck typing, inheritance, and testing. In this project,
# you are expected to use the following: code comments, variables, if statements, for loops, while loops, user input,
# import statements, Protocol (duck typing), functions, and inheritance. Your project will have several files.
#
# This file is the driver file that handles the user interaction and the vehicle creation.
# - Use a while loop that presents the user with a number list for which vehicle to add, or 4 for done. If the users
# enters anything but 1-4, they should get an error message and try again. You should prompt the user to enter values to fully customize the vehicle they are creating.
# - Store the added vehicles in a list
# - Use a for loop to print out the range of each vehicle (along with an indication of vehicle type).

# Bring in the class definitons
from vehicle_protocol import VehicleProtocol, Car, Train, Plane


# Create the function that generates a list of vehicles based on user input.
def addvehicles(vehiclelist):
    """Creates a list of vehicles based on user inputs."""
    keepgoing = True

    while keepgoing:
        print("1 - Add a car")
        print("2 - Add a train")
        print("3 - Add a plane")
        print("4 - Exit")

        vehiclechoice = input("Enter the number of your choice (1-4): ")

        if vehiclechoice == "1":
            fuelcapacity = float(input("Enter the fuel capacity of the car: "))
            mpg = float(input("Enter the mpg of the car: "))
            numberofpassengers = int(input("Enter the number of passengers of the car: "))
            horsepower = int(input("Enter the horsepower of the car: "))
            vehiclelist.append(Car(fuelcapacity, mpg, numberofpassengers, horsepower))
        elif vehiclechoice == "2":
            fuelcapacity = float(input("Enter the fuel capacity of the train: "))
            mpg = float(input("Enter the mpg of the train: "))
            numberofpassengers = int(input("Enter the number of passengers of the train: "))
            railtype = input("Enter the rail type of the train: ")
            vehiclelist.append(Train(fuelcapacity, mpg, numberofpassengers, railtype))
        elif vehiclechoice == "3":
            fuelcapacity = float(input("Enter the fuel capacity of the plane: "))
            mpg = float(input("Enter the mpg of the plane: "))
            numberofpassengers = int(input("Enter the number of passengers of the plane: "))
            vehiclelist.append(Plane(fuelcapacity, mpg, numberofpassengers))
        elif vehiclechoice == "4":
            keepgoing = False
        else:
            print("Please enter a valid input.")

        print()

    return vehiclelist


# Create the function that will print the range of the vehicles.
def printvehicles(vehiclelist, debug):
    """Prints the range of the vehicles in the list."""
    for vehicle in vehiclelist:
        # Enforce the protocol at runtime before using the vehicle.
        if isinstance(vehicle, VehicleProtocol):
            if isinstance(vehicle, Car):
                print(f"Car - Range:  {vehicle.getrange()} miles.")
            elif isinstance(vehicle, Train):
                print(f"Train - Range:  {vehicle.getrange()} miles.")
            elif isinstance(vehicle, Plane):
                print(f"Plane - Range:  {vehicle.getrange()} miles.")
            else:
                print("The vehicle type doesn't exist.")
        else:
            print(f"Not a vehicle: {type(vehicle)}")

    if debug:
        print("\nThese are the vehicles and their attributes in the list.")
        for vehicle in vehiclelist:
            print(vehicle)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    VehicleList = []
    Debug = True

    addvehicles(VehicleList)
    printvehicles(VehicleList, Debug)

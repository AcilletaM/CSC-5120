# CSC 5120 Module 7 Project
# Paul England
# Instructions
#
# The goal of the seventh project is to compare the "step" and timing results for storing and retrieving data from two different data structures: the singly linked list 
# we developed in class and a built in Python Array. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert and retrieval methods. 
#
# Write Python code that generates a 10,000 random numbers between 1 and 1,000,000. 
#   - Store those numbers in an instance of our singly linked list, and the same set of numbers in a Python array (a python list []). 
#   - Count the number of steps (as we discussed in class) for the linked list add operation, and compare it to n (which is 10,000 here at the end, but is smaller for earlier adds).
#   - Time how long it takes to insert all 10,000 numbers for both the linked list and the array, compare (print out explanations) this to each other and to the number of steps for LL.
#   - Pick a number that you know is stored as one of the 10,000 entries near the beginning of the batch, and retrieve (get) it by index for both array and LL, counting steps for the linked list get and timing both while you do. Analyze the results (print out explanations).
#   - Retrieve the 7000th number for the LL and from the Array, counting steps and timing while you do. Analyze the results.
#
# Consider the following questions, and provide answers in a text file included with your submission:
#   - Which data structure is better at insertion, which is better at retrieval of the nth (7000th in our case) number?
#   - Which would be better at deletion of the nth number? The 1st number?

# Bring in the class definitons
from vehicle import Car, Train, Plane

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
        if isinstance(vehicle, Car):
            print(f"Car - Range:  {vehicle.getrange()} miles.")
        elif isinstance(vehicle, Train):
            print(f"Train - Range:  {vehicle.getrange()} miles.")
        elif isinstance(vehicle, Plane):
            print(f"Plane - Range:  {vehicle.getrange()} miles.")
        else:
            print("The vehicle type doesn't exist.")

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

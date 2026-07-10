# CSC 5120 Module 3 Project
# Paul England
# Instructions
# The goal of the third project is to explore the concepts of duck typing, inheritance, and testing. In this project,
# you are expected to use the following: code comments, variables, if statements, for loops, while loops, user input,
# import statements, Protocol (duck typing), functions, and inheritance. Your project will have several files.
#
# This file contains the definitions of several vehicle-related classes.  It contains the definitions of the Vehicle,
# Car, Train, and Plane classes.  Each class contains a constructor.  Vehicle is the parent class while Car, Train, and
# Plane are child classes.  The three child classes all inherit the 3 attributes from Vehicle.  Vehicle also contains a
# method that calculates the range based on the fuel capacity and mpg.
# - Create a vehicle class that defines a fuel capacity attribute, and miles per gallon attribute, a passengers
#   attribute, and a getRange function.
# - Create Car, Train and Plane classes that inherit from Vehicle (and so implement the getRange) and add the following
#   functionality:
#       - for Car add horsepower
#       - for Train add railType
#       - for plane the getRange function should account for using 10% of the fuel for takeoff.
from abc import ABC, abstractmethod


class Vehicle(ABC):
    # Constructor
    def __init__(self, fuelcapacity, mpg, numberofpassengers):
        """Initialize a Vehicle with all of its fields."""
        self.fuelcapacity = fuelcapacity
        self.mpg = mpg
        self.numberofpassengers = numberofpassengers

    # Each vehicle type must supply its own range calculation.
    @abstractmethod
    def getrange(self):
        """Calculate the range; each vehicle subclass must implement this."""
        pass

    # Gives a sample of characteristics for one vehicle
    def __str__(self) -> str:
        """Return a sample of characteristics of the specified vehicle."""
        result = f"{self.fuelcapacity}, {self.mpg}, {self.numberofpassengers}"
        return result

    # printable representation used when a Vehicle is shown from inside a list
    def __repr__(self):
        """Return the representation used when a Vehicle is printed from a list."""
        result = f"{self.fuelcapacity}, {self.mpg}, {self.numberofpassengers}"
        return result


class Car(Vehicle):
    # Constructor
    def __init__(self, fuelcapacity, mpg, numberofpassengers, horsepower):
        """Initialize a Car with all of Vehicle's fields plus the Car specific horsepower."""
        super().__init__(fuelcapacity, mpg, numberofpassengers)
        self.horsepower = horsepower

    # Calculate the range using the mpg and the fuel capacity.
    def getrange(self):
        """Calculate the range using mpg and the fuel capacity."""
        return self.mpg * self.fuelcapacity

    # Gives a sample of characteristics for one car
    def __str__(self) -> str:
        """Return a sample of characteristics of the specified car."""
        result = f"Car {super().__str__()}, {self.horsepower}"
        return result

    # printable representation used when a Car is shown from inside a list
    def __repr__(self):
        """Return the representation used when a Car is printed from a list."""
        result = f"Car {super().__repr__()}, {self.horsepower}"
        return result


class Train(Vehicle):
    # Constructor
    def __init__(self, fuelcapacity, mpg, numberofpassengers, railtype):
        """Initialize a Train with all of Vehicle's fields plus the Train specific railtype."""
        super().__init__(fuelcapacity, mpg, numberofpassengers)
        self.railtype = railtype

    # Calculate the range using the mpg and the fuel capacity.
    def getrange(self):
        """Calculate the range using mpg and the fuel capacity."""
        return self.mpg * self.fuelcapacity

    # Gives a sample of characteristics for one train
    def __str__(self) -> str:
        """Return a sample of characteristics of the specified train."""
        result = f"Train {super().__str__()}, {self.railtype}"
        return result

    # printable representation used when a Train is shown from inside a list
    def __repr__(self):
        """Return the representation used when a Train is printed from a list."""
        result = f"Train {super().__repr__()}, {self.railtype}"
        return result


class Plane(Vehicle):
    # Calculate the range using the mpg and the fuel capacity.
    def getrange(self):
        """Calculate the range using mpg and the fuel capacity but only 90% because of fuel usage at takeoff."""
        return (self.mpg * self.fuelcapacity) * 0.9

    # Gives a sample of characteristics for one plane
    def __str__(self) -> str:
        """Return a sample of characteristics of the specified plane."""
        result = f"Plane {super().__str__()}"
        return result

    # printable representation used when a Plane is shown from inside a list
    def __repr__(self):
        """Return the representation used when a Plane is printed from a list."""
        result = f"Plane {super().__repr__()}"
        return result

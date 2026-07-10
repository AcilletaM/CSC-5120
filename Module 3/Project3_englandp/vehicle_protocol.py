# CSC 5120 Module 3 Project
# Paul England
# Instructions
# The goal of the third project is to explore the concepts of duck typing, inheritance, and testing. In this project,
# you are expected to use the following: code comments, variables, if statements, for loops, while loops, user input,
# import statements, Protocol (duck typing), functions, and inheritance. Your project will have several files.
#
# This file contains the definitions of several vehicle-related classes.  It contains the definitions of the Vehicle,
# Car, Train, and Plane classes.
# Create a separate Python file and refactor the project using Protocol instead of inheritance.
# - I am looking for a separate file that contains the protocol definition and your “driver code” cut and paste from
#   your original file, with any changes you may need to make. You can still use the train, plane, and car classes, or
#   you may need to make new versions of them. All the code associated with the protocol portion, including modified
#   versions of your plane, train, and car classes (if needed) can go into this single other file
from typing import Protocol, runtime_checkable


@runtime_checkable
class VehicleProtocol(Protocol):
    def getrange(self) -> float:
        ...


class Car:
    # Constructor
    def __init__(self, fuelcapacity: float, mpg: int, numberofpassengers: int, horsepower: int):
        """Initialize a Car with all of Vehicle's fields plus the Car specific horsepower."""
        self.fuelcapacity = fuelcapacity
        self.mpg = mpg
        self.numberofpassengers = numberofpassengers
        self.horsepower = horsepower

    # Calculate the range using the mpg and the fuel capacity.
    def getrange(self) -> float:
        """Calculate the range using mpg and the fuel capacity."""
        return self.mpg * self.fuelcapacity

    # Gives a sample of characteristics for one car
    def __str__(self) -> str:
        """Return a sample of characteristics of the specified car."""
        result = f"Car {self.fuelcapacity}, {self.mpg}, {self.numberofpassengers}, {self.horsepower}"
        return result

    # printable representation used when a Car is shown from inside a list
    def __repr__(self):
        """Return the representation used when a Car is printed from a list."""
        result = f"Car {self.fuelcapacity}, {self.mpg}, {self.numberofpassengers}, {self.horsepower}"
        return result


class Train:
    # Constructor
    def __init__(self, fuelcapacity: float, mpg: int, numberofpassengers: int, railtype: str):
        """Initialize a Train with all of Vehicle's fields plus the Train specific railtype."""
        self.fuelcapacity = fuelcapacity
        self.mpg = mpg
        self.numberofpassengers = numberofpassengers
        self.railtype = railtype

    # Calculate the range using the mpg and the fuel capacity.
    def getrange(self) -> float:
        """Calculate the range using mpg and the fuel capacity."""
        return self.mpg * self.fuelcapacity

    # Gives a sample of characteristics for one train
    def __str__(self) -> str:
        """Return a sample of characteristics of the specified train."""
        result = f"Train {self.fuelcapacity}, {self.mpg}, {self.numberofpassengers}, {self.railtype}"
        return result

    # printable representation used when a Train is shown from inside a list
    def __repr__(self):
        """Return the representation used when a Train is printed from a list."""
        result = f"Train {self.fuelcapacity}, {self.mpg}, {self.numberofpassengers}, {self.railtype}"
        return result


class Plane:
    # Constructor
    def __init__(self, fuelcapacity: float, mpg: int, numberofpassengers: int):
        """Initialize a Plane with all of Vehicle's fields."""
        self.fuelcapacity = fuelcapacity
        self.mpg = mpg
        self.numberofpassengers = numberofpassengers

    # Calculate the range but only 90% because of fuel usage at takeoff.
    def getrange(self) -> float:
        """Calculate the range using mpg and the fuel capacity but only 90% because of fuel usage at takeoff."""
        return (self.mpg * self.fuelcapacity) * 0.9

    # Gives a sample of characteristics for one plane
    def __str__(self) -> str:
        """Return a sample of characteristics of the specified plane."""
        result = f"Plane {self.fuelcapacity}, {self.mpg}, {self.numberofpassengers}"
        return result

    # printable representation used when a Plane is shown from inside a list
    def __repr__(self):
        """Return the representation used when a Plane is printed from a list."""
        result = f"Plane {self.fuelcapacity}, {self.mpg}, {self.numberofpassengers}"
        return result

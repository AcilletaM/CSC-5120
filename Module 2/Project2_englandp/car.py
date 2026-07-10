# CSC 5120 Module 2 Project
# Paul England
# Instructions
# The goal of the second project is to modify our first project to use a Car class (defined in a separate car.py file).
# In this project, you are expected to use the following: code comments, variables, if statements, for loops, while
# loops, user input, import statements, file input, functions, and a Car class.
#
# This file contains the definition of the car class called Car.  It contains the 26 fields in the autos.json plus an
# extra field called nickname.  It contains the constructor, a method to set the nickname, and a method that is a
# car honking its horn at another.
class Car:
    # class variable that counts how many Car objects currently exist
    NumberOfCars = 0

    # Fields mirror the same order they appear in autos.json
    def __init__(self, aspiration, bodystyle, bore, citympg, compressionratio,
                 curbweight, drivewheels, enginelocation, enginesize, enginetype,
                 fuelsystem, fueltype, height, highwaympg, horsepower, length,
                 make, normalizedlosses, numofcylinders, numofdoors, peakrpm,
                 price, stroke, symboling, wheelbase, width, nickname="none"):
        """Initialize a Car with all of its fields - nickname is optional and defaults to "none"."""
        self.aspiration = aspiration
        self.bodystyle = bodystyle
        self.bore = bore
        self.citympg = citympg
        self.compressionratio = compressionratio
        self.curbweight = curbweight
        self.drivewheels = drivewheels
        self.enginelocation = enginelocation
        self.enginesize = enginesize
        self.enginetype = enginetype
        self.fuelsystem = fuelsystem
        self.fueltype = fueltype
        self.height = height
        self.highwaympg = highwaympg
        self.horsepower = horsepower
        self.length = length
        self.make = make
        self.normalizedlosses = normalizedlosses
        self.numofcylinders = numofcylinders
        self.numofdoors = numofdoors
        self.peakrpm = peakrpm
        self.price = price
        self.stroke = stroke
        self.symboling = symboling
        self.wheelbase = wheelbase
        self.width = width
        self.nickname = nickname

        # Increment the number of cars
        Car.NumberOfCars += 1

    def updatenickname(self, nickname):
        """Update the car's nickname."""
        self.nickname = nickname

    # Example of a method where the cars interact
    def honksat(self, other):
        """Print a message that this car honks at another car."""
        print(f"{self.nickname} honks at {other.nickname}.")

    # Gives a sample of characteristics for one car
    def __str__(self) -> str:
        """Return a sample of characteristics of the specified car."""
        result = f"Car '{self.nickname}' - aspiration: {self.aspiration}, make: {self.make}, body-style: {self.bodystyle}, city-mpg: {self.citympg}, highway-mpg: {self.highwaympg}, price: ${self.price:,.2f}"
        return result

    # printable representation used when a Car is shown from inside a list
    def __repr__(self):
        """Return the representation used when a Car is printed from a list."""
        result = f"Car '{self.nickname}' is a {self.make} that costs ${self.price:,.2f}"
        return result

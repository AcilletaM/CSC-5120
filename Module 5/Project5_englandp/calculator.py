# CSC 5120 Module 5 Project
# Paul England
# Instructions
# The goal of the fifth project is to create a command line calculator program. The program should take 3 command line
# arguments in the form: number operation number
# We will be creating an external calculator class in its own file, with the functions that handle the math, and
# importing it into our driver file. You should also write tests for all the functions in your calculator class. Number
# inputs can be integers or decimal numbers and you should support the following operations +, -, x, /, %, ^.
#
# *Note that multiplication, the * sign, may cause issues, so you can require an x or some other work around instead.
#
# This file is the Calculator class file that contains the actual math methods.
#   - Create a separate calculator class with the functions that handle the math.
#   - Support the following operations +, -, x, /, %, ^

class Calculator:
    """Class that performs the mathematical calculations requested through the calculator."""

    # No __init__ because we don't need values stored.

    def add(self, num1, num2):
        """Return the sum of the two numbers."""
        return num1 + num2

    def subtract(self, num1, num2):
        """Return the difference of the two numbers."""
        return num1 - num2

    def multiply(self, num1, num2):
        """Return the product of the two numbers."""
        return num1 * num2

    def divide(self, num1, num2):
        """Return the quotient of the two numbers."""
        return num1 / num2

    def modulo(self, num1, num2):
        """Return the remainder of the two numbers after division."""
        return num1 % num2

    def power(self, num1, num2):
        """Return num1 raised to the power num2."""
        return num1 ** num2

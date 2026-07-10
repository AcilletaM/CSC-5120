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
# This file is the driver file that handles the user interaction.
#   - Create a main.py Python script that takes 3 command line arguments in the form: number operation number
#   - Your program should produce helpful error messages when the input values are not properly formatted.
#   - Create a separate calculator class with the functions that handle the math.
#   - Support the following operations +, -, x, /, %, ^
#   - Create tests for all functions, and include a test_classname for each class. The instructor may also provide some
#     tests classes to use/test you code with.

# Import sys
import sys

# Bring in the class definitions
from calculator import Calculator

def showhelp():
    """Print a help message for this module."""
    print("Usage: python main.py <number> <operation> <number>")
    print("  number    : an integer or a decimal number (example: 4 or 2.5)")
    print("  operation : one of + - x / % ^")
    print("Note: use 'x' for multiplication because the shell expands an unquoted '*'.\n")
    print("To see this message again run:  python main.py --help")

def isnumber(number):
    """If the number is not valid, return False."""
    convert_to_text = number

    # Remove extra characters that could interfere with the number check
    if convert_to_text.startswith("-") or convert_to_text.startswith("+"):
        convert_to_text = convert_to_text[1:]

    # If there is no value it can't be a valid number
    if convert_to_text == "":
        return False

    # If they only have a decimal point
    if convert_to_text == ".":
        return False

    # If they have too many decimal points
    if convert_to_text.count(".") > 1:
        return False

    # Convert floats to a integer and check
    convert_to_text = convert_to_text.replace(".", "")
    return convert_to_text.isdigit()

def numparse(number):
    """Determine the number type and return as either an int or float."""
    # If it has a decimal point it is a float otherwise it is an int.
    if "." in number:
        return float(number)

    return int(number)

def main():
    """Read the command line arguments, perform the requested calculation, and return the result.  Show the help message if requested."""
    # Validate the number of arguments passed in.  Handle errors and --help.
    if len(sys.argv) != 4:
        if len(sys.argv) > 4:
            print("Error:  Expected 3 arguments but more were given.\n")
        elif len(sys.argv) < 2 or sys.argv[1] != "--help":
            print("Error:  Expected 3 arguments but not enough were given.\n")

        showhelp()
        return

    # Assign the command line arguments.
    first_number = sys.argv[1]
    operator = sys.argv[2]
    second_number = sys.argv[3]

    # Validate the first number.
    if not isnumber(first_number):
        print("Error:  First number must be a valid integer or decimal number.")
        return

    # Validate the second number.
    if not isnumber(second_number):
        print("Error:  Second number must be a valid integer or decimal number.")
        return

    # Convert to int or float.
    first_number = numparse(first_number)
    second_number = numparse(second_number)

    # Create a calculator class instance.
    calc_class = Calculator()

    # Perform the appropriate calculation.  Do additional error handling for special cases.
    if operator == "+":
        result = calc_class.add(first_number, second_number)
    elif operator == "-":
        result = calc_class.subtract(first_number, second_number)
    elif operator in ["x", "X", "*"]:
        result = calc_class.multiply(first_number, second_number)
    elif operator == "/":
        if second_number == 0:
            print("Error: division by zero.\n")
            return

        result = calc_class.divide(first_number, second_number)
    elif operator in ["%", "mod", "MOD"]:
        if second_number == 0:
            print("Error: division by zero.\n")
            return

        result = calc_class.modulo(first_number, second_number)
    elif operator == "^":
        if first_number == 0 and second_number < 0:
            print("Error: cannot raise zero to a negative power.\n")
            return

        result = calc_class.power(first_number, second_number)
    else:
        print("Error:  Invalid operation.\n")
        showhelp()
        return

    # Show the result.
    print(f"{first_number} {operator} {second_number} = {result}")

    return

if __name__ == '__main__':
    main()

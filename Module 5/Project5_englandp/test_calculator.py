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
# This is the test file.


# import sys and pytest
import sys
import pytest

# Bring in the class definition and functions to test
from calculator import Calculator
from main import isnumber, numparse, main


class TestCalculator:
    """Test every math function in the Calculator class."""

    @pytest.fixture
    def calc(self):
        """Provide a Calculator instance for the tests."""
        return Calculator()

    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 8),
        (-5, 3, -2),
        (2.5, 0.25, 2.75),
        (0, 0, 0),
    ])
    def test_add(self, calc, num1, num2, expected):
        """Verify add returns the correct sum."""
        assert calc.add(num1, num2) == pytest.approx(expected)

    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 2),
        (3, 5, -2),
        (2.5, 0.5, 2.0),
        (-1, -1, 0),
    ])
    def test_subtract(self, calc, num1, num2, expected):
        """Verify subtract returns the correct difference."""
        assert calc.subtract(num1, num2) == pytest.approx(expected)

    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 15),
        (-5, 3, -15),
        (2.5, 4, 10.0),
        (5, 0, 0),
    ])
    def test_multiply(self, calc, num1, num2, expected):
        """Verify multiply returns the correct product."""
        assert calc.multiply(num1, num2) == pytest.approx(expected)

    @pytest.mark.parametrize("num1, num2, expected", [
        (6, 3, 2.0),
        (5, 2, 2.5),
        (-6, 3, -2.0),
        (0.5, 0.25, 2.0),
    ])
    def test_divide(self, calc, num1, num2, expected):
        """Verify divide returns the correct quotient."""
        assert calc.divide(num1, num2) == pytest.approx(expected)

    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 2),
        (10, 2, 0),
        (-5, 3, 1),  # Python uses floor modulo, so -5 % 3 is 1
        (5.5, 2, 1.5),
    ])
    def test_modulo(self, calc, num1, num2, expected):
        """Verify modulo returns the correct remainder."""
        assert calc.modulo(num1, num2) == pytest.approx(expected)

    @pytest.mark.parametrize("num1, num2, expected", [
        (2, 3, 8),
        (5, 0, 1),
        (2, -1, 0.5),
        (9, 0.5, 3.0),
    ])
    def test_power(self, calc, num1, num2, expected):
        """Verify power returns the correct result."""
        assert calc.power(num1, num2) == pytest.approx(expected)


class TestMain:
    """Test the driver's validation, dispatch, and error messages in main.py."""

    @pytest.mark.parametrize("value, expected", [
        ("5", True),
        ("-3", True),
        ("+7", True),
        ("2.5", True),
        ("-0.5", True),
        (".5", True),
        ("abc", False),
        ("1.2.3", False),
        ("", False),
        ("-", False),
        (".", False),
        ("5-3", False),
    ])
    def test_isnumber(self, value, expected):
        """Verify isnumber accepts valid number strings and rejects bad ones."""
        assert isnumber(value) == expected

    def test_numparse_returns_int(self):
        """Verify numparse returns an int for whole number input."""
        result = numparse("5")
        assert result == 5
        assert isinstance(result, int)

    def test_numparse_returns_float(self):
        """Verify numparse returns a float for decimal input."""
        result = numparse("2.5")
        assert result == 2.5
        assert isinstance(result, float)

    def test_numparse_negative_values(self):
        """Verify numparse handles negative integers and decimals."""
        assert numparse("-3") == -3
        assert numparse("-0.5") == -0.5

    def test_main_addition(self, monkeypatch, capsys):
        """Verify main prints the correct result for a valid addition."""
        monkeypatch.setattr(sys, "argv", ["main.py", "5", "+", "3"])
        main()
        captured = capsys.readouterr()
        assert "5 + 3 = 8" in captured.out

    def test_main_multiplication_with_x(self, monkeypatch, capsys):
        """Verify main accepts x for multiplication."""
        monkeypatch.setattr(sys, "argv", ["main.py", "4", "x", "2.5"])
        main()
        captured = capsys.readouterr()
        assert "4 x 2.5 = 10.0" in captured.out

    def test_main_mod_alias(self, monkeypatch, capsys):
        """Verify main accepts the mod alias for modulo."""
        monkeypatch.setattr(sys, "argv", ["main.py", "10", "mod", "3"])
        main()
        captured = capsys.readouterr()
        assert "10 mod 3 = 1" in captured.out

    def test_main_negative_number_argument(self, monkeypatch, capsys):
        """Verify main handles a negative number argument."""
        monkeypatch.setattr(sys, "argv", ["main.py", "-5", "+", "3"])
        main()
        captured = capsys.readouterr()
        assert "-5 + 3 = -2" in captured.out

    def test_main_help_flag(self, monkeypatch, capsys):
        """Verify main shows help without an error message for --help."""
        monkeypatch.setattr(sys, "argv", ["main.py", "--help"])
        main()
        captured = capsys.readouterr()
        assert "Usage:" in captured.out
        assert "Error" not in captured.out

    def test_main_no_arguments(self, monkeypatch, capsys):
        """Verify main prints a helpful message when run with no arguments."""
        monkeypatch.setattr(sys, "argv", ["main.py"])
        main()
        captured = capsys.readouterr()
        assert "Expected 3 arguments" in captured.out
        assert "Usage:" in captured.out

    def test_main_missing_argument(self, monkeypatch, capsys):
        """Verify main prints a helpful message when an argument is missing."""
        monkeypatch.setattr(sys, "argv", ["main.py", "5", "+"])
        main()
        captured = capsys.readouterr()
        assert "not enough were given" in captured.out
        assert "Usage:" in captured.out

    def test_main_too_many_arguments(self, monkeypatch, capsys):
        """Verify main prints a helpful message when extra arguments arrive."""
        monkeypatch.setattr(sys, "argv", ["main.py", "5", "x", "3", "4"])
        main()
        captured = capsys.readouterr()
        assert "more were given" in captured.out

    def test_main_invalid_first_number(self, monkeypatch, capsys):
        """Verify main prints a helpful message for a bad first number."""
        monkeypatch.setattr(sys, "argv", ["main.py", "abc", "+", "3"])
        main()
        captured = capsys.readouterr()
        assert "First number must be a valid" in captured.out

    def test_main_invalid_second_number(self, monkeypatch, capsys):
        """Verify main prints a helpful message for a bad second number."""
        monkeypatch.setattr(sys, "argv", ["main.py", "5", "+", "abc"])
        main()
        captured = capsys.readouterr()
        assert "Second number must be a valid" in captured.out

    def test_main_invalid_operation(self, monkeypatch, capsys):
        """Verify main prints a helpful message for a bad operation."""
        monkeypatch.setattr(sys, "argv", ["main.py", "5", "?", "3"])
        main()
        captured = capsys.readouterr()
        assert "Invalid operation" in captured.out

    def test_main_divide_by_zero(self, monkeypatch, capsys):
        """Verify main prints a helpful message on division by zero."""
        monkeypatch.setattr(sys, "argv", ["main.py", "5", "/", "0"])
        main()
        captured = capsys.readouterr()
        assert "division by zero" in captured.out

    def test_main_modulo_by_zero(self, monkeypatch, capsys):
        """Verify main prints a helpful message on modulo by zero."""
        monkeypatch.setattr(sys, "argv", ["main.py", "5", "%", "0"])
        main()
        captured = capsys.readouterr()
        assert "division by zero" in captured.out

    def test_main_zero_to_negative_power(self, monkeypatch, capsys):
        """Verify main prints a helpful message for zero to a negative power."""
        monkeypatch.setattr(sys, "argv", ["main.py", "0", "^", "-1"])
        main()
        captured = capsys.readouterr()
        assert "cannot raise zero to a negative power" in captured.out

    def test_main_subtraction(self, monkeypatch, capsys):
        """Verify main prints the correct result for a valid subtraction."""
        monkeypatch.setattr(sys, "argv", ["main.py", "5", "-", "3"])
        main()
        captured = capsys.readouterr()
        assert "5 - 3 = 2" in captured.out

    def test_main_division(self, monkeypatch, capsys):
        """Verify main prints the correct result for a valid division."""
        monkeypatch.setattr(sys, "argv", ["main.py", "7", "/", "2"])
        main()
        captured = capsys.readouterr()
        assert "7 / 2 = 3.5" in captured.out

    def test_main_power(self, monkeypatch, capsys):
        """Verify main prints the correct result for a valid power."""
        monkeypatch.setattr(sys, "argv", ["main.py", "2", "^", "10"])
        main()
        captured = capsys.readouterr()
        assert "2 ^ 10 = 1024" in captured.out
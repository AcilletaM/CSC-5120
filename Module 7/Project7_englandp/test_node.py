# CSC 5120 Module 7 Project
# Paul England
# Instructions
# The goal of the seventh project is to compare the "step" and timing results for storing and retrieving data from two
# different data structures: the singly linked list we developed in class and a built in Python Array. We will also
# analyze the Big O upper bound (in terms of the n items stored) for our insert and retrieval methods.
#
# This file contains the tests of the Node class.  These are the tests:
# - A new node stores the data it was given.
# - A new node does not link to another node yet.
# - A node returns its data.  This also tests different data types can be saved in a Node.

# Load pytest, Node, and LinkedList.
import pytest
from node import Node

# Test initial Node setup.
def teststoresdata():
    """Validate the Node stores the data passed to it."""
    assert Node(5).data == 5

def teststartsempty():
    """Validate a new node does not link to anything yet."""
    assert Node(5).next is None

@pytest.mark.parametrize(
    "data, expected",
    [
        (5, "5"),           # integer
        (2.5, "2.5"),       # float
        ("text", "text"),   # a string passes straight through
        (None, "None"),     # even an empty value prints readably
    ],
)
def teststrreturnscontents(data, expected):
    """Validate a node returns its data.  This also tests different data types can be saved. (parameterize)."""
    assert str(Node(data)) == expected

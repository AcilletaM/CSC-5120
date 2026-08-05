# CSC 5120 Module 8 Project
# Paul England
# Instructions
#
# The goal of the eighth project is to collect and analyze the "step" and timing results for storing and retrieving data
# from a binary search tree. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert
# and retrieval methods.
#
# This file contains the tests of the Node class.  These are the tests:
# - A new node stores the data it was given.
# - A new node stores the key it was given.
# - A new node does not link to another node yet.
# - A node returns its data.  This also tests different data types can be saved in a Node.

# Load pytest and Node.
import pytest
from node import Node

# Test initial Node setup.
def teststoresdata():
    """Validate the Node stores the data passed to it."""
    assert Node(1,5).data == 5

# Test initial Node setup.
def teststoreskey():
    """Validate the Node stores the key passed to it."""
    assert Node(1,5).key == 1

def teststartsempty():
    """Validate a new node does not link to anything yet."""
    node = Node(1,5)
    assert node.left is None
    assert node.right is None

@pytest.mark.parametrize(
    "key, data, expected",
    [
        (1,5, "5"),           # integer
        (2,2.5, "2.5"),       # float
        (3,"text", "text"),   # a string passes straight through
        (4,None, "None"),     # even an empty value prints readably
    ],
)
def teststrreturnscontents(key,data, expected):
    """Validate a node returns its data.  This also tests different data types can be saved. (parameterize)."""
    assert str(Node(key,data)) == expected

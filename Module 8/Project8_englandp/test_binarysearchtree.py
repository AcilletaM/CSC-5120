# CSC 5120 Module 8 Project
# Paul England
# Instructions
#
# The goal of the eighth project is to collect and analyze the "step" and timing results for storing and retrieving data
# from a binary search tree. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert
# and retrieval methods.
#
# This file contains the tests of the BTS class.  These are the tests:
# - A new binary search tree is empty by using isEmpty.
# - A new binary search tree is empty by using len.
# - A new binary search tree is empty by using size.
# - Adding to an empty binary search tree makes it no longer empty.
# - The length is 1 when the initial node is inserted.
# - The size attribute is 1 when the initial node is inserted.
# - The length of the binary search tree tracks the number of nodes inserted.
# - Adding the same key twice only allows one node.
# - An empty binary search tree prints a message rather than a blank string.
# - A one node binary search tree prints without a trailing arrow.
# - A binary search tree with increasing keys prints its values separated by arrows.
# - A binary search tree with decreasing keys prints its values separated by arrows.
# - A binary search tree with keys that alternate between greater than and less than prints values separated by arrows from one traversal down a branch.

# Load pytest, Node, and LinkedList.
import pytest
from node import Node
from binarysearchtree import BST

# Need to create an empty binary search tree for the next tests.
@pytest.fixture
def emptytree():
    """Provide a new empty BTS for these tests (fixture)."""
    return BST()

# Empty node tests first
def testnewtreeisempty(emptytree):
    """Validate isEmpty reports true on a newly created binary search tree (fixture)."""
    assert emptytree.isEmpty() is True

def testnewtreeiszeroength(emptytree):
    """Validate len reports zero on a newly created binary search tree (fixture)."""
    assert len(emptytree) == 0

def testnewtreesizeiszero(emptytree):
    """Validate the size attribute is 0 on a newly created binary search tree (fixture)."""
    assert emptytree.size == 0

# Single node tests next.
def testinsertisnotempty(emptytree):
    """Validate isEmpty is false when a node is inserted (fixture)."""
    emptytree.insert(1,5)
    assert emptytree.isEmpty() is False

def testinsertlengthequalsone(emptytree):
    """Validate that length is 1 when the initial node is inserted (fixture)."""
    emptytree.insert(1,5)
    assert len(emptytree) == 1

def testinsertsizenotzero(emptytree):
    """Validate the size attribute is 1 when the initial node is inserted (fixture)."""
    emptytree.insert(1,5)
    assert emptytree.size == 1

@pytest.mark.parametrize("count", [1, 2, 3, 4, 5, 10, 100])
def testinsertingmanynodes(emptytree, count):
    """Validate the insert method inserts many nodes (fixture + parameterize)."""
    loopkey = 1
    for number in range(count):
        emptytree.insert(loopkey,number)
        loopkey += 1
    assert len(emptytree) == count

def testinsertingsamedata(emptytree):
    """Validate you get one node if the data is duplicated (fixture)."""
    emptytree.insert(1,5)
    emptytree.insert(1,5)
    assert len(emptytree) == 1

def testemptyliststr(emptytree):
    """Validate an empty list prints a message instead of a blank string (fixture)."""
    assert str(emptytree) == "The binary search tree is empty."

def testsinglenodestr(emptytree):
    """Validate a one node list prints without a trailing -> (fixture)."""
    emptytree.insert(1, 10)
    print(str(emptytree))
    assert str(emptytree) == "10"

def testmultiplenodestrright(emptytree):
    """Validate a multi node list prints each value separated by ->'s (fixture)."""
    for number in (10, 20, 30):
        emptytree.insert(number, number)
    print(str(emptytree))
    assert str(emptytree) == "10 -> 20 -> 30"

def testmultiplenodestrleft(emptytree):
    """Validate a multi node list prints each value separated by ->'s (fixture)."""
    for number in (100, 40, 30):
        emptytree.insert(number, number)
    print(str(emptytree))
    assert str(emptytree) == "100 -> 40 -> 30"

def testmultiplenodestrpartright(emptytree):
    """Validate a multi node list prints each value separated by ->'s (fixture)."""
    for number in (100, 20, 200, 30, 300, 40, 400):
        emptytree.insert(number, number)
    print(str(emptytree))
    assert str(emptytree) == "100 -> 20 -> 30 -> 40"


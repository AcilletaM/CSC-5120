# CSC 5120 Module 7 Project
# Paul England
# Instructions
# The goal of the seventh project is to compare the "step" and timing results for storing and retrieving data from two
# different data structures: the singly linked list we developed in class and a built in Python Array. We will also
# analyze the Big O upper bound (in terms of the n items stored) for our insert and retrieval methods.
#
# This file contains the tests of the Node and LinkedList classes.  These are the tests:
# - A new linked list is empty by using isEmpty.
# - A new linked list is empty by using len.
# - A new linked list is empty by using size.
# - Adding to an empty list makes it no longer empty.
# - The length of the list tracks the number of nodes added.
# - Adding the same value twice creates two separate nodes.
# - Get returns a Node rather than the raw data.
# - Get walks the list in the order the values were added, which proves add appends to the end.
# - The last node in the list terminates the chain.
# - An empty list prints a message rather than a blank string.
# - A populated list prints its values separated by arrows.

# Load pytest, Node, and LinkedList.
import pytest
from node import Node
from linkedlist import LinkedList

# Need to create an empty linked list for the next tests.
@pytest.fixture
def emptylist():
    """Provide a new empty LinkedList for these tests (fixture)."""
    return LinkedList()

# Empty node tests first
def testnewlistisempty(emptylist):
    """Validate isEmpty reports true on a newly created linked list (fixture)."""
    assert emptylist.isEmpty() is True

def testnewlistiszeroength(emptylist):
    """Validate len reports zero on a newly created linked list (fixture)."""
    assert len(emptylist) == 0

def testnewlistsizeiszero(emptylist):
    """Validate the size attribute is 0 on a newly created linked list (fixture)."""
    assert emptylist.size == 0

# Single node tests next.
def testaddisnotempty(emptylist):
    """Validate isEmpty is false when a node is added (fixture)."""
    emptylist.add(5)
    assert emptylist.isEmpty() is False

def testaddlengthequalsone(emptylist):
    """Validate that length is 1 when the initial node is added (fixture)."""
    emptylist.add(5)
    assert len(emptylist) == 1

def testaddsizenotzero(emptylist):
    """Validate the size attribute is 1 when the initial node is added (fixture)."""
    emptylist.add(5)
    assert emptylist.size == 1

@pytest.mark.parametrize("count", [1, 2, 3, 10, 100])
def testlengthmatchesnumberadded(emptylist, count):
    """Validate the length tracks how many nodes were added (fixture + parameterize)."""
    for number in range(count):
        emptylist.add(number)
    assert len(emptylist) == count

def testduplicatedatacountstwice(emptylist):
    """Validate adding the same value twice creates two separate nodes (fixture)."""
    emptylist.add(5)
    emptylist.add(5)
    assert len(emptylist) == 2

# Test the printed form of the linked list.
def testemptyliststr(emptylist):
    """Validate an empty list prints a message instead of a blank string (fixture)."""
    assert str(emptylist) == "empty linked list"

def testsinglenodestr(emptylist):
    """Validate a one node list prints without a trailing arrow (fixture)."""
    emptylist.add(10)
    assert str(emptylist) == "10"

def testmultiplenodestr(emptylist):
    """Validate a multi node list prints each value separated by an arrow (fixture)."""
    for number in (10, 20, 30):
        emptylist.add(number)
    assert str(emptylist) == "10 -> 20 -> 30"

# The next tests need a list with nodes already.
@pytest.fixture
def numberlist():
    """Provide a fresh LinkedList holding 10, 20, 30, 40, 50 in that order for each test (fixture)."""
    filledlist = LinkedList()
    for number in (10, 20, 30, 40, 50):
        filledlist.add(number)
    return filledlist

def testgetreturnsanode(numberlist):
    """Validate get hands back a Node rather than the raw data (fixture)."""
    assert isinstance(numberlist.get(0), Node)

def testgetzeroreturnsfirstvalue(numberlist):
    """Validate index 0 is the head of the list (fixture)."""
    assert numberlist.get(0).data == 10

def testgetlastreturnslastvalue(numberlist):
    """Validate add appends to the end of the list rather than the front (fixture)."""
    assert numberlist.get(4).data == 50

@pytest.mark.parametrize(
    "index, expected",
    [
        (0, 10),    # head
        (1, 20),
        (2, 30),
        (3, 40),
        (4, 50),    # tail
    ],
)
def testgetwalksininsertionorder(numberlist, index, expected):
    """Validate every index reports the value that was added at that position (fixture + parameterize)."""
    assert numberlist.get(index).data == expected

def testlastnodedoesnotlinkonward(numberlist):
    """Validate the node at the end of the list terminates the chain (fixture)."""
    assert numberlist.get(4).next is None

# CSC 5120 Module 7 Project
# Paul England
# Instructions
# The goal of the seventh project is to compare the "step" and timing results for storing and retrieving data from two
# different data structures: the singly linked list we developed in class and a built in Python Array. We will also
# analyze the Big O upper bound (in terms of the n items stored) for our insert and retrieval methods.
#
# This file contains the tests of the LinkedList class.  These are the tests:
# - A new linked list is empty by using isEmpty.
# - A new linked list is empty by using len.
# - A new linked list is empty by using size.
# - Adding to an empty list makes it no longer empty.
# - The length is 1 when the initial node is appended.
# - The size attribute is 1 when the initial node is appended.
# - The length of the list tracks the number of nodes appended.
# - Adding the same value twice creates two separate nodes.
# - An empty list prints a message rather than a blank string.
# - A one node list prints without a trailing arrow.
# - A populated list prints its values separated by arrows.
# - Find returns None on an empty list.
# - Find returns the first occurrence when data is duplicated.
# - Removing the only node leaves an empty list.
# - Get returns a Node rather than the raw data.
# - Get walks the list in the order the values were appended, which proves append appends to the end.
# - The last node in the list terminates the chain.
# - Remove handles the first, middle, and last node.
# - Find returns the node holding the search data at the head, middle, and tail.
# - Find returns a Node rather than the raw data.
# - Find returns None when the data is not in the list.
# - Insert handles the head, negative, middle, and end positions.

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
def testappendisnotempty(emptylist):
    """Validate isEmpty is false when a node is appended (fixture)."""
    emptylist.append(5)
    assert emptylist.isEmpty() is False

def testappendlengthequalsone(emptylist):
    """Validate that length is 1 when the initial node is appended (fixture)."""
    emptylist.append(5)
    assert len(emptylist) == 1

def testappendsizenotzero(emptylist):
    """Validate the size attribute is 1 when the initial node is appended (fixture)."""
    emptylist.append(5)
    assert emptylist.size == 1

@pytest.mark.parametrize("count", [1, 2, 3, 4, 5, 10, 100])
def testappendingmanynodes(emptylist, count):
    """Validate the append method appends many nodes (fixture + parameterize)."""
    for number in range(count):
        emptylist.append(number)
    assert len(emptylist) == count

def testappendingsamedata(emptylist):
    """Validate you get two nodes if the data is duplicated (fixture)."""
    emptylist.append(5)
    emptylist.append(5)
    assert len(emptylist) == 2

def testemptyliststr(emptylist):
    """Validate an empty list prints a message instead of a blank string (fixture)."""
    assert str(emptylist) == "The linked list is empty."

def testsinglenodestr(emptylist):
    """Validate a one node list prints without a trailing -> (fixture)."""
    emptylist.append(10)
    assert str(emptylist) == "10"

def testmultiplenodestr(emptylist):
    """Validate a multi node list prints each value separated by ->'s (fixture)."""
    for number in (10, 20, 30):
        emptylist.append(number)
    assert str(emptylist) == "10 -> 20 -> 30"

def testfindonemptylist(emptylist):
    """Validate find returns None on an empty list (fixture)."""
    assert emptylist.find(10) is None

def testfindduplicatereturnsfirst(emptylist):
    """Validate find returns the first occurrence when data is duplicated (fixture)."""
    emptylist.append(5)
    emptylist.append(7)
    emptylist.append(5)
    assert emptylist.find(5) is emptylist.get(0)

def testremovelastnode(emptylist):
    """Validate removing the only node leaves an empty list (fixture)."""
    emptylist.append(5)
    emptylist.remove(0)
    assert str(emptylist) == "The linked list is empty."
    assert len(emptylist) == 0

# The next tests need a list with nodes created.
@pytest.fixture
def numberlist():
    """Provide a fresh LinkedList holding 10, 20, 30, 40, 50 in that order for each test (fixture)."""
    notemptylist = LinkedList()
    for number in (10, 20, 30, 40, 50):
        notemptylist.append(number)
    return notemptylist

def testgetanode(numberlist):
    """Validate getting the first node and not the node's value (fixture)."""
    assert isinstance(numberlist.get(0), Node)

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
def testgetvalues(numberlist, index, expected):
    """Validate you get the correct value for each assigned node (fixture + parameterize)."""
    assert numberlist.get(index).data == expected

def testlastnodeislastnode(numberlist):
    """Validate the last node is the last node (fixture)."""
    assert numberlist.get(4).next is None

@pytest.mark.parametrize(
    "index, expected",
    [
        (0, "20 -> 30 -> 40 -> 50"),    # first
        (2, "10 -> 20 -> 40 -> 50"),    # middle
        (4, "10 -> 20 -> 30 -> 40"),    # last
    ],
)
def testremovebyposition(numberlist, index, expected):
    """Validate remove handles the first, middle, and last node (fixture + parameterize)."""
    numberlist.remove(index)
    assert str(numberlist) == expected
    assert len(numberlist) == 4

@pytest.mark.parametrize(
    "searchdata",
    [
        10,     # head
        30,     # middle
        50,     # tail
    ],
)
def testfindreturnsmatchingnode(numberlist, searchdata):
    """Validate find returns the node holding the search data (fixture + parameterize)."""
    assert numberlist.find(searchdata).data == searchdata

def testfindreturnsanode(numberlist):
    """Validate find returns a Node rather than the raw data (fixture)."""
    assert isinstance(numberlist.find(30), Node)

def testfindmissingdata(numberlist):
    """Validate find returns None when the data is not in the list (fixture)."""
    assert numberlist.find(999) is None

@pytest.mark.parametrize(
    "index, newdata, expected",
    [
        (0, 5, "5 -> 10 -> 20 -> 30 -> 40 -> 50"),      # head
        (-3, 5, "5 -> 10 -> 20 -> 30 -> 40 -> 50"),     # negative also prepends
        (2, 25, "10 -> 20 -> 25 -> 30 -> 40 -> 50"),    # middle
        (4, 45, "10 -> 20 -> 30 -> 40 -> 45 -> 50"),    # just before the tail
        (5, 60, "10 -> 20 -> 30 -> 40 -> 50 -> 60"),    # at size, delegates to append
        (99, 60, "10 -> 20 -> 30 -> 40 -> 50 -> 60"),   # beyond size, delegates to append
    ],
)
def testinsertbyposition(numberlist, index, newdata, expected):
    """Validate insert handles head, negative, middle, and end positions (fixture + parameterize)."""
    numberlist.insert(index, newdata)
    assert str(numberlist) == expected
    assert len(numberlist) == 6

# CSC 5120 Module 8 Project
# Paul England
# Instructions
#
# The goal of the eighth project is to collect and analyze the "step" and timing results for storing and retrieving data
# from a binary search tree. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert
# and retrieval methods.
#
# This file contains the tests of the BST class.  These are the tests:
# - A new binary search tree is empty by using isEmpty.
# - A new binary search tree is empty by using len.
# - A new binary search tree is empty by using size.
# - Adding to an empty binary search tree makes it no longer empty.
# - The length is 1 when the initial node is inserted.
# - The size attribute is 1 when the initial node is inserted.
# - The length of the binary search tree tracks the number of nodes inserted.
# - Adding the same key twice only allows one node.
# - An empty binary search tree prints a message rather than a blank string.
# - A one node binary search tree prints only the root row.
# - A binary search tree with increasing keys prints None for the root's missing left child.
# - A binary search tree with decreasing keys prints None for the root's missing right child.
# - An eight node binary search tree prints all four rows with None placeholders.
# - Find returns None on an empty binary search tree.
# - Find returns the original node after a duplicate key is rejected.
# - The iterative in order traversal returns the values in ascending key order.
# - The traversal helper returns an empty string for None.
# - The traversal helper returns one value with a trailing separator.
# - The traversal helper returns ascending key order for a tree built by insert.
# - The recursive in order traversal prints a message on an empty binary search tree.
# - The recursive in order traversal returns one value without a separator.
# - The recursive in order traversal returns the values in ascending key order.
# - The iterative and recursive in order traversals return the same string.
# - Recursively adding to an empty binary search tree makes it no longer empty.
# - The length is 1 when the initial node is inserted recursively.
# - The size attribute is 1 when the initial node is inserted recursively.
# - The length of the binary search tree tracks the number of nodes inserted recursively.
# - Recursively adding the same key twice only allows one node.
# - A tree built by the recursive insert traverses in ascending key order.
# - The recursive find returns None on an empty binary search tree.
# - The recursive find returns the original node after a duplicate key is rejected.
# - The recursive find returns nodes on both sides of the root.
# - The recursive find returns None for a missing key in a populated binary search tree.

# Load pytest and BST.
import pytest
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

def testemptytreestr(emptytree):
    """Validate an empty binary search tree prints a message instead of a blank string (fixture)."""
    assert str(emptytree) == "The binary search tree is empty."

def testsinglenodestr(emptytree):
    """Validate a one node binary search tree prints without a trailing -> (fixture)."""
    emptytree.insert(1, 10)
    print("f\n {str(emptytree)}")
    assert str(emptytree) == "\t  10\n"

def testmultiplenodestrright(emptytree):
    """Validate a multi node binary search tree prints each value separated by ->'s (fixture)."""
    for number in (10, 20, 30):
        emptytree.insert(number, number)
    print(f"\n{str(emptytree)}")
    assert str(emptytree) == "\t  10\n\t/\t\\\n  None\t  20\n"

def testmultiplenodestrleft(emptytree):
    """Validate a multi node binary search tree prints each value separated by ->'s (fixture)."""
    for number in (100, 40, 30):
        emptytree.insert(number, number)
    print(f"\n{str(emptytree)}")
    assert str(emptytree) == "\t  100\n\t/\t\\\n  40\t  None\n"

def testmultiplenodestrpartright(emptytree):
    """Validate a multi node binary search tree prints each value separated by ->'s (fixture)."""
    for number in (100, 20, 200, 30, 300, 40, 400, 50):
        emptytree.insert(number, number)
    print(f"\n{str(emptytree)}")
    assert str(emptytree) == ("\t  100\n"
                             "\t/\t\\\n"
                             "  20\t  200\n"
                             "/\t\\\t/\t\\\n"
                             "None\t30\tNone\t300\n"
                             "/  \\  /  \\  /  \\  /  \\\n"
                             "None  None  None 40  None  None  None 400")

def testfindonemptytree(emptytree):
    """Validate find returns None on an empty binary search tree (fixture)."""
    assert emptytree.findbykey(10) is None

def testfindduplicatereturnsfirst(emptytree):
    """Validate find returns the first occurrence when data is duplicated (fixture)."""
    emptytree.insert(5,5)
    emptytree.insert(7,7)
    emptytree.insert(5,7)
    newnode = emptytree.findbykey(5)
    print(str(newnode))
    assert str(newnode) == "5"

def testdisplayinorder(emptytree):
    """Validate a multi node binary search tree prints each value separated by ->'s (fixture)."""
    for number in (100, 20, 200, 30, 300, 40, 400, 50):
        emptytree.insert(number, number)
    print(f"\n{emptytree.displayinorder()}")
    assert emptytree.displayinorder() == "20, 30, 40, 50, 100, 200, 300, 400"

def testemptytreedisplayinorderrecursive(emptytree):
    """Validate the traversal helper returns an empty string for None (fixture)."""
    print(f"\n{emptytree.displayinorderrecursive(None)}")
    assert emptytree.displayinorderrecursive(None) == ""

def testsinglenodedisplayinorderrecursive(emptytree):
    """Validate the traversal helper returns one value with a trailing separator (fixture)."""
    emptytree.insert(5, 30)
    newnode = emptytree.findbykey(5)
    print(f"\n{emptytree.displayinorderrecursive(newnode)}")
    assert emptytree.displayinorderrecursive(newnode) == "30, "

def testmultinodedisplayinorderrecursive(emptytree):
    """Validate the traversal helper walks a hand built tree in ascending key order (fixture)."""
    for number in (10, 20, 30):
        emptytree.insert(number, number)
    newnode = emptytree.findbykey(10)
    print(f"\n{emptytree.displayinorderrecursive(newnode)}")
    assert emptytree.displayinorderrecursive(newnode) == "10, 20, 30, "

def testemptytreedisplayinorderusingrecursion(emptytree):
    """Validate an empty binary search tree prints a message instead of a blank string (fixture)."""
    print(f"\n{emptytree.displayinorderusingrecursion()}")
    assert emptytree.displayinorderusingrecursion() == "The binary search tree is empty."

def testsinglenodedisplayinorderusingrecursion(emptytree):
    """Validate the traversal helper returns one value with a trailing separator (fixture)."""
    emptytree.insert(5, 30)
    print(f"\n{emptytree.displayinorderusingrecursion()}")
    assert emptytree.displayinorderusingrecursion() == "30"

def testdisplayinorderusingrecursion(emptytree):
    """Validate a multi node binary search tree prints each value separated by ->'s (fixture)."""
    for number in (100, 20, 200, 30, 300, 40, 400, 50):
        emptytree.insert(number, number)
    print(f"\n{emptytree.displayinorderusingrecursion()}")
    assert emptytree.displayinorderusingrecursion() == "20, 30, 40, 50, 100, 200, 300, 400"

def testinordermethodsagree(emptytree):
    """Validate the iterative and recursive in order traversals return the same string (fixture)."""
    for number in (100, 20, 200, 30, 300, 40, 400, 50):
        emptytree.insert(number, number)
    assert emptytree.displayinorder() == emptytree.displayinorderusingrecursion()

def testcallinsertrecursiveisnotempty(emptytree):
    """Validate isEmpty is false when a node is inserted (fixture)."""
    emptytree.callinsertrecursive(1,5)
    assert emptytree.isEmpty() is False

def testcallinsertrecursivelengthequalsone(emptytree):
    """Validate that length is 1 when the initial node is inserted (fixture)."""
    emptytree.callinsertrecursive(1,5)
    assert len(emptytree) == 1

def testcallinsertrecursivesizenotzero(emptytree):
    """Validate the size attribute is 1 when the initial node is inserted (fixture)."""
    emptytree.callinsertrecursive(1,5)
    assert emptytree.size == 1

@pytest.mark.parametrize("count", [1, 2, 3, 4, 5, 10, 100])
def testcallinsertrecursivemanynodes(emptytree, count):
    """Validate the insert method inserts many nodes (fixture + parameterize)."""
    loopkey = 1
    for number in range(count):
        emptytree.callinsertrecursive(loopkey,number)
        loopkey += 1
    assert len(emptytree) == count

def testcallinsertrecursivesamedata(emptytree):
    """Validate you get one node if the data is duplicated (fixture)."""
    emptytree.callinsertrecursive(1,5)
    emptytree.callinsertrecursive(1,5)
    assert len(emptytree) == 1

def testmultinoderecursiveinsertanddisplay(emptytree):
    """Validate the traversal helper walks a hand built tree in ascending key order (fixture)."""
    for number in (10, 20, 30):
        emptytree.callinsertrecursive(number, number)
    newnode = emptytree.findbykey(10)
    print(f"\n{emptytree.displayinorderrecursive(newnode)}")
    assert emptytree.displayinorderrecursive(newnode) == "10, 20, 30, "

def testfindonemptytreerecursive(emptytree):
    """Validate find returns None on an empty binary search tree (fixture)."""
    assert emptytree.callfindkeyrecursive(10) is None

def testfindduplicatereturnsfirstrecursive(emptytree):
    """Validate find returns the first occurrence when data is duplicated (fixture)."""
    emptytree.callinsertrecursive(5,5)
    emptytree.callinsertrecursive(7,7)
    emptytree.callinsertrecursive(5,7)
    newnode = emptytree.callfindkeyrecursive(5)
    print(str(newnode))
    assert str(newnode) == "5"

def testfinddeepernodesrecursive(emptytree):
    """Validate the recursive find returns nodes on both sides of the root (fixture)."""
    for number in (20, 10, 30):
        emptytree.callinsertrecursive(number, number)
    assert str(emptytree.callfindkeyrecursive(10)) == "10"
    assert str(emptytree.callfindkeyrecursive(30)) == "30"

def testfindmissingkeyrecursive(emptytree):
    """Validate the recursive find returns None for a missing key in a populated binary search tree (fixture)."""
    for number in (20, 10, 30):
        emptytree.callinsertrecursive(number, number)
    assert emptytree.callfindkeyrecursive(99) is None
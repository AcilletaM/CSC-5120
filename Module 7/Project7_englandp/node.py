# CSC 5120 Module 7 Project
# Paul England
# Instructions
#
# The goal of the seventh project is to compare the "step" and timing results for storing and retrieving data from two different data structures: the singly linked list 
# we developed in class and a built in Python Array. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert and retrieval methods. 
#
# This creates the Node class for the linked list.  A linked list would have 1 or more of these nodes.
class Node(object):
    """Single node class for a linked list."""

    def __init__(self, data):
        """Constructor."""
        self.data = data
        self.next = None

    def __str__(self):
        """Returns the value of the node."""
        return str(self.data)

# CSC 5120 Module 7 Project
# Paul England
# Instructions
#
# The goal of the seventh project is to compare the "step" and timing results for storing and retrieving data from two different data structures: the singly linked list 
# we developed in class and a built in Python Array. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert and retrieval methods. 
#
# This creates the LinkedList class for the linked list.  This creates and manipulates a linked list, which is made up of nodes from the Node class.
#
# Bring in the class definitons
from node import Node

class LinkedList(object):  # A linked list of data elements
    """Base class for a linked list, which is a collection of Nodes."""

    def __init__(self):
        """Constructor."""
        self.__head = None
        self.size = 0

    def isEmpty(self):  # Test for empty list
        """Returns the number of nodes in a linked list."""
        return (self.size == 0)
 
    def __len__(self):
        """Returns the number of nodes in a linked list."""
        return self.size

    def add(self, newnodedata):
        """Adds a new node to the end of the linked list."""
        other = Node(newnodedata)
        cur = self.__head
        steps = 1

        # Check if empty otherwise step through the list to find the end.
        if (self.size == 0):
            self.__head = other
        else:
            while (cur.next is not None):
                    cur = cur.next
                    steps += 1
            cur.next = other
        self.size += 1


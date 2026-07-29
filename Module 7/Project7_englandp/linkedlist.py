# CSC 5120 Module 7 Project
# Paul England
# Instructions
#
# The goal of the seventh project is to compare the "step" and timing results for storing and retrieving data from two different data structures: the singly linked list 
# we developed in class and a built in Python Array. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert and retrieval methods. 
#
# This creates the LinkedList class for the linked list.  This creates and manipulates a linked list, which is made up of nodes from the Node class.
#
# Bring in the class definitions
from node import Node

class LinkedList(object):  # A linked list of data elements
    """Base class for a linked list, which is a collection of Nodes."""

    def __init__(self):
        """Constructor."""
        self.__head = None
        self.size = 0
        self.steps = 0

    def isEmpty(self):
        """Checks if a linked list is empty."""
        return (self.size == 0)
 
    def __len__(self):
        """Returns the number of nodes in a linked list."""
        return self.size

    def append(self, newnodedata):
        """Adds a new node to the end of the linked list."""
        newnode = Node(newnodedata)
        steps = 1

        # Check if empty otherwise step through the list to find the end.
        if (self.isEmpty()):
            self.__head = newnode
            self.size += 1
        else:
            current = self.__head
            while (current.next is not None):
                current = current.next
                steps += 1
            current.next = newnode
            self.size += 1

        self.steps = steps
        return None

    def get(self, index: int):
        """Retrieves a specific node from the linked list."""

        # If empty, return None otherwise find the node and return it.
        if (self.isEmpty()):
            return None
        # If index is not valid, return None.
        elif (index < 0 or index >= self.size):
            return None
        # Find the node and return the value.
        else:
            current = self.__head
            steps = 1

            for i in range(index):
                current = current.next
                steps += 1

            self.steps = steps
            return current

    def remove(self, index:int):
        """Removes a specific node from the linked list."""

        # Check if the index is valid.
        if (index < 0 or index >= self.size):
            return None
        # Check if the index is the first node.
        elif (index == 0):
            # Could be a single node linked list, meaning it is the last node.
            if (self.size == 1):
                self.__head = None
            # There are multiple nodes in this list.  Remove the first node.
            else:
                self.__head = self.__head.next
        # It is a valid node that is not the first.  Is it the last?
        elif (index == self.size - 1):
            previousnode = self.get(index - 1)
            previousnode.next = None
        # This is a node somewhere in the middle.
        else:
            previousnode = self.get(index - 1)
            nextnode = self.get(index + 1)

            previousnode.next = nextnode

        self.size -= 1
        return None

    def find(self, searchdata) -> Node:
        """Finds a node from the linked list by the first occurrence of its data."""
        current = self.__head

        # Loop through the list returning the first node that matches the search data
        for loop in range(self.size):
            if (current.data != searchdata):
                current = current.next
            else:
                return current
        return None

    def insert(self, insertindex: int, newdata):
        """Inserts a new node into the linked list at the specified index."""
        newnode = Node(newdata)

        # The linked list is empty or the specified index is greater than the last index value, append to the end.
        if (self.isEmpty() or insertindex >= self.size):
            self.append(newdata)
        # Insert in beginning of the list if the index specified is 0 or less.
        elif (insertindex <= 0):
            newnode.next = self.__head
            self.__head = newnode
            self.size += 1
        # In between the first and last node.
        else:
            current = self.__head

            # Find the specified node to insert after.
            for i in range(insertindex - 1):
                current = current.next

            newnode.next = current.next
            current.next = newnode
            self.size += 1

        return None

    def __str__(self):
        """Return a message showing the node values or a default message if empty."""
        current = self.__head
        message = ""

        # Check if the list is empty.  Return a default message if it is otherwise return the contents with ->'s between the nodes.
        if (self.size == 0):
            return "The linked list is empty."
        else:
            while (current.next is not None):
                message += f"{str(current.data)} -> " # add the current node's data on to the message
                current = current.next
            message += str(current.data)  # add the last node's data to the message

        return message

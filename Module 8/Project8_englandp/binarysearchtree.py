# CSC 5120 Module 8 Project
# Paul England
# Instructions
#
# The goal of the eighth project is to collect and analyze the "step" and timing results for storing and retrieving data
# from a binary search tree. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert
# and retrieval methods.
#
# Load the Node class
from node import Node

# This creates the binary search tree class.
class BST(object):
    """Binary search tree of data elements."""

    def __init__(self):
        """Constructor for Binary Search Tree."""
        self.__root = None
        self.size = 0

    def isEmpty(self):
        """Checks if a linked list is empty."""
        return (self.size == 0)

    def __len__(self):
        """Returns the number of nodes in a linked list."""
        return self.size

    def insert(self, newkey, newnodedata):
        """Inserts a new node into the linked list."""

        # Create the new node, increment the size, log the first step, and resync to the root of the tree.
        newnode = Node(newkey,newnodedata)
        current = self.__root
        steps = 1

        if current is None:
            self.__root = newnode
            self.size += 1
            # print("\nRoot node.")
        else:
            looping = True

            while looping:
                steps += 1
                if newkey == current.key:
                    # print("\nNo duplicate keys - node not added.")
                    looping = False
                elif newkey < current.key:
                    if current.left is None:
                        current.left = newnode
                        self.size += 1
                        looping = False
                        # print("\nLeft new node.")
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = newnode
                        self.size += 1
                        looping = False
                        # print("\nRight new node.")
                    else:
                        current = current.right

        return None

    def __str__(self):
        """Return a message showing the node values or a default message if empty.  This will never print the whole tree."""
        current = self.__root
        message = ""

        # Check if the tree is empty.  Return a default message if it is otherwise return the contents with ->'s between the nodes.
        if self.size == 0:
            return "The binary search tree is empty."
        else:
            while current.left is not None or current.right is not None:
                message += f"{str(current.data)} -> " # add the current node's data on to the message
                if current.left is not None:
                    current = current.left
                else:
                    current = current.right
            message += str(current.data)  # add the last node's data to the message

        return message
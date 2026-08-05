# CSC 5120 Module 8 Project
# Paul England
# Instructions
#
# The goal of the eighth project is to collect and analyze the "step" and timing results for storing and retrieving data
# from a binary search tree. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert
# and retrieval methods.
#
# This creates the Node class for the binary search tree.  A binary search tree would have 1 or more of these nodes.
class Node(object):
    """Single node class for a binary search tree."""

    def __init__(self, key, data):
        """Constructor."""

        # A node will contain the data, left and right references, and a key for uniqueness.
        self.data = data
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        """Returns the value of the node."""
        return str(self.data)

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
from linkedlist import LinkedList

# This creates the binary search tree class.
class BST(object):
    """Binary search tree of data elements."""

    def __init__(self):
        """Constructor for Binary Search Tree."""
        self.__root = None
        self.size = 0
        self.steps = 0

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
        self.steps = 1

        if current is None:
            self.__root = newnode
            self.size += 1
            # print("\nRoot node.")
        else:
            looping = True

            while looping:
                self.steps += 1
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

    def findbykey(self, searchkey):
        """Find a node using the key."""

        # Start with no node found and the top of the tree.
        foundnode = None
        current = self.__root
        self.steps = 1

        if current is not None:
            # The tree has a least 1 node.
            looping = True

            # Loop basics:
            # - Use key value to choose path.
            # - If left/right of the current node is None, we know a node with the key doesn't exist.
            # - If left/right of the current node is not None, move to that node.
            # - If the current key matches the search key - stop looking.
            # - Otherwise, loop through again.
            while (looping):
                self.steps += 1
                if searchkey < current.key:
                    if (current.left is None):
                        looping = False
                    else:
                        current = current.left
                elif searchkey > current.key:
                    if (current.right is None):
                        looping = False
                    else:
                        current = current.right
                else:
                    foundnode = current
                    looping = False

        return foundnode

    def __str__(self):
        """Return a message showing the node values or a default message if empty.  This will never print the whole tree."""
        message = "The binary search tree is empty."

        # Check if the tree is empty.  Return a default message if it is otherwise return the contents with ->'s between the nodes.
        if self.size > 0:
            message = f"\t  {self.__root}\n"

            if (self.size > 1):
                message += f"\t/\t\\\n"
                message += f"  {self.__root.left}\t  {self.__root.right}\n"

            if (self.size > 3):
                leftnode = self.__root.left
                rightnode = self.__root.right
                message += "/\t\\\t/\t\\\n"
                if leftnode is not None:
                    message += f"{leftnode.left}\t{leftnode.right}"
                else:
                    message += "None\tNone"
                if rightnode is not None:
                    message += f"\t{rightnode.left}\t{rightnode.right}"
                else:
                    message += "\tNone\tNone"

            if (self.size > 7):
                leftleftnode = self.__root.left.left
                leftrightnode = self.__root.left.right
                rightleftnode = self.__root.right.left
                rightrightnode = self.__root.right.right
                message += "\n/  \\  /  \\  /  \\  /  \\\n"
                if leftleftnode is not None:
                    message += f"{leftleftnode.left} {leftleftnode.right}"
                else:
                    message += "None  None "
                if leftrightnode is not None:
                    message += f" {leftrightnode.left} {leftrightnode.right}"
                else:
                    message += "None  None "
                if rightleftnode is not None:
                    message += f" {rightleftnode.left} {rightleftnode.right}"
                else:
                    message += "  None  None "
                if rightrightnode is not None:
                    message += f" {rightrightnode.left} {rightrightnode.right}"
                else:
                    message += "  None  None "

        return message

    def displayinorder(self):
        """Display the in order traversal of the binary search tree (not recursive)."""
        message = "The binary search tree is empty."
        current = self.__root

        if current is not None:
            message = ""

        # Using a linked list like a stack.
        # Basically keep added nodes at the root pushes other nodes down the list.
        # Removing from the root shrinks the "stack".
        # Other way to think about it is a typical list has nodes added the end.
        # A stack treats the root node as the end to insert in front of.
        stackofnodes = LinkedList()

        looping = True
        while (looping):

            if current is not None:
                # Add the node to the stack
                stackofnodes.insert(0, current)

                # Go left first.
                current = current.left
            elif (stackofnodes.size > 0):
                # Get the data from the last node added and remove.
                current = stackofnodes.get(0).data
                stackofnodes.remove(0)
                message += f"{current}, "

                # We went left, now check right.
                current = current.right
            else:
                # We got here by having an empty binary search tree,
                # no more nodes to traverse,
                # or we've built the message from all the values.
                looping = False

        if self.size > 0:
            # Remove the last comma and space.
            message = message[:-2]

        return message

    def displayinorderrecursive(self, current):
        """Traverses the binary search tree recursively to find all the values."""

        # Make sure there are nodes in the binary search tree.
        if current is None:
            return ""

        # Call itself to go to the left.
        message = self.displayinorderrecursive(current.left)
        message += f"{current}, "
        # Call itself to go to the right.
        message += self.displayinorderrecursive(current.right)

        return message

    def displayinorderusingrecursion(self):
        """Display the in order traversal of the binary search tree (recursive)."""

        # Initialize message and start traversing the binary search tree.
        message = "The binary search tree is empty."
        current = self.__root

        if self.size > 0:
            message = self.displayinorderrecursive(self.__root)

            # Remove the last comma and space.
            message = message[:-2]

        return message

    def insertrecursive(self, current, newkey, newnodedata):
        """Inserts a new node into the binary search tree recursively."""
        self.steps += 1

        # Nothing to traverse, add the node here.
        if current is None:
            self.size += 1
            return Node(newkey, newnodedata)

        if newkey < current.key:
            # Call itself to go to the left.
            current.left = self.insertrecursive(current.left, newkey, newnodedata)
        elif newkey > current.key:
            # Call itself to go to the right.
            current.right = self.insertrecursive(current.right, newkey, newnodedata)

        # No duplicates allowed so no else clause.

        return current

    def callinsertrecursive(self, newkey, newnodedata):
        """Call the function that inserts a new node into the binary search tree recursively."""
        self.steps = 0
        self.__root = self.insertrecursive(self.__root, newkey, newnodedata)

        return None

    def findkeyrecursive(self, current, searchkey):
        """Finds a node by key in a binary search tree recursively."""
        self.steps += 1

        # Nothing to traverse, no node to find.
        if current is None:
            return None

        if searchkey < current.key:
            # Call itself to go to the left.
            return self.findkeyrecursive(current.left, searchkey)
        elif searchkey > current.key:
            # Call itself to go to the right.
            return self.findkeyrecursive(current.right, searchkey)

        # Key matches, return current node.
        return current

    def callfindkeyrecursive(self, searchkey):
        """Call the function that finds a node using the key in a binary search tree recursively."""
        self.steps = 0

        return self.findkeyrecursive(self.__root, searchkey)
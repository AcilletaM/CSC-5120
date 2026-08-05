from linked_list import LinkedList
# we inherit from object by convention here (and possibly
# for compatibility with older versions of python).
# It used to be needed in python 2,
# but in python 3 it is no longer needed
class Node(object):  # One part of the data Tree
    def __init__(self, key, data):  # Constructor
        self.data = data  # The data object for this Node
        self.left = None  # the left child
        self.right = None  # the right child
        #using a key, like Student with an ID
        self.key = key  # could be used to prevent duplicates,
                        # but be careful how you use if you WANT duplicates

    def __str__(self):
        return str(self.data)

class BST(object):  # A binary search tree of data elements
    # class variable to keep track of how many Nodes in list

    def __init__(self):  # Constructor
        self.__root = None  # Reference to start of BST
        self.size = 0


    # add (aka insert)
    # this function does NOT keep the tree balanced
    # Rules for data struct functions:
    # 1. before function is called, we have a valid data structure (BST)
    # 2. update all attributes (root, size, left and right of Nodes)
    # 3. on the way out, the function must leave the data structure valid
    def add(self, key, dataToAdd): # we decided that adding is log(N) (LOG BASE 2)
        nodeToAdd = Node(key, dataToAdd) # QoL improvement, hide Nodes from user
        cur = self.__root  # the current Node we are looking at

        self.size += 1
        steps = 1
        if cur is None:  # For empty trees, insert new node at root
            self.__root = nodeToAdd  # root of tree
        else:
            # we at least have a root already
            lookingForSpot = True

            while (lookingForSpot):
                steps +=1
                if key < cur.key:  # updated for key. If new data is less cur's data, go left
                    if (cur.left is None):  # if there is a open spot
                        cur.left = nodeToAdd
                        lookingForSpot = False
                    else:
                        cur = cur.left  # equivalent of cur = cur.next in LL. Meaning keeping going
                else:  # Otherwise >= look right
                    if (cur.right is None):
                        cur.right = nodeToAdd
                        lookingForSpot = False
                    else:
                        cur = cur.right  # equivalent of cur = cur.next in LL. Meaning keeping going
            # print (f"steps for adding {dataToAdd}: {steps}")


    # return the Object (data) if found, or None
    def find(self, keyToFind): # takes key, NOT a Node. Also O(log(N))
        nodeWeFound = None

        cur = self.__root  # the current Node we are looking at

        steps = 1
        if cur is not None:
            # we at least have a root already
            lookingForSpot = True

            while (lookingForSpot):
                steps += 1
                if keyToFind < cur.key:  # updated for key. If new data is less cur's data, go left
                    if (cur.left is None):  # if there isn't a left, we aren't gonna find it
                        lookingForSpot = False
                    else:
                        cur = cur.left  # equivalent of cur = cur.next in LL. Meaning keeping going
                elif keyToFind > cur.key:  # Otherwise > look right
                    if (cur.right is None): # if there isn't a right, we aren't gonna find it
                        lookingForSpot = False
                    else:
                        cur = cur.right
                else: # we found it!
                    nodeWeFound = cur
                    lookingForSpot = False
        return nodeWeFound

    # working on inOrder to make this better
    def __str__(self):
        return self.inorderTraversal()
        """message = f"\t  {self.__root}\n"

        if (self.size>1):
            message += f"\t/\t\\\n"
            message += f"  {self.__root.left}\t\t  {self.__root.right}\n"

        if (self.size>3):
            message += f"/\t\\\t/\t\\\n"
            message += f"{self.__root.left.left}\t{self.__root.left.right}"
            message += f"\t{self.__root.right.left}\t{self.__root.right.right}"

        return message
        """

    # inorder traversal, non-recursive (so that we can print out in order)
    # instead of a "text based graphics" for printing out a tree, we are better off with
    # an in-order traversal, printing out each item in order of smallest to largest
    def inOrderNonRecursive(self):
        message = ""

        cur = self.__root  # the current Node we are looking at


        # we use a linked list (as a Stack) where we add and remove from the
        # beginning so save Nodes in the order we want
        saved = LinkedList()

        keepGoing = True
        while (keepGoing):

            # Reach the left most Node of the current Node
            if cur is not None:

                # Place reference cur Node at the start of the list
                # before traversing the node's left subtree
                saved.addAt(0, cur) # we are using our linked list like a stack here
                # stack: push is addAt(0...), pop is get(0) then remove(0)
                cur = cur.left

            # Back out of an empty subtree and add Node's at the front
            # of the list's  data to message
            # if the list is empty, we are done
            elif (saved.size > 0):
                cur = saved.get(0).data #TODO why .data here?
                saved.remove(0) # clear that entry out since we are now dealing with it
                message += f"{cur}, "

                # We have visited the cur node and its left subtree
                # Now go right
                cur = cur.right
            else:
                keepGoing = False # we have visited all nodes


        return message

    # TODO try recursive add on your own

    # TODO recursive find on your own

    # TODO recursive inorder
    def inorderTraversal(self):
        message = ""
        message = self.inorderTraversalHelper(self.__root)
        return message


    def inorderTraversalHelper(self, cur):

        if cur is None:
            return ""

        message = self.inorderTraversalHelper(cur.left) # this is tricky (being = )
        message += f"{cur}, "
        message += self.inorderTraversalHelper(cur.right)
        return message

    # how would delete work?

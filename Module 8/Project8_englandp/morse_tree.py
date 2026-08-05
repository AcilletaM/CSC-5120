
# Our Morse Tree still uses a Node with data - but we don't really need an extra key attribute.
# Our data will a character (String)
class Node(object):  # One part of the Morse Tree. character is none if it isn't a decode Node, or hasn't been populated yet
    def __init__(self, character):  # Constructor
        self.character = character  # The data object for this Node
        self.left = None  # the left child
        self.right = None  # the right child

    def __str__(self):
        return str(self.character)

class MorseTree(object):  # A binary search tree for morse code

    def __init__(self):  # Constructor
        self.__root = Node(None)  # Our root node in a Morse tree also contains no data, so None



    # add (aka insert)
    # we are not concerned with a balanced tree, since the decoding is built into the tree structure now
    # depending on what data you are decoding for your project (if it is sorted alphabetically for example), you
    # will want to add things in a way that results in a somewhat balanced tree. randomization like in homework 8 is
    # an option
    def add(self, character, code): # is adding still log(N) (LOG BASE 2)?

        # the current Node we are looking at,
        # but we label it as the parent because of how we use it below
        cur_parent = self.__root


        # we must move left or right based on the dots and dashes in the code until we have nothing remaining
        # we then put the new character there (maybe new node, maybe one was there)
        # we have to account for have empty/missing children along the way, and create them if needed
        # we have to account for having already added a character, in which case we do nothing, or at least do no harm

        # for code, . is left, - is right
        # the root is never None, sine it is initialized in the __init__
        while (len(code)>0): # while we still have some code left to parse
            nextPart = code[0:1:1] # start:stop:step, same as code{:1:] since default start is 0, default step is 1
            code = code[1:] # substring starting at spot 1, so spot 0 is removed
            # "" is empty string, len("") is 0

            #TODO can this be simplified? Is it better as recursion?
            if (len(code)==0): # we are at the end of the code, "base case"
                if (nextPart=="."):# got left
                    if (cur_parent.left is None):
                        cur_parent.left = Node(character)
                    else:
                        cur_parent.left.character = character # and Empty node is already available where we need it

                elif (nextPart=="-"): # go right
                    if (cur_parent.right is None):
                        cur_parent.right = Node(character)
                    else:
                        cur_parent.right.character = character
                else:
                    print(f"Warning - skipping: ->{nextPart}<-" )
                    return False # we are in trouble
            else: # we are not at the end of the code, still trying to get to where we are going
                if (nextPart == "."):  # got left
                    if (cur_parent.left is None):
                        cur_parent.left = Node(None)
                    cur_parent = cur_parent.left
                elif (nextPart == "-"):  # go right
                    if (cur_parent.right is None):
                        cur_parent.right = Node(None)
                    cur_parent = cur_parent.right
                else:
                    print(f"Warning - skipping: ->{nextPart}<-")
                    return False  # we are in trouble

        return True # if we get back out here, we were successful




    def decode(self, code):
        cur_parent = self.__root

        # we must move left or right based on the dots and dashes in the code until we have nothing remaining

        # for code, . is left, - is right
        # the root is never None, since it is initialized in the __init__
        while (len(code) > 0):  # while we still have some code left to parse
            nextPart = code[0:1:1]  # start:stop:step, same as code{:1:] since default start is 0, default step is 1
            code = code[1:]  # substring starting at spot 1, so spot 0 is removed
            # "" is empty string, len("") is 0

            if (len(code) == 0):  # we are at the end of the code, "base case" -> should have found it
                if (nextPart == "."):  # got left
                    if (cur_parent.left is None):
                        # not in coded tree
                        return "[ERROR!!!!!!!]"
                    else:
                        return cur_parent.left.character

                elif (nextPart == "-"):  # go right
                    if (cur_parent.right is None):
                        # not in coded tree
                        return "[ERROR!!!!!!!]"
                    else:
                        return cur_parent.right.character
                else:
                    return "[ERROR!!!!!!!]"  # we are in trouble
            else:  # we are not at the end of the code, still trying to get to where we are going
                if (nextPart == "."):  # got left
                    if (cur_parent.left is None):
                        return "[ERROR!!!!!!!]"
                    cur_parent = cur_parent.left
                elif (nextPart == "-"):  # go right
                    if (cur_parent.right is None):
                        return "[ERROR!!!!!!!]"
                    cur_parent = cur_parent.right
                else:
                    return "[ERROR!!!!!!!]"  # we are in trouble

        return "[ERROR!!!!!!!]"  # if we get back out here, we have a problem

    # working on inOrder to make this better
    def __str__(self):
        return self.inorderTraversal()




    # Trecursive inorder
    # does this need updating for Morse Tree??
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



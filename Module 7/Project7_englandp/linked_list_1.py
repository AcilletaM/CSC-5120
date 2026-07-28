
# we inherit from object by convention here (and possibly
# for compatibility with older versions of python).
# It used to be needed in python 2,
# but in python 3 it is no longer needed
class Node(object):  # One part of the data Linked List
    def __init__(self, data):  # Constructor
        self.data = data  # The data object for this Node
        self.next = None  # Reference to next Node

    def __str__(self):
        return str(self.data)


class LinkedList(object):  # A linked list of data elements
    # class variable to keep track of how many Nodes in list

    def __init__(self):  # Constructor
        self.__head = None  # Reference to start of the Linked List
        self.size = 0 # we don't have to keep track of size

    def isEmpty(self):  # Test for empty list
        return (self.size == 0)
        #return self.__head is None  # True if & only if no 1st Node

    def __len__(self):
        return self.size

    # add
    # assumptions for functions:
    # 1. assume we have a valid Linked List that we are adding to
    # 2. make sure all linked list parameters are updated in the function (as needed)
    # 3. at end of function, make sure we have a valid linked list
    # what's big O time?

    # We can re-write add so it DOESN'T have a loop?
    #      -> add can be improved by maintaining a 'tail' reference that always points to the last node in the list
    # add is O(n)
    def add(self, newDataToAdd): # new nodes added to end
        # we can assume, we have a valid linked list right now
        newNode = Node(newDataToAdd)
        # out here is 1 step
        steps = 1
        if (self.isEmpty()):
            self.__head = newNode
            self.size += 1
        else:
            # have size
            # we have __head
            # we have to traverse the list, starting at head, to get to the last node
            # I need a additional local reference, current (Node reference)
            current = self.__head
            while current.next != None:
                current = current.next
                # every time this loop runs, it adds another step
                steps += 1
            #now after the loop, what does current point to?
            # current points to LAST node in the list
            current.next = newNode
            self.size += 1


        # anything else: we don't think so...
        #print(f"steps for add: {steps}")

    # where head is index 0, head->next would be index 1, etc.
    def get(self, index: int): #
        # size is the same as n, so get(size) should cause error
        # see if you can code get

        #case 1, the is empty
        if (self.isEmpty()): # could cause an error or return false
            return None
        #case 2, bad index
        elif (index < 0 or index >= self.size):
            return None
        #else:
        #want to go to that index
        current = self.__head
        for i in range(index):
            current = current.next

        return current.data # we could return current,
        # by convention, we return data.


    # remove

    # TODO need to test for edge cases (removing first, last, list is empty, or index is out of bounds)
    def remove(self, index:int):


        # what if we remove(0)?
        # update the __head!!!!
        if (index == 0):
            # remove last node in list?
            if (self.size == 1):
                self.__head = None
            else:
                self.__head = self.__head.next
        else:
            # see picture from video
            # (i-1).next = (i.next)
            nodeIminus1 = self.getNode(index - 1)  # big O(n)
            nodeIplus1 = self.getNode(index + 1)

            nodeIminus1.next = nodeIplus1
        self.size -= 1

    # print
    # assmume we have a valid list coming in
    # this should be a "read only" function
    def __str__(self):
        cur = self.__head
        message = ""
        if (self.size == 0):  # empty list coming in
            return "empty linked list"
        else:  # we don't have an empty list
            while (cur.next is not None):
                message += f"{str(cur.data)} -> " # add the current node's data on to the message
                cur = cur.next
            message += str(cur.data)  # add the last node's data to the message
        return message


    def find(self, dataToLookFor) -> int: # return the index of the spot, or None if not found
        # returns the index where we found the value
        # returns None if not found

        current = self.__head

        # steps = 1

        for i in range(self.size): # this is the correct range
            if (current.data != dataToLookFor):
                current = current.next
                # steps +=1
            else:
                return i # could have retrned Node, or True
        # big O(n)
        return None

    # assumptions for functions:
    # 1. assume we have a valid Linked List that we are adding to
    # 2. make sure all linked list parameters are updated in the function (as needed)
    # 3. at end of function, make sure we have a valid linked list
    # what's big O time?
    def addAt(self, indexToAddAt: int, dataToAddThere):
        # Case 1: empty list (do we cause an error if index !=0 -> we decide not to)
            # so can just call add
        # Case 2: adding at beginning
        # Case 3: adding at end (can just call add)
        # Case 4: adding in the middle

        # we can assume, we have a valid linked list right now
        newNode = Node(dataToAddThere)

        # out here is 1 step
        # steps = 1
        if (self.isEmpty() or indexToAddAt >= self.size): # Case1 or Case 3
            self.add(dataToAddThere) #O(n)
        elif (indexToAddAt == 0): # Case 2 O(1)
            newNode.next = self.__head
            self.__head = newNode

            self.size += 1
        else: # adding to the middle, O(n)

            current = self.__head
            # when we want to insert something at index y, we are interested in
            # making changes to Node(y-1).next
            # we  use get(indexToAddAt -1)

            for i in range(indexToAddAt - 1):
                current = current.next

            #current now points to the node at indexToAddAt-1
            
            #alt
            # current = self.getNode(indexToAddAt - 1)


            # yourself these next two lines are correct, and test addAt function
            # what is big O of atAdd
            newNode.next = current.next
            current.next = newNode
            self.size += 1

    def getNode(self, index) -> Node :
        # size is the same as n, so get(size) should cause error
        # see if you can code get

        # case 1, the is empty
        if (self.isEmpty()):  # could cause an error or return false
            return None
        # case 2, bad index
        elif (index < 0 or index >= self.size):
            return None
        # else:
        # want to go to that index
        current = self.__head
        for i in range(index):
            current = current.next

        return current  # we could return current,
        # by convention, we return data.
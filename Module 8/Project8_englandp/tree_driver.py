from binary_search_tree import BST, Node
from timeit import default_timer as timer

class Student:
    def __init__(self, id, name, major, gpa):
        self.id = id
        self.name = name
        self.major = major
        self.gpa = gpa

    def __str__(self):
        message = f"Name:{self.name}, id:{self.id}"
        return message

def main():
    print("BST driver!")
    mystudents = BST()
    student1 = Student(1234, "Jon", "CS", 3.1)
    mystudents.add(student1.id, student1)
    student2 = Student(1233, "Jill", "CS", 3.5)
    mystudents.add(student2.id, student2)
    student3 = Student(1235, "Jane", "CS", 3.9)
    mystudents.add(student3.id, student3)

    print(f"printing student tree: {mystudents}")

    print("about to look for 1235")
    print(mystudents.find(1235))
    print("about to look for 9999")
    print(mystudents.find(9999))

    """
    mywords = BST()

    mywords.add("mom")
    mywords.add("sister")
    mywords.add("dad")


    #print(mywords)

"""
    my_BST = BST() # creates an empty BST, size 0, and root points to None

    my_BST.add(4, 4) # for ints, key and data are the same
    my_BST.add(6, 6)
    my_BST.add(2, 2)
    my_BST.add(1, 1)
    my_BST.add(3, 3)
    my_BST.add(5, 5)
    my_BST.add(6, 6)

    print(my_BST)
    """
    start = timer()
    # we are timing the code between start and end
    for i in range(200): # when you double this number, the time more than doubles. why? O(n^2)
        my_linked_list.add(Node(i))
    end = timer()
    print(f"time to add numbers: {end - start} seconds")  # Time in seconds, e.g. 5.38091952400282
    """
if __name__ == "__main__":
    main()

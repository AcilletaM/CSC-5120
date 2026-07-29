# CSC 5120 Module 7 Project
# Paul England
# Instructions
#
# The goal of the seventh project is to compare the "step" and timing results for storing and retrieving data from two different data structures: the singly linked list 
# we developed in class and a built in Python Array. We will also analyze the Big O upper bound (in terms of the n items stored) for our insert and retrieval methods. 
#
# Write Python code that generates a 10,000 random numbers between 1 and 1,000,000. 
#   - Store those numbers in an instance of our singly linked list, and the same set of numbers in a Python array (a python list []). 
#   - Count the number of steps (as we discussed in class) for the linked list add operation, and compare it to n (which is 10,000 here at the end, but is smaller for earlier adds).
#   - Time how long it takes to insert all 10,000 numbers for both the linked list and the array, compare (print out explanations) this to each other and to the number of steps for LL.
#   - Pick a number that you know is stored as one of the 10,000 entries near the beginning of the batch, and retrieve (get) it by index for both array and LL, counting steps for the linked list get and timing both while you do. Analyze the results (print out explanations).
#   - Retrieve the 7000th number for the LL and from the Array, counting steps and timing while you do. Analyze the results.
#
# Consider the following questions, and provide answers in a text file included with your submission:
#   - Which data structure is better at insertion, which is better at retrieval of the nth (7000th in our case) number?
#   - Which would be better at deletion of the nth number? The 1st number?

# Load random, timer, and LinkedList.
import random
from timeit import default_timer as timer
from linkedlist import LinkedList

def main():
    """Compare step counts and timing for a linked list versus a Python array."""
    print("Linked List driver!\n")

    # Generate the random numbers once so both structures store the same set.
    randomnumbers = []
    for loop in range(10000):
        randomnumbers.append(random.randint(1, 1000000))

    print("Load the linked list with 10,000 random values.")
    # Create the empty linked list.
    mylinkedlist = LinkedList()

    # Loop through the list of numbers and adding to the linked list.
    totalsteps = 0
    start = timer()
    for number in randomnumbers:
        mylinkedlist.append(number)
        totalsteps += mylinkedlist.steps
    end = timer()

    # Capture the final append's step count before any get() overwrites it.
    finalappendsteps = mylinkedlist.steps

    print(f"Time to add 10,000 numbers to a linked list: {end - start} seconds and {totalsteps} steps.")
    print(f"The final append alone took {finalappendsteps} steps, essentially n, since it walks every node already in the list.")

    print("Load the array with 10,000 random values.")
    # Create the empty array.
    myarray = []

    start = timer()
    # Loop through the list of numbers and adding to the array.
    for number in randomnumbers:
        myarray.append(number)
    end = timer()
    print(f"Time to add 10,000 numbers to an array: {end - start} seconds.")

    print("In comparison, the linked list did about 50 million steps for the same 10,000 inserts the array did nearly instantly, which is why its load time is so much larger.")

    # Pick a value we know is near the beginning of the batch.  I will use index value of 13.
    knownvalue = randomnumbers[13]
    print(f"\nRetrieve the known value {knownvalue} from index 13 of both structures.")

    start = timer()
    linkedlistnode = mylinkedlist.get(13)
    end = timer()
    totalsteps = mylinkedlist.steps
    print(f"Linked list get(13): {end - start} seconds and {totalsteps} steps.  Value is {linkedlistnode.data}")

    start = timer()
    arrayvalue = myarray[13]
    end = timer()
    print(f"Array [13]: {end - start} seconds and 1 step.  Value is {arrayvalue}.")

    print("This close to the head both structures should be near instant; the gap only opens deeper in the list.")

    # NOTE!!!
    # The instructions and the scoring rubric use 7000th number and 7000th index in different places.
    # I will use index value of 6999 as 7000th number is used more.
    knownvalue = randomnumbers[6999]
    print(f"\nRetrieve the known value {knownvalue} from index 6999 of both structures.")

    start = timer()
    linkedlistnode = mylinkedlist.get(6999)
    end = timer()
    totalsteps = mylinkedlist.steps
    print(f"Linked list get(6999): {end - start} seconds and {totalsteps} steps.  Value is {linkedlistnode.data}")

    start = timer()
    arrayvalue = myarray[6999]
    end = timer()
    print(f"Array [6999]: {end - start} seconds and 1 step.  Value is {arrayvalue}.")

    print(f"Both structures returned the same value: {linkedlistnode.data == arrayvalue}")
    print(f"This is where the separation becomes apparent: {totalsteps} steps for the linked list versus 1 for the array.")
    print("\nIn comparison, retrieving by index from an array stays nearly constant at any position, while the linked list must walk the chain, so the gap grows as n increases.")

if __name__ == "__main__":
    main()
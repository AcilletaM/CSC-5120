CSC 5120 Module 7 Project
Paul England

Answers to the analysis questions for the linked list versus Python array comparison.
The step counts below come from the counters built into my LinkedList class and driver
(englandp7.py). Note: I used index 6999 as the 7000th number since the list is 0-indexed.

Question 1: Which data structure is better at insertion?

The array is much better at insertion. Every append to my linked list has to
walk the entire list to find the last node, so the cost of each insert grows with the
size of the list. My driver counted 49,995,001 total steps to load 10,000 numbers, which
is about n squared over 2. The array appends each number instantly, so the same 10,000 inserts 
are just 10,000 units of work. This also showed in the times: the linked list load takes
dramatically longer than the array load for identical data.  The linked list insertion 
is O(n) per operation and the array is O(1).

Question 2: Which is better at retrieval of the nth (7000th in our case) number?

The array is better for nearly the same reason as in question 1. Retrieving index 
6999 from the array is 1 step. The linked list must traverse the list, taking 6999 
steps.  That is O(1) for the array versus O(n) for the linked list. The gap is 
invisible near the head (get(13) was only 14 steps) but grows with the index.

Question 3: Which would be better at deletion of the nth (7000th) number?

This one is much closer because both are O(n), but for different reasons.  My linked 
list remove must first walk the chain to reach the nodes around index 6999 (my 
implementation calls get twice, about 14,000 steps total) and then does the actual
removal in constant time with one pointer change. The array finds index 6999 instantly
but then has to shift every element after it down one slot to close the gap, roughly
3,000 shifts in this case. In Big O terms both are O(n).

Question 4: Which would be better at deletion of the 1st number?

This is the only win for the linked list. My remove(0) is a single pointer move,
self.__head = self.__head.next, which is O(1) no matter how many nodes are in the list.
Deleting index 0 from the array is its worst case: all 9,999 remaining elements have to
shift down one position, which is O(n). 
CSC 5120 Module 8 Project
Paul England

Answers to the analysis questions for the binary search tree iterative versus recursive comparison. The step counts 
below come from the self.steps counter built into my BST class and driver (englandp8.py). The driver generates fresh 
random numbers on every run, so the exact counts shift a little from run to run.  The numbers here are from one 
representative run but the pattern holds across runs.

Question 1: Which is better for insertion: recursion or our original method?

Generally both methods were the same.  Both versions build the same tree structure with the same number of nodes
and levels.  My run counted 168,990 steps for the iterative load and 168,936 for the recursive load of the same 10,000 
numbers. The difference of 54 is exactly the number of duplicate keys the tree rejected.  For the iterative method, it
still requires a step to reject the duplicate. My driver program verifies that duplicate equality on every run. Both 
methods are O(log n) per insert on average with random keys, and both share the same O(n) worst case when sorted 
input degrades the tree into a chain.  There was a small differance in time that favored the iterative method.  
Multiple function calls for the recursive method added time to the process, but not enough a user would notice with 
the number of nodes we are adding. It is also not enough to offset the gain by using the recursion method to find
a node.  Recursion was much faster, especially the further down the tree the program had to search.  If I had to pick
one methodology for inserts, finds, and even deletes, recursion would be my choice because of the real search speed 
gains.

Question 2: Without code, explain how you would delete a number from the tree.

Deleting would be like doing a find: walk down from the root comparing keys, going left when the target key is smaller 
and right when it is larger.  Only difference is it would have to remember the parent and which side you came down. If 
the key is never found, there is nothing to delete. When the node is found, what happens next depends on the number of 
children it has.

No children (a leaf): Point the parent's link that led to the node at None. The node drops out of the tree.
One child: Point the parent's link past the node at the node's only child. The parent adopts the child's child, and the 
entire subtree under that child shifts up to the parent while still maintaining order.
Two children:  This one is tricky because you can't simply unlink the child from the parent by pointing the child's
children at the parent.  Instead of removing the node, replace its contents. Find the in-order successor, which is the 
smallest key in the right subtree: step right once, then keep stepping left until there is no left child. Copy the 
successor's key and data onto the node being deleted. The ordering stays valid because the successor's key is larger 
than everything in the node's left subtree and smaller than everything else in its right subtree. Then delete the 
successor node from the right subtree, which is guaranteed to be Case 1 or Case 2, because by construction the 
successor has no left child.

Because my tree rejects duplicate keys, delete never has to decide which of several equal keys to remove.  

delete(key):
    walk from the root to the node with the key,
        remembering the parent and which side we came down
    if the key is not found:
        return

    if the node has two children:
        successor = right child, then left until there is no left child
            (remember the successor's parent along the way)
        copy successor.key and successor.data onto the node
        node = successor
        parent = the successor's parent

    # The node to unlink now has zero children or one child.
    child = the node's left child if it exists, otherwise its right child
        (child is None when the node is a leaf)
    if the node is the root:
        root = child
    else if the parent's left is the node:
        parent.left = child
    else:
        parent.right = child
    size = size - 1
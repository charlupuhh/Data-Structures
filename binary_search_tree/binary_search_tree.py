"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue 
from stack import Stack 

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
                return value
            else:
                self.right.insert(value)
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
                return value
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.value is None:
            return
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        curr_node = self
        # instantiate a queue
        q = Queue()
        # enqueue our starting node (self)
        q.enqueue(curr_node)
        # while the queue is not empty
        while len(q) > 0:
            # dequeue the current node
            curr_node = q.dequeue()
            # print the nodes value
            print(curr_node.value)
            # check if left child exists
            if curr_node.left is not None:
                # enqueue left child
                q.enqueue(curr_node.left)

            # check if right child exists
            if curr_node.right is not None:
                # enqueue right child            
                q.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        curr_node = self
        # instantiate a stack
        q = Stack()
        # push our starting node (self)
        q.push(curr_node)
        # while the stack is not empty
        while len(q) > 0:
            # pop the current node
            curr_node = q.pop()
            # print the nodes value
            print(curr_node.value)

            # check if left child exists
            if curr_node.left is not None:
                # push left child
                q.push(curr_node.left)

            # check if right child exists
            if curr_node.right is not None:
                # push right child
                q.push(curr_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  

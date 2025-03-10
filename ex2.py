import timeit
import random
from bisect import bisect_left

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

# Binary search 
def binary_search(arr, value):
    index = bisect_left(arr, value)
    return index < len(arr) and arr[index] == value

# Generate and shuffle vector
vector = list(range(10000))
random.shuffle(vector)

# Build BST
bst = BST()
for num in vector:
    bst.insert(num)

# Measure BST search time
bst_search_time = timeit.timeit(lambda: [bst.search(num) for num in vector], number=10) / 10

# Sort vector for binary search
vector.sort()

# Measure binary search time
binary_search_time = timeit.timeit(lambda: [binary_search(vector, num) for num in vector], number=10) / 10

# Print results
print(f"BST search time (average over 10 runs): {bst_search_time:.6f} seconds")
print(f"Binary search time (average over 10 runs): {binary_search_time:.6f} seconds")

# Discussion (included as a comment)

"""
Binary search on an array is significantly faster than searching in a BST. This is due to
cache efficiency and the reduced overhead of recursive function calls. BST search involves
pointer dereferencing and recursion, which add to execution time. On the other hand,
binary search on an array leverages contiguous memory access, making it more efficient.
Additionally, Python's built-in sorting algorithms are optimized, making array-based search
very fast.
"""

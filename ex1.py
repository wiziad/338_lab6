#question 1: Implement a binary search tree with insertion and search operations as seen in class [0.2 pts]
import random
import timeit

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

''' question 2 : Measure search performance using timeit as follows: [0.3 pts]
1. Generate a 10000-element sorted vector and use it to build a tree by inserting
each element
2. Search each element. Time the search (averaged across 10 tries for each
element), and return average and total time '''

def measure_search_time(bst, values):
    total_time = 0
    for key in values:
        total_time += timeit.timeit(lambda: bst.search(key), number=10)
    average_time = total_time / len(values)
    return average_time, total_time

# Create a sorted vector
sorted_vector = list(range(10000))

# Build BST from sorted vector
bst_sorted = BST()
for num in sorted_vector:
    bst_sorted.insert(num)

# Measure search time for sorted BST
avg_time_sorted, total_time_sorted = measure_search_time(bst_sorted, sorted_vector)

print(f"Sorted Insertion BST - Average Search Time: {avg_time_sorted:.6f} sec")
print(f"Sorted Insertion BST - Total Search Time: {total_time_sorted:.6f} sec")


''' question 3: Measure search performance using timeit as follows: [0.3 pts]
1. Shuffle the vector used for question 2 (using random.shuffle)
2. Search each element. Time the search (averaged across 10 tries for each
element), and return average and total time '''

# Shuffle the vector
random.shuffle(sorted_vector)

# Build BST from shuffled vector
bst_shuffled = BST()
for num in sorted_vector:
    bst_shuffled.insert(num)

# Measure search time for shuffled BST
avg_time_shuffled, total_time_shuffled = measure_search_time(bst_shuffled, sorted_vector)

print(f"Shuffled Insertion BST - Average Search Time: {avg_time_shuffled:.6f} sec")
print(f"Shuffled Insertion BST - Total Search Time: {total_time_shuffled:.6f} sec")


#question 4. Discuss the results. Which approach is faster? Why? [0.2 pts]
''' When inserting elements in sorted order, the BST becomes highly unbalanced, resembling a linked list 
where each node only has a right child. This results in search operations having a time complexity of O(n), 
making them significantly slower. On the other hand, when the elements are inserted in a shuffled order, 
the BST is more balanced, leading to an average search time complexity of O(log n). Consequently, searches 
in the shuffled BST are much faster compared to the sorted-insertion BST. The results clearly demonstrate 
that balanced trees perform better in search operations, highlighting the importance of maintaining balance in BSTs. '''
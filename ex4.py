import heapq
import random
import unittest

class Heap:
    def __init__(self):
        self.data = []
    
    def heapify(self, arr):
        self.data = arr[:]
        heapq.heapify(self.data)
    
    def enqueue(self, value):
        heapq.heappush(self.data, value)
    
    def dequeue(self):
        if self.data:
            return heapq.heappop(self.data)
        return None

class TestHeap(unittest.TestCase):
    def test_already_heapified(self):
        heap = Heap()
        arr = [1, 3, 5, 7, 9, 11]
        heap.heapify(arr)
        self.assertEqual(heap.data, arr)  # Already heapified array should remain unchanged
    
    def test_empty_heap(self):
        heap = Heap()
        arr = []
        heap.heapify(arr)
        self.assertEqual(heap.data, [])  # Empty array should remain empty
    
    def test_random_list(self):
        heap = Heap()
        arr = list(range(100))
        random.shuffle(arr)
        heap.heapify(arr)
        self.assertEqual(heap.data, sorted(arr))  # Min-heap property should hold

if __name__ == "__main__":
    unittest.main()

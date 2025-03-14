# 338 Lab 6 Exercise 5

import random
import timeit

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1) ListPriorityQueue
class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None or self.head.value > value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.value <= value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue from empty priority queue")
        min_value = self.head.value
        self.head = self.head.next
        return min_value

# 2) HeapPriorityQueue
class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            raise IndexError("dequeue from empty priority queue")
        if len(self.heap) == 1:
            return self.heap.pop()
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Generating tasks
def generate_tasks(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(1, 100)))
        else:
            tasks.append(('dequeue',))
    return tasks

# 3) Function to measure execution time
def measure_time(queue_class, tasks):
    queue = queue_class()
    start_time = timeit.default_timer()
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueue(task[1])
        elif task[0] == 'dequeue':
            try:
                queue.dequeue()
            except IndexError:
                pass
    end_time = timeit.default_timer()
    return end_time - start_time

if __name__ == "__main__":
    num_tasks = 1000
    tasks = generate_tasks(num_tasks)

    # Timing ListPriorityQueue
    list_time = measure_time(ListPriorityQueue, tasks)
    print(f"ListPriorityQueue time: {list_time:.6f} seconds")

    # Timing HeapPriorityQueue
    heap_time = measure_time(HeapPriorityQueue, tasks)
    print(f"HeapPriorityQueue time: {heap_time:.6f} seconds")

    # Calculating the average time per task
    avg_list_time = list_time / num_tasks
    avg_heap_time = heap_time / num_tasks
    print(f"Average time per task (ListPriorityQueue): {avg_list_time:.6f} seconds")
    print(f"Average time per task (HeapPriorityQueue): {avg_heap_time:.6f} seconds")

'''
4) I ran this program on my terminal and my output was:
        ListPriorityQueue time: 0.002119 seconds
        HeapPriorityQueue time: 0.001307 seconds
        Average time per task (ListPriorityQueue): 0.000002 seconds
        Average time per task (HeapPriorityQueue): 0.000001 seconds 
Based on the output, the HeapPriorityQueue is faster than the ListPriorityQueue. This is because it has a logarithmic time complexity (O(log n)) for enqueue and dequeue operations. Nonetheless, the ListPriorityQueue has linear time complexity (O(n)), hence being less efficient.

'''

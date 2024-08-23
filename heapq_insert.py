import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child_(self, index):
        return (2 * index) + 1

    def _right_child_(self, index):
        return (2 * index) + 2
    
    def _parent(self, index):
        return (index - 1)//2
    
    def insert(self, vertex):
        self.heap.append(vertex)
        return heapq._heapify_max(self.heap)
    
    def remove(self):
        return heapq.heappop_max(self.heap)

myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)  


myheap.insert(100)

print(myheap.heap)  


myheap.insert(75)

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""
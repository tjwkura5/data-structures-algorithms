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
       return heapq._heappop_max(self.heap)

    def sink_down(self, index):
        return heapq._siftdown_max(self.heap, index) 
    
# myheap = MaxHeap()
# myheap.insert(95)
# myheap.insert(75)
# myheap.insert(80)
# myheap.insert(55)
# myheap.insert(60)
# myheap.insert(50)
# myheap.insert(65)

# print(myheap.heap)


# myheap.remove()

# print(myheap.heap)


# myheap.remove()

# print(myheap.heap)


# """
#     EXPECTED OUTPUT:
#     ----------------
#     [95, 75, 80, 55, 60, 50, 65]
#     [80, 75, 65, 55, 60, 50]
#     [75, 60, 65, 55, 50]

# """
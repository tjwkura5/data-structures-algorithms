import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        heapq._heapify_max(self.heap)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        return heapq._heappop_max(self.heap)
    

myheap = MaxHeap()
myheap.push(99)
myheap.push(72)
myheap.push(61)
myheap.push(58)

print(myheap.heap)  


myheap.push(100)

print(myheap.heap)  


myheap.push(75)

print(myheap.heap)

myheap.pop()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]
    [99, 75, 58, 72, 61]

"""       
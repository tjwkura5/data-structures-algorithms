import heapq
class MinHeap:
    def __init__(self):
        self.heap = []
        
    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)
    


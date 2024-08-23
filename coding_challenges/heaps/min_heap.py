class MinHeap:
    def __init__(self):
       self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2
        
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, vertex):
        self.heap.append(vertex)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self.swap(current, self._parent(current))
            current = self._parent(current)
        
        
    def _sink_down(self, index):
        min_index = index 
        while True:
            left = self._left_child(min_index)
            right = self._right_child(min_index)
            
            if (left < len(self.heap)) and self.heap[left] < self.heap[min_index]:
                min_index = left
            if (right < len(self.heap)) and self.heap[right] < self.heap[min_index]:
                min_index = right
                
            if index != min_index:
                self.swap(index, min_index)
                index = min_index
            else:
                return 
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value  = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        
        return min_value



myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]



"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]

"""
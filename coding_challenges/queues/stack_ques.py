class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def top(self):
        return self.tail.value
    
    def empty(self):
        return len(self.length) == 0
    
    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1


    def pop(self):
        if self.length == 0:
            return None
        curr = self.head
        pre = self.head
        while(curr.next):
            pre = curr
            curr = curr.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return curr.value
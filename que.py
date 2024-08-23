class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Que():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1

    def print_que(self):
        temp = self.first
        while(temp):
            print(temp.value)
            temp = temp.next 
    
    #pop_first()
    def dequeue(self):
        if self.height == 0:
            return None
        temp = self.first
        if self.height == 1:
            self.first = None
            self.last = None
        self.first = self.first.next
        temp.next = None
        self.height -= 1
        return temp

    # Append
    def enqueue(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height += 1

my_queue = Que(1)
my_queue.enqueue(2)

my_queue.print_que()
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None 

    class DoublyLinkedList:
        def __init__(self, value):
            node = Node(value)
            self.head = node
            self.tail = node
            self.length = 1

        def get(self, index):
            if index < 0 or index >= self.length:
                return None
            if index == 0 or index == 1:
                if index == 0:
                    return self.head
                else:
                    return self.head.next 
            if index == self.length -1 or index == self.length - 2:
                if index == self.length -1:
                    return self.tail
                else:
                    return self.tail.prev
            curr = self.head
            for _ in range(index):
                curr = curr.next

            return curr
        
        def prepend(self, value):
            node = Node(value)
            if self.length == 0:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node 
            self.length +=1

        def append(self, value):
            node = Node(value)
            if self.length == 0:
                self.head = node
                self.tail = node
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            self.length += 1 

        def insert(self, index, value):
            if index < 0 or index > self.length:
                return None
            if index == 0:
                self.append(value)
                return self.head
            if index == self.length:
                self.prepend(value)
                return self.tail
             
            node = node(value)
            curr = self.get(index)
            before = curr.prev
            before.next = node 
            curr.prev = node 
            node.prev = before 
            node.next = curr

            self.length +=1
            return node
            

        def pop(self):
            if self.length == 0:
                return None
            
            temp = self.tail 
            prev = self.tail.prev
            self.tail.prev = None
            self.tail.next = None
            self.tail = prev
            self.length -= 1

            if self.length == 0:
                self.head = None
                self.tail =  None

            return temp
        
        def remove(self, index):
            if index < 0 or index >= self.length:
                return None
            
            if index == 0:
                temp = self.head
                nxt = self.head.next
                nxt.prev = None
                self.head.next = None
                self.head = nxt 
                self.length -= 1

                return temp
            if index == self.length - 1:
                return self.pop()
            
            deletable = self.get(index)
            before = deletable.prev
            after = deletable.next
            before.next = None
            after.prev = None
            deletable.next = None
            deletable.prev = None 


            self.length -= 1
            return deletable
            



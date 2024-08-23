class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, n):
        # using the pushback function from dynamic arrays to add to the stack
        self.stack.append(n)

    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        return self.stack.pop()

        
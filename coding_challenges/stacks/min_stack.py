class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        self.stack.append(value)
        val = min(value, self.minStack[-1] if self.minStack else value)
        self.minStack.append(val)
    
    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]
    

minStack = MinStack();

minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin()) 
minStack.pop();
print(minStack.top())   
print(minStack.getMin())
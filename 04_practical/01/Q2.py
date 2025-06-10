class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    

    Stack = Stack()
    Stack.push(10)
    Stack.push(20)
    print(Stack.peak())
    print(Stack.pop())
    print(Stack.is_empty())
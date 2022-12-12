# Stack 구현
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        print(self.stack)
    

stack1 = Stack()
stack1.push(1)
print(stack1.size())
print(stack1.top())

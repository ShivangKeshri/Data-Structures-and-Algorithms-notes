class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stack.pop()

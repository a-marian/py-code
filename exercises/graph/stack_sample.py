class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if self.items:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek()) # output: 3

print(stack.pop()) # output: 3
print(stack.pop()) # output: 2
print(stack.pop()) # output: 1
print(stack.pop()) # Output: None (stack is empty)

print(stack.is_empty()) # Output: True
# Run with python3
class Stack:
    def __init__(self):
        self.items = []

    # List methods for completeness
    def append(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def clear(self):
        self.items.clear()

    # Stack methods
    def push(self, item):
        self.items.append(item)

    def pop(self):
        # Now exactly as list.pop(), will raise IndexError if empty
        return self.items.pop()

    def peek(self):
        # Now like list[-1], raises IndexError if empty
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    # List-like interface
    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

    def __repr__(self):
        return f"Stack({self.items})"

s = Stack()
#This will now raise:
try:
    s.pop()
except Exception as e:
    print(type(e).__name__)

try:
    s.peek()
except Exception as e:
    print(type(e).__name__)


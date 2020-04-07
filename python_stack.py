# A Stack
# A stack is a data strucutre that adds and removed elements in a particular order
# Every time an element is added it goes on "top" of the stack. Follows LILO scheme.
# Push onto the stack, pop off the stack

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item) # push item to top of the stack

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)


s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack()

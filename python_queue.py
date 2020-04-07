# Queue
# A queue is a simple structure that allows elements to be inserted from one end (rear, or tail)
# and deleted from the other end (front, or head)
# follows FIFO (first in first out), opposite to the stack.
# added elements is called enqueue and removing is dequeue
# used whenever we need to manage objects in order starting with the first one in.
# examples (printing queue, call system answers queue)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop() # here is the different from stack

    def print_queue(self):
        print(self.items)

s = Queue()
s.enqueue('a')
s.enqueue('b')
s.enqueue('c')
s.print_queue()

s.dequeue()
s.print_queue()

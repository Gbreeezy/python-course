# Examples of linked list in python

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def add_at_front(self, data):
        """
        Function to add a node to front
        :param data:
        :return:
        """
        self.head = Node(data=data, next=self.head)

    def is_empty(self):
        """
        Function to check whether the list is empty
        :return:
        """
        return self.head == None

    def add_at_end(self, data):
        """
        Function to add node to the end
        :return:
        """
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)


    def delete_node(self, key):
        """
        function to delete any node
        :return:
        """
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None


    def get_last_node(self):
        """
        Function to get the last node
        :return:
        """
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp.data

    def print_list(self):
        """
        Function to to print the list nodes
        :return:
        """
        node = self.head
        while node != None:
            print(node.data, end = " => ")
            node = node.next


s = LinkedList()
s.add_at_front(5)
s.print_list()
s.add_at_front(10)
s.print_list()
s.add_at_end(8)
s.print_list()
s.add_at_front(9)
s.print_list()
s.delete_node(0)

s.print_list()
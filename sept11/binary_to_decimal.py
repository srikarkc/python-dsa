class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Some methods have been omitted

    def binary_to_decimal(self):
        curr = self.head
        decimal = 0
        while curr is not None:
            decimal = (decimal * 2) + curr.value
            curr = curr.next
        return decimal
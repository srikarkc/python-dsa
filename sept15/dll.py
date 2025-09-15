class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Some methods omitted

    def reverse(self):
        if not self.head:
            return
        
        curr = self.head

        while curr:
            prev = curr.prev
            curr.prev, curr.next = curr.next, prev

            curr = curr.prev

        self.head, self.tail = self.tail, self.head

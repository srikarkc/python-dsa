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

# Omit some methods

    def reverse_between(self, start_index, end_index):
        if not self.head or start_index == end_index:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for i in range(start_index):
            prev = prev.next

        curr = prev.next

        for i in range(end_index - start_index):
            next_node = curr.next

            curr.next = next_node.next
            if next_node.next:
                next_node.next.prev = curr

            next_node.next = prev.next
            prev.next.prev = next_node
            prev.next = next_node
            next_node.prev = prev
        
        self.head = dummy.next
        self.head.prev = None

    def swap_pairs(self):
        if not self.head:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = None
        prev, current = dummy, self.head

        while current and current.next:
            next_node = current.next

            current.next = next_node.next
            if next_node.next:
                next_node.next.prev = current
            
            prev.next = next_node
            current.prev = next_node
            next_node.next = current
            next_node.prev = prev

            prev = current
            current = current.next

        self.head = dummy.next
        self.head.prev = None
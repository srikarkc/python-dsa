class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head, self.tail = new_node, new_node
        self.length = 1

# Omit some methods

    def reverse_between(self, left, right):
        if not self.head or left == right:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for i in range(left):
            prev = prev.next

        curr = prev.next
        
        for i in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        self.head = dummy.next
        
    def swap_pairs(self):
        if not self.head:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        curr = prev.next
        while curr and curr.next:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

            prev = curr
            curr = curr.next
        
        self.head = dummy.next
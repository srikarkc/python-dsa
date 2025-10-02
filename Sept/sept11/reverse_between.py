class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(0)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for i in range(start_index):
            prev = prev.next

        curr = prev.next

        for i in range(end_index - start_index):
            node_to_move = curr.next
            curr.next = node_to_move.next
            node_to_move.next = prev.next
            prev.next = node_to_move

        self.head = dummy.next
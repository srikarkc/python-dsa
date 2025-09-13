class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.left = new_node
        self.right = new_node
        self.length = 1

    # miss some methods

    def reverse_between(self, left, right):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for i in range(left):
            prev = prev.next

        curr = prev.next

        for i in range(right - left):
            node_to_move = curr.next
            curr.next = node_to_move.next
            node_to_move.next = prev.next
            prev.next = node_to_move

        return dummy.head
    
    def swap_pairs(self):
        if not self.head or not self.head.next:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Swap
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev to the next pair
            prev = first

        self.head = dummy.next

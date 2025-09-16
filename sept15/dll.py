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

    def parition_list(self, value):
        if not self.head:
            return
        
        dummy1 = Node(0)
        dummy2 = Node(0)

        dp1 = dummy1
        dp2 = dummy2

        curr = self.head

        while curr:
            next_node = curr.next

            if curr.value < value:
                dp1.next = curr
                curr.prev = dp1
                dp1 = dp1.next
            else:
                dp2.next = curr
                curr.prev = dp2
                dp2 = dp2.next
            
            curr.next = None
            curr = next_node
        
        dp1.next, dp2.next = None, None

        if dummy1.next and dummy2.next:
            dp1.next = dummy2.next
            dummy2.next.prev = dp1
            self.head = dummy1.next
        elif dummy1.next:
            self.head = dummy1.next
        elif dummy2.next:
            self.head = dummy2.next
        else:
            self.head = None
        
        if self.head:
            self.head.prev = None

    # Cannot reproduce this solution without looking at the answer
    def reverse_list(self, start_index, end_index):
        if not self.head or start_index == end_index:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        prev = dummy
        
        for _ in range(start_index):
            prev = prev.next

        current = prev.next

        for _ in range(end_index - start_index):
            node_to_move = current.next

            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current
            
            node_to_move.next = prev.next
            prev.next.prev = node_to_move
            prev.next = node_to_move
            node_to_move.prev = prev

        self.head = dummy.next
        self.head.prev = None
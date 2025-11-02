class Node:
    def __init__(self, value):
        self.value = value
        self.next, self.prev = None, None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head, self.tail = new_node, new_node
        self.length = 1

    # Omitting some methods


    # Problem 1 - Palindrome checker
    def palidrome_checker(self):
        left, right = self.head, self.tail

        for i in range(self.length // 2):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev

        return True
    

    # Problem 2 - reverse the doubly linked list
    def reverse(self):
        if not self.head or self.head is self.tail:
            return True
        
        curr = self.head

        while curr:
            prev = curr.prev
            curr.prev, curr.next = curr.next, prev

            curr = curr.prev

        self.head, self.tail = self.tail, self.head


    # Problem 3 - Partition list at a certain value
    def partition_list(self, k):

        if not self.head:
            return
        
        dummy1, dummy2 = Node(0), Node(0)
        dp1, dp2 = dummy1, dummy2

        current = self.head

        while current:
            next_node = current.next

            if current.value < k:
                dp1.next = current
                current.prev = dp1
                dp1 = dp1.next
            else:
                dp2.next = current
                current.prev = dp2
                dp2 = dp2.next

            current.next = None
            current = next_node

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


    # Problem 4 - Reverse between
    def reverse_between(self, start_index, end_index):
        if self.length <= 1 or start_index == end_index:
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


    # Problem 5 - Swap pairs
    def swap_pairs(self):
        if not self.head:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        prev, current = dummy, self.head

        while current and current.next:
            next_node = current.next

            current.next = next_node.next
            if next_node.next:
                next_node.next.prev = current

            prev.next = next_node
            next_node.prev = prev
            next_node.next = current
            current.prev = next_node

            prev = current
            current = current.next

        self.head = dummy.next
        self.head.prev = None
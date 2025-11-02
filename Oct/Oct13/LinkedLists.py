class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head, self.tail = new_node, new_node
        self.length = 1

    # some methods omitted

    # problem - remove duplicates (solved using sets)
    def remove_duplicates(self):
        values = set()
        slow, fast = None, self.head
        slow.next = self.head

        while fast:
            if fast.value in values:
                slow.next = fast.next
                self.length -= 1
            else:
                values.add(fast.value)
                slow = fast
            fast = fast.next

    # problem - binary to decimal
    def binary_to_decimal(self):
        current = self.head
        decimal = 0

        while current:
            decimal = (2 * decimal) + current.value
            current = current.next

        return decimal
    
    # problem - parition list (hard problem)
    def partition_list(self, k):
        dummy1, dummy2 = Node(0), Node(0)

        prev1, prev2 = dummy1, dummy2
        current = self.head

        while current is not None:
            if current.value < k:
                prev1.next = current
                prev1 = prev1.next
            elif current.value >= k:
                prev2.next = current
                prev2 = prev2.next
            current = current.next

        prev2.next = None
        prev1.next = dummy2.next

        self.head = dummy1.next

    # problem - reverse between (possible the hardest problem)
    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for i in range(start_index):
            prev = prev.next

        current = prev.next

        for i in range(end_index - start_index):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = prev.next
            prev.next = node_to_move

        self.head = dummy.next


    # problem - swap pairs (linked lists)
    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
        
        self.head = dummy.next
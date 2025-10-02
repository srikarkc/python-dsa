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

    # Some methods omitted

    def parition(self, value):
        dummy1, dummy2 = Node(0), Node(0)
        prev1, prev2 = dummy1, dummy2

        curr = self.head

        while curr is not None:
            if curr.value < value:
                prev1.next = curr
                prev1 = prev1.next
            elif curr.value >= value:
                prev2.next = curr
                prev2 = prev2.next
            curr = curr.next

        prev2.next = None

        # Attache the first partition with the second
        prev1.next = dummy2.next

        # Update the head pointer
        self.head = dummy1.next
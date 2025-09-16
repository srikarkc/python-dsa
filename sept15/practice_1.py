class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = None
        self.tail = None
        self.length = 1

# Omit some methods

def partition_list(self, x):
    if not self.head:
        return
    
    dummy1, dummy2 = Node(0), Node(0)

    dp1, dp2 = dummy1, dummy2

    curr = self.head

    while curr:
        next_node = curr.next

        if curr.value < x:
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


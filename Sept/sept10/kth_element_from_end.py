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

def kth_element_from_end(ll, k):
    slow = ll.head
    fast = ll.head

    for i in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow
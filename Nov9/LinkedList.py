class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head, self.tail = new_node, new_node
        self.length = 1

    def reverse(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

def reverseKGroup(head, k):
    curr = head
    count = 0
    while curr and count < k:
        curr = curr.next
        count += 1

    if count < k:
        return head
    
    prev = None
    curr = head
    for i in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    
    # 'prev' is now the head of the reversed group
    # 'head' is now the tail of the reversed group
    # 'curr' points to the start of the next group

    # Recursively reverse remaining groups and connect
    head.next = reverseKGroup(curr, k)

    return prev
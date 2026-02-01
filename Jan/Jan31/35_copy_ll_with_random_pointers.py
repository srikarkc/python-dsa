class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return
        
        # 1 - Weave
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 2 - set random pointer
        curr = head
        while curr:
            copy = curr.next
            copy.random = curr.random.next if curr.random else None
            curr = copy.next

        # 3 - unweave separate copy
        curr = head
        copy_head = curr.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return copy_head
    
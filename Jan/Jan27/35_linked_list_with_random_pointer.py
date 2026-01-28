class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        copy_head = head.next
        while cur:
            copy = cur.next
            cur.next = copy.next
            copy.next = copy.next.next if copy.next else None
            cur = cur.next

        return copy_head
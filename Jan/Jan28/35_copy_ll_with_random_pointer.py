class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return
        
        # 1 - Weave
        curr = head
        while curr:
            copy = Node(curr.value)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 2 - Set random pointer
        curr = head
        while curr:
            copy = curr.next
            copy.next = curr.random.next if curr.random else None
            curr = copy.next

        # 3 - Unweave separate copy
        curr = head
        copy_head = curr.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return copy_head
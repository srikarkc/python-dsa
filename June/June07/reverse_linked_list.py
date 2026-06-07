class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def reverse_linked_list(self, head):
        prev, current = None, head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
    
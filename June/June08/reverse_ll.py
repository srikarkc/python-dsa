class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def reverse_linked_list(self, head):
        current, prev = head, None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
    
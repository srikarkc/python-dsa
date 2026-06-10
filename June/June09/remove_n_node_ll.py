class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def remove_nth_node(self, head, n):
        current, ahead = head, head

        for _ in range(n):
            ahead = ahead.next

        if not ahead.next:  # the nth node from the end is the head self
            return head.next
        
        while ahead.next:
            current, ahead = current.next, ahead.next

        current.next = current.next.next

        return head
    
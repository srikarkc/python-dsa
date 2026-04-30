class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Soln:
    def reverse_linked_list(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
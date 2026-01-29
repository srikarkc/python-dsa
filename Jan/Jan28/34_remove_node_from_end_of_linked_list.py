class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodeFromEndOfLinkedList(self, head, n):
        dummy = ListNode(0, head)

        slow, fast = dummy, dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next
    
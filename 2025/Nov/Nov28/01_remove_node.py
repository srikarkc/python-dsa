class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def removeNthNodeFromEnd(head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
    
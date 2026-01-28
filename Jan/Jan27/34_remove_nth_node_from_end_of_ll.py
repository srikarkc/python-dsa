class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def removeNthNodeFromEnd(self, head, n):
        dummy = Node(0)
        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
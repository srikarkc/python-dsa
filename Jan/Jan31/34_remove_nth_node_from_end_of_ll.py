class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = None

class Solution:
    def removeNthNode(self, head, n):
        dummyNode = ListNode(0, head)

        slow, fast = dummyNode, dummyNode

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummyNode.next
    
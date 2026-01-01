class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def removeNthNodeFromEndOfLinkedList(head, n):
        dummy = Node(0)
        dummy.next = head

        slow, fast = dummy, dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next
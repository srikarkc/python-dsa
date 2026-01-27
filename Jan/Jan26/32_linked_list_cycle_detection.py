class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def __init__(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True     # The cycle has been detected
            
        return False            # No cycle has been detected
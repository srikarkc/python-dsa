class Solution:
    def reorderList(head):
        if not head or not head.next:
            return

        # step 1 - find the left middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2 - reverse the second half
        prev, curr = None, slow.next
        slow.next = None    # separate the second half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # step 3 - merge the 2 halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2
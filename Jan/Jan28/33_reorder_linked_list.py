class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # 1 - Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2 - severe the second half
        second = slow.next
        slow.next = None

        # 2 - reverse the second half
        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3 - Merge the two halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
            
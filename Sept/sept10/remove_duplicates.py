class Node:
    def __init__(self, value):
        self.value = self.value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Other methods have been omitted

    # Remove duplicates the O(n^2) way
    def remove_duplicates(self):
        slow, fast = self.head, self.head

        while slow is not None:
            slow = fast

            while fast.next is not None:
                if fast.next.value == slow.value:
                    fast.next = fast.next.next
                    self.length -= 1
                else:
                    fast = fast.next
            
            slow = slow.next

    # Remove duplicates the O(n) way
    def remove_dupes(self):
        values = set()
        prev = None
        current = self.head

        while current:
            if current.value in values:
                prev.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                prev = current
            current = current.next
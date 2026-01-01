class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head, self.tail = new_node, new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # Some methods omitted

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        
        sorted_head = self.head
        sorted_head.next = None
        current = self.head.next

        while current:
            next_node = current.next

            if current.value < sorted_head.value:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while (search.next is not None and search.next.value < current.value):
                    search = search.next
                current.next = search.next
                search.next = current
            current = current.next

        self.head = sorted_head
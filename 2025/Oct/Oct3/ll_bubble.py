class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True
    
    def bubble_sort(self):
        if self.length < 2:
            return

        # Outer Loop: repeat until no swaps        
        for _ in range(self.length):
            swapped = False
            temp = self.head

            # Inner Loop: compare adjacent nodes
            while temp is not None and temp.next is not None:
                if temp.value > temp.next.value:
                    temp.value, temp.next.value = temp.next.value, temp.value
                    swapped = True
                temp = temp.next

            if not swapped:
                break
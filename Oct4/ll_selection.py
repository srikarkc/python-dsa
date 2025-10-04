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
    
    # Some other methods omitted

    def selection_sort(self):

        temp = self.head

        # temp is not None is so that we don't go out of range
        # temp.next is not None is so that we stop early since last node does not need sorting
        while temp is not None and temp.next is not None:
            min = temp
            ahead = temp.next

            # we need to go all the way to the last node
            while ahead is not None:
                if ahead.value < min.value:
                    min = ahead
                ahead = ahead.next

            if min != temp:
                min.value, temp.value = temp.value, min.value

            temp = temp.next
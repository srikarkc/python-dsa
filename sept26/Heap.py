class Heap:
    def __init__(self):
        self.heap = []

    # Here we are starting to store values from 0-index
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # To insert a value - we will first append to the end of the list
        self.heap.append(value)
        
        # Then we bubble up the value to the appropriate position
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self._parent(current):
            # Swap function takes indices
            self._swap(current, self._parent(current))
            current = self._parent(current)

    # Most of the complexity for the remove method exists here
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self, value):
        # We will remove the highest value node and then replace with the bottom value and sink it
        # We need to code for empty heap and for 1 item in the heap

        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]

        # Remove the last element and move to the top
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value


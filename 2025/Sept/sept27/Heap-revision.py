# Heaps by KC. Revision on Saturday, Sept 27, 2025

# The follwing represents a max heap
class Heap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return index * 2 + 1
    
    def _right_child(self, index):
        return index * 2 + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # Append the value to the end
        self.heap.append(value)

        current = len(self.heap) - 1

        # Bubble up to the right spot
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    # Remove will always remove the top node with the highest/lowest value
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        # Sink down the value to the appropriate position
        self._sink(0)

        return max_value
    
    def _sink(self, index):
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
            

# Problem 1 - Find the kth smallest number in the index
def find_kth_smallest(nums, k):
    max_heap = Heap()

    for num in nums:
        max_heap.insert(num)

    # Find the number of numbers to remove
    neg_k = len(nums) - k

    for i in range(neg_k):
        max_heap.remove()

    return max_heap.remove()


# The solution from Udemy
def find_kth_smallest(nums, k):
    max_heap = Heap()
 
    for num in nums:
        max_heap.insert(num)
        if len(max_heap.heap) > k:
            max_heap.remove()
 
    return max_heap.remove()



# Problem 2 - Return the max number in a continuous stream
def stream_max(nums):
    max_heap = Heap()

    output_list = []

    for num in nums:
        max_heap.append(num)
        output_list.append(max_heap.heap[0])

    return output_list
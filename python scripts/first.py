'''code to Implement a Python class MaxHeap that supports the following operations: insert, 
delete, and get_max. Ensure the operations maintain the properties of a max-heap.
'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()  
        self._heapify_down(0)
        
        return max_val

    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(30)
max_heap.insert(20)

print(max_heap.get_max())  
print(max_heap.delete())   
print(max_heap.get_max())  

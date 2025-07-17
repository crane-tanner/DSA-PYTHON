import random

class MaxBinaryHeap:
    def __init__(self):
        self.items = []

    def insert(self, data): # Time & Space Complexity: O(log n) and O(1)
        self.items.append(data)
        self.move_up()
        return self

    def move_up(self):
        child_idx = len(self.items) - 1
        while child_idx > 0:
            parent_idx = (child_idx -1) // 2
            if self.items[child_idx] <= self.items[parent_idx]:
                break
            self.swap(child_idx, parent_idx)
            child_idx = parent_idx

    def swap(self, idx_1, idx_2):
        self.items[idx_1], self.items[idx_2] = self.items[idx_2], self.items[idx_1]


    def remove_max(self): # Time & Space Complexity: O(log n) and O(1)
        if not self.items:
            raise Exception("Heap is empty")
        max_elem = self.items[0]
        end_idx = len(self.items) - 1
        self.swap(0, end_idx)
        self.items.pop()
        self.move_down()
        return max_elem

    def move_down(self):
        parent_idx = 0
        child_idx = (2 * parent_idx) + 1
        end_idx = len(self.items) - 1
        while child_idx <= end_idx:
            if child_idx < end_idx and self.items[child_idx] < self.items[child_idx + 1]:
               child_idx += 1
            if self.items[parent_idx] < self.items[child_idx]:
                self.swap(parent_idx, child_idx)
                parent_idx = child_idx
                child_idx = 2 * parent_idx + 1
            else:
                break


new_list = []
for _ in range(0, 10):
    new_list.append(random.randint(0,100))
print("List before heapify:", new_list)

# heap = MaxBinaryHeap()
# for _ in range(0,10):
#     heap.insert(random.randint(0, 100))
# print(heap.items)
# heap.remove_max()
# print(heap.items)


# Floyd's Algorithm
def heapify(array): # Time and Space Complexity: O(n) and O(1)
    last_parent_idx = len(array) // 2 - 1
    for idx in range(last_parent_idx, -1, -1):
        move_down(array, idx, len(array) -1)
    return array

def move_down(array, start_idx, end_idx):
    child_idx = (2 * start_idx) + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx], array[start_idx]
            start_idx = child_idx
            child_idx = (2 * start_idx) + 1
        else:
            break


print("After heapify:", heapify(new_list))

#
# Heap (max heap)
#
#
#

import random 

class Heap:
    def __init__(self, data):
        self.heap_arr = []
        self.heap_arr.append(None)
        self.heap_arr.append(data)

    def bubble_up(self, insert_id):
        if insert_id <= 1:
            return False

        parent_id = insert_id // 2
        if self.heap_arr[insert_id] > self.heap_arr[parent_id]:
            return True
        else:
            return False
        
    def insert(self, data):
        self.heap_arr.append(data)

        insert_id = len(self.heap_arr) - 1

        while self.bubble_up(insert_id):
            parent_id = insert_id // 2
            self.heap_arr[insert_id], self.heap_arr[parent_id] = self.heap_arr[parent_id], self.heap_arr[insert_id]
            insert_id = parent_id

        return True

    def bubble_down(self, popped_id):
        left_child_id = popped_id * 2
        right_child_id = (popped_id * 2) + 1

        # left child does not exist
        if left_child_id >= len(self.heap_arr):
            return False
        
        # right child does not exist
        elif right_child_id >= len(self.heap_arr):
            if self.heap_arr[popped_id] < self.heap_arr[left_child_id]:
                return True
            else:
                return False
        
        # left, right child do exist
        else:
            if self.heap_arr[left_child_id] > self.heap_arr[right_child_id]:
                if self.heap_arr[popped_id] < self.heap_arr[left_child_id]:
                    return True
                else:
                    return False
            else:
                if self.heap_arr[popped_id] < self.heap_arr[right_child_id]:
                    return True
                else:
                    return False

    def pop(self):
        returned_data = self.heap_arr[1]
        self.heap_arr[1] = self.heap_arr[-1] #root를 삭제 후 마지막 데이터를 삽입, 후 정렬
        del self.heap_arr[-1]
        popped_id = 1

        while self.bubble_down(popped_id):            
            left_child_id = popped_id * 2
            right_child_id = (popped_id * 2) + 1

            # right child does not exist
            if right_child_id >= len(self.heap_arr):
                if self.heap_arr[popped_id] < self.heap_arr[left_child_id]:
                    self.heap_arr[popped_id], self.heap_arr[left_child_id] = self.heap_arr[left_child_id], self.heap_arr[popped_id]
                    popped_id = left_child_id
            # left, right child do exist
            else:
                if self.heap_arr[left_child_id] > self.heap_arr[right_child_id]:
                    if self.heap_arr[popped_id] < self.heap_arr[left_child_id]:
                        self.heap_arr[popped_id], self.heap_arr[left_child_id] = self.heap_arr[left_child_id], self.heap_arr[popped_id]
                        popped_id = left_child_id
                else:
                    if self.heap_arr[popped_id] < self.heap_arr[right_child_id]:
                        self.heap_arr[popped_id], self.heap_arr[right_child_id] = self.heap_arr[right_child_id], self.heap_arr[popped_id]
                        popped_id = right_child_id
            
        return returned_data

if __name__ == "__main__":
    heap = Heap(20)    
    print(heap.heap_arr)

    i = 1
    while i < 10: 
        heap.insert(random.randint(0, 99))
        print(heap.heap_arr)
        i += 1
    
    print(heap.pop())
    print(heap.heap_arr)
    
    

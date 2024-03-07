#problem: https://replit.com/@ZhangMYihua/priority-queue-class-implementation#index.js
from typing import List, Dict

#-------------------------------------------------------------------------
class PriorityQueue:
    #-------------------------------------------------------------------------
    def __notes():
        pass
        #in order to find the children of a node at index i, we can use the following formulas:
        #left_child_index = 2 * i + 1
        #right_child_index = 2 * i + 2
    
        #in order to find the parent of a node at index i, we can use the following formula:
        #parent_index = (i - 1) // 2
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def int_max_comparator( a , b ) -> bool:
        return a > b
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def __init__(self, fnc_comparator = int_max_comparator) -> None:
        self.__heap = []
        self.comparator = fnc_comparator
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def size(self) -> int:
        return len(self.__heap)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def peek(self):
        return self.__heap[0]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def is_empty(self) -> bool:
        return len(self.__heap) == 0
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def push(self, value) -> None:
        self.__heap.append(value)
        self.__sift_up()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop(self):
        if self.is_empty(): return None
        if len(self.__heap) <= 2: return self.__heap.pop(0)

        ret_val = self.__heap[0]
        self.__sift_down()

        return ret_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __sift_down(self) -> None:
        #left_child_index = 2 * i + 1
        #right_child_index = 2 * i + 2        
        self.__heap[0] = self.__heap.pop()

        current_index : int = 0
        #----------------
        while current_index < len(self.__heap):
            left_idx : int = self.__get_left_child_idx(current_index)
            right_idx : int = self.__get_right_child_idx(current_index)

            if left_idx and right_idx: #you have both left and right children - check which is bigger
                if self.comparator(self.__heap[left_idx], self.__heap[right_idx]) and self.comparator(self.__heap[left_idx], self.__heap[current_index]):
                    self.__heap[current_index], self.__heap[left_idx] = self.__heap[left_idx], self.__heap[current_index]
                    current_index = left_idx
                elif self.comparator(self.__heap[right_idx], self.__heap[current_index]):
                    self.__heap[current_index], self.__heap[right_idx] = self.__heap[right_idx], self.__heap[current_index]
                    current_index = right_idx
                else:
                    break #left and right are not bigger than current
            elif left_idx: #only left exists - check if left is bigger
                if self.comparator(self.__heap[left_idx], self.__heap[current_index]):
                    self.__heap[current_index], self.__heap[left_idx] = self.__heap[left_idx], self.__heap[current_index]
                    current_index = left_idx
                else: #left is not bigger, break
                    break
            elif right_idx:
                if self.comparator(self.__heap[right_idx], self.__heap[current_index]):
                    self.__heap[current_index], self.__heap[right_idx] = self.__heap[right_idx], self.__heap[current_index]
                    current_index = right_idx
                else: #right is not bigger, break
                    break
            else: #no children - break
                break
        #----------------
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __get_left_child_idx(self, current_idx: int) -> int:
        idx : int =  2 * current_idx + 1
        if idx < len(self.__heap): return idx
        return None
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __get_right_child_idx(self, current_idx: int) -> int:
        idx : int =  2 * current_idx + 2
        if idx < len(self.__heap): return idx
        return None
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __get_parent_idx(self, current_idx: int) -> int:
        return (current_idx - 1) // 2
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __sift_up(self) -> None:
        #parent_index = (i - 1) // 2
        current_index = len(self.__heap) - 1
        parent_index = self.__get_parent_idx(current_index)

        while current_index > 0 and parent_index >= 0 and self.comparator(self.__heap[current_index], self.__heap[parent_index]):
            self.__heap[current_index], self.__heap[parent_index] = self.__heap[parent_index], self.__heap[current_index]
            current_index = parent_index
            parent_index = self.__get_parent_idx(current_index)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

x = PriorityQueue()

x.push(3)
x.push(9)
x.push(5)
x.push(6)
x.push(2)
x.push(7)
x.push(1)
x.push(8)
x.push(4)
print('hi')
while x.is_empty() == False:
    result = x.pop()
    print(result)
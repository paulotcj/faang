#problem: https://replit.com/@ZhangMYihua/priority-queue-class-implementation#index.js
from typing import Callable
# #-------------------------------------------------------------------------
# def int_max_comparator( bigger_int : int , smaller_int : int) -> bool:
#     return bigger_int > smaller_int
# #-------------------------------------------------------------------------    
#-------------------------------------------------------------------------
class PriorityQueue : 
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
    def __init__( self) -> None :
        self.__heap : list[int] = []
        # self.comparator : Callable[[int,int], bool] = fnc_comparator
        self.h : list[int] = self.__heap
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def peek(self) -> int|None :
        if self.__heap: return self.__heap[0]
        else : return None
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def size(self) -> int :
        return len(self.__heap)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def is_empty(self) -> bool :
        return len(self.__heap) == 0 
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __get_parent(self, current_idx : int) -> int :
        parent : int = (current_idx - 1) // 2
        return parent
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __get_left_child_idx(self, current_idx : int) -> int :
        left_child_idx : int = (current_idx * 2) + 1
        if left_child_idx < len(self.__heap) : return left_child_idx # ok, within range
        else : return None
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __get_right_child_idx(self, current_idx : int) -> int :
        right_child_idx : int = (current_idx * 2) + 2
        if right_child_idx < len(self.__heap) : return right_child_idx # ok , within range
        else : return None
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def __sift_up(self) -> None : 
        curr_idx : int = len(self.__heap) - 1
        parent_idx : int = self.__get_parent(current_idx=curr_idx)

        #----------------------------------------
        # while current_idx is bigger than the root node (i.e.: 0), and the parent_idx is
        #  bigger or equal to the root node (0), and the child is bigger than the parent
        while curr_idx > 0 and parent_idx >= 0 and \
         self.__heap[curr_idx] > self.__heap[parent_idx] :
            #switch positions
            self.__heap[curr_idx] , self.__heap[parent_idx] = self.__heap[parent_idx] , self.__heap[curr_idx]

            #update the indexes
            curr_idx = parent_idx
            parent_idx : int = self.__get_parent(current_idx=curr_idx)
        #----------------------------------------
    #------------------------------------------------------------------------- 
    #-------------------------------------------------------------------------
    def __sift_down(self) -> None :
        self.__heap[0] = self.__heap.pop() # last item now is root
        curr_idx : int = 0
        # now we have to descend and find this item's place. remember if this priority
        #  queue is not empty, this item is smaller than the items below it

        #----------------------------------------
        while curr_idx < len(self.__heap) :
            left_idx    : int = self.__get_left_child_idx(current_idx=curr_idx)
            right_idx   : int = self.__get_right_child_idx(current_idx=curr_idx)

            if left_idx is not None and right_idx is not None : # you have both left and right children, check which one is bigger
                #-----
                # if left is bigger than right, and left is bigger than current, then swap
                if self.__heap[left_idx] > self.__heap[right_idx] and \
                  self.__heap[left_idx] > self.__heap[curr_idx] :
                    self.__heap[curr_idx] , self.__heap[left_idx] = self.__heap[left_idx] , self.__heap[curr_idx]
                    curr_idx = left_idx
                    continue
                #-----
                if self.__heap[right_idx] > self.__heap[curr_idx]: # right is bigger than curr
                    self.__heap[right_idx] , self.__heap[curr_idx] = self.__heap[curr_idx] , self.__heap[right_idx]
                    curr_idx = right_idx
                #-----
                else: # no one is bigger
                    break
                #-----
            elif left_idx is not None: # only left exists
                #-----
                if self.__heap[left_idx] > self.__heap[curr_idx] : 
                    self.__heap[left_idx] , self.__heap[curr_idx] = self.__heap[curr_idx] , self.__heap[left_idx]
                    curr_idx = left_idx
                #-----
                else:
                    break
                #-----
            elif right_idx is not None: # only right exists
                #-----
                if self.__heap[right_idx] > self.__heap[curr_idx] :
                    self.__heap[curr_idx] , self.__heap[right_idx] = self.__heap[right_idx] , self.__heap[curr_idx]
                    curr_idx = right_idx
                #-----
                else:
                    break
                #-----
            else: # no child - break
                break
        #---------------------------------------- 
    #-------------------------------------------------------------------------
    def push(self, input : int) -> None :
        self.__heap.append(input)
        self.__sift_up()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop(self) -> int :
        if self.is_empty() : return None
        if len(self.__heap) <= 2 : return self.__heap.pop(0) # most basic scenario, only root or root and 1 child

        ret_val : int = self.__heap[0]
        self.__sift_down()

        return ret_val
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
print('------------------')
while x.is_empty() == False:
    result = x.pop()
    print(result)
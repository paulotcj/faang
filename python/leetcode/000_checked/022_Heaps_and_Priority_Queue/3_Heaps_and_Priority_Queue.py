#problem: https://replit.com/@ZhangMYihua/priority-queue-class-implementation#index.js

#-------------------------------------------------------------------------
class PriorityQueue :
    #-------------------------------------------------------------------------
    def __init__(self) -> None:
        self._heap: list[int] = []
        self.h = self._heap
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def peek(self) -> int|None:
        return self.h[0] if self.h else None
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def size(self) -> int:
        return len(self.h)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def is_empty(self) -> bool:
        return not self.h
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _get_parent_idx(self, idx: int) -> int:
        return (idx - 1) // 2
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _left_child_idx(self, idx: int) -> int:
        return (idx * 2)  + 1
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _right_child_idx(self, idx: int) -> int:
        return (idx * 2) + 2
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def _sift_up(self) -> None:
        # you pushed a value to the end of the queue and now you must find its correct spot, so you bubble
        #  it up until the spot is right.        
        curr_idx : int = len(self.h) - 1

        #----------------------------------------
        while curr_idx > 0: # while curr_idx is not the root node, let's check if this position is right
            parent : int = self._get_parent_idx( idx = curr_idx )
            #-----
            if self.h[curr_idx] > self.h[parent]: # need to swap places
                self.h[curr_idx], self.h[parent] = self.h[parent], self.h[curr_idx]
                curr_idx = parent
            #-----
            else: # no need to swap, then the value it's in the right place - done
                break
            #-----
        #----------------------------------------
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _sift_down(self) -> None:
        # you have a value at the top of the queue. It's possible this value is not the biggest
        #  value from the priority queue, so you need to push it down until you find the right
        #  place for it        
        curr_idx : int = 0

        #----------------------------------------
        while True:
            left_idx    : int = self._left_child_idx(idx = curr_idx)
            right_idx   : int = self._right_child_idx(idx = curr_idx)
            largest_idx : int = curr_idx


            if left_idx < len(self.h) and self.h[left_idx] > self.h[largest_idx]:
                largest_idx = left_idx
            if right_idx < len(self.h) and self.h[right_idx] > self.h[largest_idx]:
                largest_idx = right_idx


            # we found a larger value and it's not at the curr_idx, then it needs to be replaced
            if largest_idx != curr_idx:
                self.h[curr_idx], self.h[largest_idx] = self.h[largest_idx], self.h[curr_idx]
                curr_idx = largest_idx
            else: # the largest_idx is the curr_idx
                break
        #----------------------------------------
    #------------------------------------------------------------------------- 
    #-------------------------------------------------------------------------
    def push(self, value: int) -> None:
        self.h.append(value)
        self._sift_up()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop(self) -> int|None:
        if not self.h: return None
        if len(self.h) == 1: return self.h.pop()

        max_val : int = self.h[0]
        self.h[0] = self.h.pop()
        self._sift_down()
        return max_val
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
if __name__ == "__main__":
    pq = PriorityQueue()
    #----------------------------------------
    for num in [3, 9, 5, 6, 2, 7, 1, 8, 4]:
        pq.push(num)
    #----------------------------------------


    print('------------------')
    #----------------------------------------
    while not pq.is_empty():
        print(pq.pop())
    #----------------------------------------
#-------------------------------------------------------------------------
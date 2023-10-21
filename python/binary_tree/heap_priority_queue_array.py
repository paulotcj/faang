#------------------------------------------------------------------
class HeapArray:
    #------------------------------------------------------------------
    def __init__(self) -> None:
        self.heap = []
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_parent_idx(self,idx):
        if self.is_idx_in_range(idx) is False: 
            return None
        parent_idx = (idx-1)//2
        if self.is_idx_in_range(parent_idx) is False: 
            return None
        return parent_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_parent(self,idx):
        parent_idx = self.get_parent_idx(idx)
        if parent_idx is None: return None
        else: return self.heap[parent_idx]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_right_idx(self,idx):
        if self.is_idx_in_range(idx) is False: return None
        right_idx = 2*idx + 2
        if self.is_idx_in_range(right_idx) is False: return None
        return right_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_right(self,idx):
        right_idx = self.get_right_idx(idx)
        if right_idx is None: return None
        else: return self.heap[right_idx]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_left_idx(self,idx):
        if self.is_idx_in_range(idx) is False: return None
        left_idx = 2*idx + 1
        if self.is_idx_in_range(left_idx) is False: return None
        return left_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_left(self,idx):
        left_idx = self.get_left_idx(idx)
        if left_idx is None: return None
        else: return self.heap[left_idx]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def is_idx_in_range(self,idx):
        if idx is None or idx < 0 or idx >= len(self.heap): 
            return False
        else: 
            return True
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def insert(self,value):
        self.heap.append(value)
        idx = len(self.heap)-1
        self.sift_up(idx)
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def update(self,old_value, new_value):
        #look up for the 'old_value' and if found replace with the new value

        if old_value in self.heap:
            idx = self.heap.index(old_value)
            self.update_using_idx(idx,new_value)
    #------------------------------------------------------------------    
#------------------------------------------------------------------
#------------------------------------------------------------------
class MinHeapArray(HeapArray):
    #------------------------------------------------------------------
    def __init__(self) -> None:
        super().__init__()
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def sift_up(self,idx):
        # swapping a node with its parent
        i = idx #preserving the original index
        parent_idx = self.get_parent_idx(idx)
        #----
        if idx is None or parent_idx is None: return
        #----
        while self.is_idx_in_range(i) and self.heap[i] < self.heap[parent_idx]:
            temp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[i]
            self.heap[i] = temp
            #----
            #now we jump the the parent index and compare from there
            i = parent_idx
            parent_idx = self.get_parent_idx(i)

            if i is None or parent_idx is None: 
                break
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def sift_down(self,idx):
        #  exchanging the value with the smaller of its two children.
        
        left_idx = self.get_left_idx(idx)
        right_idx = self.get_right_idx(idx)
        smallest_v_idx = None

        #----------------------
        #while  left  index is valid and left_value  is less than current OR
        #       right index is valid and right value is less than current
        while (left_idx  and self.heap[idx] > self.heap[left_idx ]    ) or \
              (right_idx and self.heap[idx] > self.heap[right_idx]    ): 
            #---        
            #find the smallest value index
            if right_idx is None or self.heap[left_idx] < self.heap[right_idx]: #right is invalid therefore use left OR left is less than right
                smallest_v_idx = left_idx
            else:
                smallest_v_idx = right_idx
            #---
            #swap values
            temp = self.heap[idx]
            self.heap[idx] = self.heap[smallest_v_idx]
            self.heap[smallest_v_idx] = temp
            #---
            idx = smallest_v_idx #idx now points to the index which was holding the smallest value
            #---
            left_idx = self.get_left_idx(idx)
            right_idx = self.get_right_idx(idx)
        #end of while loop
        #----------------------
    #------------------------------------------------------------------        
    #------------------------------------------------------------------
    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def extract_min(self):
        #the algorithm's general idea is to take the root node at index 0 
        # and replace it with the last node in the heap

        if self.heap is None or len(self.heap) == 0: 
            return None #house keeping
        
        min_v = self.heap[0] #get the min value
        #---
        self.heap[0] = self.heap[-1] #replace it
        self.heap.pop() #remove the last node
        #---
        self.sift_down(0) #now adjust the heap
        #-------
        return min_v
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def update_using_idx(self,idx,new_value):
        if self.is_idx_in_range(idx) is False: return
        
        old_value = self.heap[idx]
        self.heap[idx] = new_value

        #new < old -> sift up
        #new > old -> sift down
        if new_value < old_value: self.sift_up(idx)
        else: self.sift_down(idx)
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def update(self,old_value, new_value):
        #look up for the 'old_value' and if found replace with the new value

        if old_value in self.heap:
            idx = self.heap.index(old_value)
            self.update_using_idx(idx,new_value)
    #------------------------------------------------------------------      

 #------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
class MaxHeapArray(HeapArray):
    #------------------------------------------------------------------
    def __init__(self) -> None:
        super().__init__()
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def extract_max(self):
        #the algorithm's general idea is to take the root node at index 0 
        # and replace it with the last node in the heap

        if self.heap is None or len(self.heap) == 0: 
            return None #house keeping
        
        max_v = self.heap[0] #get the min value
        #---
        self.heap[0] = self.heap[-1] #replace it
        self.heap.pop() #remove the last node
        #---
        self.sift_down(0) #now adjust the heap
        #-------
        return max_v
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def sift_up(self,idx):
        # swapping a node with its parent
        i = idx #preserving the original index
        parent_idx = self.get_parent_idx(idx)
        #----
        if idx is None or parent_idx is None: return
        #----
        while self.is_idx_in_range(i) and self.heap[i] > self.heap[parent_idx]:
            #swap values
            temp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[i]
            self.heap[i] = temp
            #----
            #now we jump the the parent index and compare from there
            i = parent_idx
            parent_idx = self.get_parent_idx(i)

            if i is None or parent_idx is None: 
                break
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def sift_down(self,idx):
        #  exchanging the value with the smaller of its two children.
        
        left_idx = self.get_left_idx(idx)
        right_idx = self.get_right_idx(idx)
        biggest_v_idx = None

        #----------------------
        #while  left  index is valid and left_value  is less than current OR
        #       right index is valid and right value is less than current
        while (left_idx  and self.heap[idx] < self.heap[left_idx ]    ) or \
              (right_idx and self.heap[idx] < self.heap[right_idx]    ): 
            #---        
            #find the biggest value index
            if right_idx is None or self.heap[left_idx] > self.heap[right_idx]: #right is invalid therefore use left OR left is bigger than right
                biggest_v_idx = left_idx
            else:
                biggest_v_idx = right_idx
            #---
            #swap values
            temp = self.heap[idx]
            self.heap[idx] = self.heap[biggest_v_idx]
            self.heap[biggest_v_idx] = temp
            #---
            idx = biggest_v_idx #idx now points to the index (of the child) which was holding the biggest value
            #---
            left_idx = self.get_left_idx(idx)
            right_idx = self.get_right_idx(idx)
        #end of while loop
        #----------------------
    #------------------------------------------------------------------ 
    #------------------------------------------------------------------
    def update_using_idx(self,idx,new_value):
        if self.is_idx_in_range(idx) is False: return
        
        old_value = self.heap[idx]
        self.heap[idx] = new_value

        #new > old -> sift up
        #new < old -> sift down
        if new_value > old_value: self.sift_up(idx)
        else: self.sift_down(idx)
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def update(self,old_value, new_value):
        #look up for the 'old_value' and if found replace with the new value

        if old_value in self.heap:
            idx = self.heap.index(old_value)
            self.update_using_idx(idx,new_value)
    #------------------------------------------------------------------      
 




#------------------------------------------------------------------



#------------------------------------------------------------------
class MinHeapArray:
    #------------------------------------------------------------------
    def __init__(self) -> None:
        self.heap = []
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None
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
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def sift_up(self,idx):
        # swapping a node with its parent
        parent_idx = self.get_parent_idx(idx)
        i = idx #preserving the original index
        #----
        while self.is_idx_in_range(i) and self.heap[i] < self.heap[parent_idx]:
            temp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[i]
            self.heap[i] = temp
            #----
            #now we jump the the parent index and compare from there
            i = parent_idx
            parent_idx = self.get_parent_idx(i)

            if i or parent_idx is None: break


    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def sift_down(self,idx):
        #  exchanging the value with the smaller of its two children.
        pass
    #------------------------------------------------------------------
    #------------------------------------------------------------------
#------------------------------------------------------------------


# heap = MinHeapArray()
# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# for i in numbers:
#     heap.insert(i)

# expected_result = [
#     # {'idx':0, 'parent_idx':None},
#     {'idx':1, 'parent_idx':0},
#     {'idx':2, 'parent_idx':0},
#     {'idx':3, 'parent_idx':1},
#     {'idx':4, 'parent_idx':1},
#     {'idx':5, 'parent_idx':2},
#     {'idx':6, 'parent_idx':2},
#     {'idx':7, 'parent_idx':3},
#     {'idx':8, 'parent_idx':3},
#     {'idx':9, 'parent_idx':4},
#     {'idx':10, 'parent_idx':4},
#     {'idx':11, 'parent_idx':5},
#     {'idx':12, 'parent_idx':5},
#     {'idx':13, 'parent_idx':6},
#     {'idx':14, 'parent_idx':6},
# ]
# #act
# test_result = []
# for i in expected_result:
#     idx = i['idx']
#     parent_idx = heap.get_parent_idx(idx)
#     test_result.append( {'idx': idx, 'parent_idx': parent_idx} )
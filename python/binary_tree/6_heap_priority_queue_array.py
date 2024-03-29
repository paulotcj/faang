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
#------------------------------------------------------------------
class PriorityQueueMax:
    #------------------------------------------------------------------
    def __init__(self) -> None:
        self.queue = MaxHeapArray()
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def enqueue(self, value):
        self.queue.insert(value)
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def peek(self):
        return self.queue.get_max()
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def dequeue(self):
        return self.queue.extract_max()
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def is_empty(self):
        return len(self.queue.heap) == 0
    #------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
class PriorityQueueMin:
    #------------------------------------------------------------------
    def __init__(self) -> None:
        self.queue = MinHeapArray()
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def enqueue(self, value):
        self.queue.insert(value)
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def peek(self):
        return self.queue.get_min()
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def dequeue(self):
        return self.queue.extract_min()
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def is_empty(self):
        return len(self.queue.heap) == 0
    #------------------------------------------------------------------
#------------------------------------------------------------------

##################################
##
##  TESTS - START
##
##################################


#------------------------------------------------------------------
class Test_MinHeapArray:
    # generic tests that can be used for any heap - start
    #------------------------------------------------------------------
    def test_get_parent_idx(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0, 'parent_idx':None},
            {'idx':1, 'parent_idx':0},
            {'idx':2, 'parent_idx':0},
            {'idx':3, 'parent_idx':1},
            {'idx':4, 'parent_idx':1},
            {'idx':5, 'parent_idx':2},
            {'idx':6, 'parent_idx':2},
            {'idx':7, 'parent_idx':3},
            {'idx':8, 'parent_idx':3},
            {'idx':9, 'parent_idx':4},
            {'idx':10, 'parent_idx':4},
            {'idx':11, 'parent_idx':5},
            {'idx':12, 'parent_idx':5},
            {'idx':13, 'parent_idx':6},
            {'idx':14, 'parent_idx':6},
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            parent_idx = heap.get_parent_idx(idx)
            test_result.append( {'idx': idx, 'parent_idx': parent_idx} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_parent_idx = expected_result[i]['parent_idx']
            t_idx = test_result[i]['idx']
            t_parent_idx = test_result[i]['parent_idx']

            assert e_idx == t_idx
            assert e_parent_idx == t_parent_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_parent_value(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        expected_result = [
            {'idx':0,  'parent_idx':None , 'value' : (0  + 2), 'parent_value' : None  },
            {'idx':1,  'parent_idx':0    , 'value' : (1  + 2), 'parent_value' : (0+2) },
            {'idx':2,  'parent_idx':0    , 'value' : (2  + 2), 'parent_value' : (0+2) },
            {'idx':3,  'parent_idx':1    , 'value' : (3  + 2), 'parent_value' : (1+2) },
            {'idx':4,  'parent_idx':1    , 'value' : (4  + 2), 'parent_value' : (1+2) },
            {'idx':5,  'parent_idx':2    , 'value' : (5  + 2), 'parent_value' : (2+2) },
            {'idx':6,  'parent_idx':2    , 'value' : (6  + 2), 'parent_value' : (2+2) },
            {'idx':7,  'parent_idx':3    , 'value' : (7  + 2), 'parent_value' : (3+2) },
            {'idx':8,  'parent_idx':3    , 'value' : (8  + 2), 'parent_value' : (3+2) },
            {'idx':9,  'parent_idx':4    , 'value' : (9  + 2), 'parent_value' : (4+2) },
            {'idx':10, 'parent_idx':4    , 'value' : (10 + 2), 'parent_value' : (4+2) },
            {'idx':11, 'parent_idx':5    , 'value' : (11 + 2), 'parent_value' : (5+2) },
            {'idx':12, 'parent_idx':5    , 'value' : (12 + 2), 'parent_value' : (5+2) },
            {'idx':13, 'parent_idx':6    , 'value' : (13 + 2), 'parent_value' : (6+2) },
            {'idx':14, 'parent_idx':6    , 'value' : (14 + 2), 'parent_value' : (6+2) },
        ]
        for i in expected_result:
            value = i['value']
            heap.heap.append(value)

        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            parent_value = heap.get_parent(idx)
            test_result.append( {'idx': idx, 'parent_value' : parent_value} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_parent_value = expected_result[i]['parent_value']

            t_idx = test_result[i]['idx']
            t_parent_value = test_result[i]['parent_value']

            assert e_idx == t_idx
            assert e_parent_value == t_parent_value
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_right_idx(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0, 'right_idx':2},
            {'idx':1, 'right_idx':4},
            {'idx':2, 'right_idx':6},
            {'idx':3, 'right_idx':8},
            {'idx':4, 'right_idx':10},
            {'idx':5, 'right_idx':12},
            {'idx':6, 'right_idx':14},
            {'idx':7, 'right_idx':16},
            {'idx':8, 'right_idx':18},
            {'idx':9, 'right_idx':20},
            {'idx':10, 'right_idx':22},
            {'idx':11, 'right_idx':24},
            {'idx':12, 'right_idx':26},
            {'idx':13, 'right_idx':28},
            {'idx':14, 'right_idx':30},
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            right_idx = heap.get_right_idx(idx)
            test_result.append( {'idx': idx, 'right_idx': right_idx} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_right_idx = expected_result[i]['right_idx']
            t_idx = test_result[i]['idx']
            t_right_idx = test_result[i]['right_idx']

            assert e_idx == t_idx
            assert e_right_idx == t_right_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_right_value(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0,  'right_value':2  },
            {'idx':1,  'right_value':4  },
            {'idx':2,  'right_value':6  },
            {'idx':3,  'right_value':8  },
            {'idx':4,  'right_value':10 },
            {'idx':5,  'right_value':12 },
            {'idx':6,  'right_value':14 },
            {'idx':7,  'right_value':16 },
            {'idx':8,  'right_value':18 },
            {'idx':9,  'right_value':20 },
            {'idx':10, 'right_value':22 },
            {'idx':11, 'right_value':24 },
            {'idx':12, 'right_value':26 },
            {'idx':13, 'right_value':28 },
            {'idx':14, 'right_value':30 },
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            right_idx = heap.get_right(idx)
            test_result.append( {'idx': idx, 'right_value': right_idx} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_right_value = expected_result[i]['right_value']
            t_idx = test_result[i]['idx']
            t_right_value = test_result[i]['right_value']

            assert e_idx == t_idx
            assert e_right_value == t_right_value
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_get_left_idx(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0,  'left_idx':1  },
            {'idx':1,  'left_idx':3  },
            {'idx':2,  'left_idx':5  },
            {'idx':3,  'left_idx':7  },
            {'idx':4,  'left_idx':9  },
            {'idx':5,  'left_idx':11 },
            {'idx':6,  'left_idx':13 },
            {'idx':7,  'left_idx':15 },
            {'idx':8,  'left_idx':17 },
            {'idx':9,  'left_idx':19 },
            {'idx':10, 'left_idx':21 },
            {'idx':11, 'left_idx':23 },
            {'idx':12, 'left_idx':25 },
            {'idx':13, 'left_idx':27 },
            {'idx':14, 'left_idx':29 },
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            left_idx = heap.get_left_idx(idx)
            test_result.append( {'idx': idx, 'left_idx': left_idx} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_left_idx = expected_result[i]['left_idx']
            t_idx = test_result[i]['idx']
            t_left_idx = test_result[i]['left_idx']

            assert e_idx == t_idx
            assert e_left_idx == t_left_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_left_value(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0,  'left_value':1  },
            {'idx':1,  'left_value':3  },
            {'idx':2,  'left_value':5  },
            {'idx':3,  'left_value':7  },
            {'idx':4,  'left_value':9  },
            {'idx':5,  'left_value':11 },
            {'idx':6,  'left_value':13 },
            {'idx':7,  'left_value':15 },
            {'idx':8,  'left_value':17 },
            {'idx':9,  'left_value':19 },
            {'idx':10, 'left_value':21 },
            {'idx':11, 'left_value':23 },
            {'idx':12, 'left_value':25 },
            {'idx':13, 'left_value':27 },
            {'idx':14, 'left_value':29 },
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            left_value = heap.get_left(idx)
            test_result.append( {'idx': idx, 'left_value': left_value} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_left_value = expected_result[i]['left_value']
            t_idx = test_result[i]['idx']
            t_left_value = test_result[i]['left_value']

            assert e_idx == t_idx
            assert e_left_value == t_left_value
    #------------------------------------------------------------------ 
    #------------------------------------------------------------------ 
    def test_is_idx_in_range(self):
        #arrange
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9]
        for i in numbers:
            heap.heap.append(i)

        expected_results = [
            {'idx': 0, 'result': True},
            {'idx': 1, 'result': True},
            {'idx': 2, 'result': True},
            {'idx': 3, 'result': True},
            {'idx': 4, 'result': True},
            {'idx': 5, 'result': True},
            {'idx': 6, 'result': True},
            {'idx': 7, 'result': True},
            {'idx': 8, 'result': True},
            {'idx': 9, 'result': True},

            {'idx': 10, 'result': False},
            {'idx': 11, 'result': False},
            {'idx': -1, 'result': False},
            {'idx': -2, 'result': False},
        ]
        #act
        test_results = []
        for i in expected_results:
            idx = i['idx']
            result = heap.is_idx_in_range(idx)
            test_results.append( {'idx':idx, 'result': result})

        #assert
        for i in range(len(expected_results)):
            e_idx = expected_results[i]['idx']
            e_result = expected_results[i]['result']
            t_idx = test_results[i]['idx']
            t_result = test_results[i]['result']

            assert e_idx == t_idx
            assert e_result == t_result
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_insert_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        # ------
        #arrange
        heap = MinHeapArray()


        expected_results = [   
            {'value': 14, 'result': [14]},
            {'value': 13, 'result': [13, 14]},
            {'value': 12, 'result': [12, 14, 13]},
            {'value': 11, 'result': [11, 12, 13, 14]},
            {'value': 10, 'result': [10, 11, 13, 14, 12]},
            {'value': 9,  'result': [9, 11, 10, 14, 12, 13]},
            {'value': 8,  'result': [8, 11, 9, 14, 12, 13, 10]},
            {'value': 7,  'result': [7, 8, 9, 11, 12, 13, 10, 14]},
            {'value': 6,  'result': [6, 7, 9, 8, 12, 13, 10, 14, 11]},
            {'value': 5,  'result': [5, 6, 9, 8, 7, 13, 10, 14, 11, 12]},
            {'value': 4,  'result': [4, 5, 9, 8, 6, 13, 10, 14, 11, 12, 7]},
            {'value': 3,  'result': [3, 5, 4, 8, 6, 9, 10, 14, 11, 12, 7, 13]},
            {'value': 2,  'result': [2, 5, 3, 8, 6, 4, 10, 14, 11, 12, 7, 13, 9]},
            {'value': 1,  'result': [1, 5, 2, 8, 6, 4, 3, 14, 11, 12, 7, 13, 9, 10]},
            {'value': 0,  'result': [0, 5, 1, 8, 6, 4, 2, 14, 11, 12, 7, 13, 9, 10, 3]},
        ]

        #act
        test_results = []
        for i in expected_results:
            v = i['value']
            heap.insert(v)
            temp = heap.heap.copy()
            test_results.append( {'value': v,'result' : temp } )
            # print(f"{{'value': {i}, 'result': {test_results}}}")

        #assert
        for i in range(len(expected_results)):
            e_value = expected_results[i]['value']
            e_result = expected_results[i]['result']
            t_value = test_results[i]['value']
            t_result = test_results[i]['result']
            assert e_value == t_value
            for j in range(len(e_result)):
                assert e_result[j] == t_result[j]
    #------------------------------------------------------------------  
    #------------------------------------------------------------------
    def test_update_1(self):
        #arrange
        heap = MinHeapArray()

        #         0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
        numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14]
        for i in numbers:
            heap.insert(i)

        expected_results = [
            {'idx': 0,  'value': 0},
            {'idx': 2,  'value': 1},
            {'idx': 5,  'value': 3},
            {'idx': 10, 'value': 11},
            {'idx': 11, 'value': 12},
        ]
        

        # act
        heap.update(old_value = 6, new_value = 0)

        # assert  
        for i in range(len(expected_results)):
            idx = expected_results[i]['idx']
            value = expected_results[i]['value']
            assert heap.heap[idx] == value
    #------------------------------------------------------------------ 
    # generic tests that can be used for any heap - end       
    #####
    #####
    #####
    #####
    #------------------------------------------------------------------
    def test_get_min_1(self):
        #arrange
        heap = MinHeapArray()
        #          0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14
        numbers = [75,13,71,78,56,27,73,77,20,75,9, 76,36,91,23]
        for i in numbers:
            heap.insert(i)
        
        expected_results = 9
        #act
        result = heap.get_min()

        #assert
        assert expected_results == result
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_extract_min(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        # ------
        #arrange
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in numbers:
            heap.insert(i)
            # print(heap.heap)

        # this is an in order array going from min to max, to this is the expected order of extraction
        expected_results = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        test_results = []


        #act
        for i in range(len(heap.heap)):
            value = heap.extract_min()
            test_results.append(value)
            


        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_sift_up_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        # ------
        #               50
        #        51             52
        #    53      54      55      56
        #  57 58   59 60   61 62   63 64   
        #
        #arrange
        heap = MinHeapArray()
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [50,  51, 52,  53,54,55,56,   57,58,59,60,61,62,63,2]
        for i in numbers:
            heap.heap.append(i)

        expected_results = [2, 51, 50, 53, 54, 55, 52, 57, 58, 59, 60, 61, 62, 63, 56]

        #act
        heap.sift_up(14)
        test_results = heap.heap
        # print(test_results)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_sift_up_2(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        # ------
        #               50
        #        51             52
        #    53      54      55      56
        #  57 58   59 60   61 62   63 64   
        #
        #arrange
        heap = MinHeapArray()
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [50,  51, 52,  53,54,55,56,   57,58,2, 60,61,62,63,64]
        for i in numbers:
            heap.heap.append(i)

        #                   0   1   2     3   4   5   6     7   8   9   10  11  12  13  14
        expected_results = [2,  50, 52,   53, 51, 55, 56,   57, 58, 54, 60, 61, 62, 63, 64]

        #act
        heap.sift_up(9)
        test_results = heap.heap
        # print(test_results)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_sift_down_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        # ------
        #               50
        #        51             52
        #    53      54      55      56
        #  57 58   59 60   61 62   63 64   
        #
        #arrange
        heap = MinHeapArray()
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [99,  1,  2,   3, 4, 5, 6,    7, 8, 9, 10,11,12,13,14]
        for i in numbers:
            heap.heap.append(i)

        #                   0   1   2     3   4   5   6     7   8   9   10  11  12  13  14
        expected_results = [1, 3, 2, 7, 4, 5, 6, 99, 8, 9, 10, 11, 12, 13, 14]

        #act
        heap.sift_down(0)
        test_results = heap.heap
        # print(test_results)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_update_by_index_1(self):
        #arrange
        heap = MinHeapArray()

        #         0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
        numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14]
        for i in numbers:
            heap.insert(i)

        expected_results = [
            {'idx': 0,  'value': 0},
            {'idx': 2,  'value': 1},
            {'idx': 5,  'value': 3},
            {'idx': 10, 'value': 11},
            {'idx': 11, 'value': 12},
        ]
        

        # act
        heap.update_using_idx(idx= 5, new_value = 0)

        # assert  
        for i in range(len(expected_results)):
            idx = expected_results[i]['idx']
            value = expected_results[i]['value']
            assert heap.heap[idx] == value
    #------------------------------------------------------------------  
#------------------------------------------------------------------
#------------------------------------------------------------------
class Test_MaxHeapArray:
    #------------------------------------------------------------------
    def test_get_max_1(self):
        #arrange
        heap = MaxHeapArray()
        #          0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14
        numbers = [75,13,71,78,56,27,73,77,20,75,9, 76,36,91,23]
        for i in numbers:
            heap.insert(i)
        
        expected_results = 91
        #act
        result = heap.get_max()

        #assert
        assert expected_results == result
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_extract_max(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        # ------
        #arrange
        heap = MaxHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in numbers:
            heap.insert(i)

        # this is an in order array going from max to min, so this is the expected order of extraction
        expected_results = [14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]


        #act
        test_results = []
        for i in range(len(heap.heap)):
            value = heap.extract_max()
            test_results.append(value)
            
        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------ 
    #------------------------------------------------------------------
    def test_sift_up_1(self):
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13 14

        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        # ------
        #               50
        #        51             52
        #    53      54      55      56
        #  57 58   59 60   61 62   63 64   
        #
        #arrange
        heap = MaxHeapArray()
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [50,  49, 48,  47,46,45,44,   43,42,41,40,39,38,37,99]

        for i in numbers:
            heap.heap.append(i)

        #                   0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        expected_results = [99,  49, 50,  47,46,45,48,   43,42,41,40,39,38,37,44]

        #act
        heap.sift_up(14)
        test_results = heap.heap


        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_sift_up_2(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        # ------


        #arrange
        heap = MaxHeapArray()
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [50,  49, 48,  47,46,45,44,   43,42,41,40,99,38,37,36]

        for i in numbers:
            heap.heap.append(i)

        #                   0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        expected_results = [99,  49, 50,  47,46,48,44,   43,42,41,40,45,38,37,36]

        #act
        heap.sift_up(11)
        test_results = heap.heap

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------   
    #------------------------------------------------------------------
    def test_sift_down_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14

        #arrange
        heap = MaxHeapArray()
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [0,   49, 48,  47,46,45,44,   43,42,41,40,39,38,37,36]
        for i in numbers:
            heap.heap.append(i)

        #                  0    1   2   3  4  5  6     7  8  9  10 11 12 13 14
        expected_results =[49,  47,48,  43,46,45,44,   0, 42,41,40,39,38,37,36]


        #act
        heap.sift_down(0)
        test_results = heap.heap
        print(test_results)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------  
    #------------------------------------------------------------------
    def test_update_by_index_1(self):

        #          0     1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [50,   49, 48,  47,46,39,44,   43,42,41,40,0,38,37,36]


        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14        
        #arrange
        heap = MaxHeapArray()
        #          0     1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [50,   49, 48,  47,46,45,44,   43,42,41,40,39,38,37,36]
        for i in numbers:
            heap.insert(i)

        #                   0     1   2    3  4  5  6     7  8  9  10 11 12 13 14
        expected_results = [50,   49, 48,  47,46,39,44,   43,42,41,40,0, 38,37,36]
    
        # act
        heap.update_using_idx(idx= 5, new_value = 0)
        test_results = heap.heap

        # assert  

        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_update_1(self):

        #          0     1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [50,   49, 48,  47,46,39,44,   43,42,41,40,0,38,37,36]


        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14        
        #arrange
        heap = MaxHeapArray()
        #          0     1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [50,   49, 48,  47,46,45,44,   43,42,41,40,39,38,37,36]
        for i in numbers:
            heap.insert(i)

        #                   0     1   2    3  4  5  6     7  8  9  10 11 12 13 14
        expected_results = [50,   49, 48,  47,46,39,44,   43,42,41,40,0, 38,37,36]
    
        # act
        heap.update(old_value = 45, new_value = 0)
        test_results = heap.heap

        # assert  

        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------           
#------------------------------------------------------------------
#------------------------------------------------------------------
class Test_PriorityQueueMax:
    #------------------------------------------------------------------
    def test_queue_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        pq = PriorityQueueMax()
        numbers = [13, 5, 4, 9, 3, 14, 2, 10, 0, 1, 8, 7, 11, 6, 12]


        #                   0   1  2   3 4 5  6   7 8 9 10 11 12 13 14
        expected_results = [14, 10,13, 9,8,11,12, 5,0,1,3, 4, 7, 2, 6]

        #act
        for i in numbers:
            pq.enqueue(i)

        test_results = pq.queue.heap

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_peek_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        pq = PriorityQueueMax()
        numbers = [13, 5, 4, 9, 3, 14, 2, 10, 0, 1, 8, 7, 11, 6, 12]

        for i in numbers:
            pq.enqueue(i)        


        expected_result = 14

        #act
        test_result = pq.peek()

        #assert
        assert expected_result == test_result
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_is_dequeue_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        pq = PriorityQueueMax()
        numbers = [13, 5, 4, 9, 3, 14, 2, 10, 0, 1, 8, 7, 11, 6, 12]

        for i in numbers:
            pq.enqueue(i)        


        expected_results = [14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

        #act
        test_results = []
        for i in range(len(pq.queue.heap)):
            test_results.append(  pq.dequeue()  )


        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------   
    #------------------------------------------------------------------
    def test_is_empty_1(self):    
        #arrange
        pq = PriorityQueueMax()
        numbers = [13, 5, 4, 9, 3, 14, 2, 10, 0, 1, 8, 7, 11, 6, 12]

        for i in numbers:
            pq.enqueue(i)        


        expected_result_1 = False
        expected_result_2 = True

        #act
        test_result_1 = pq.is_empty()
        for i in range(len(pq.queue.heap)):
            pq.dequeue()
        
        test_result_2 = pq.is_empty()


        #assert
        assert expected_result_1 == test_result_1
        assert expected_result_2 == test_result_2
    #------------------------------------------------------------------       
#------------------------------------------------------------------
#------------------------------------------------------------------
class Test_PriorityQueueMin:
    #------------------------------------------------------------------
    def test_queue_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        pq = PriorityQueueMin()
        numbers = [13, 5, 4, 9, 3, 14, 2, 10, 0, 1, 8, 7, 11, 6, 12]


        #                   0   1  2   3  4  5  6     7   8   9  10 11  12  13 14
        expected_results = [0,  1, 3,  4, 2, 7, 5,    13, 10, 9, 8, 14, 11, 6, 12]

        #act
        for i in numbers:
            pq.enqueue(i)

        test_results = pq.queue.heap
        # print(test_results)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_peek_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        pq = PriorityQueueMin()
        numbers = [13, 5, 4, 9, 3, 14, 2, 10, 0, 1, 8, 7, 11, 6, 12]

        for i in numbers:
            pq.enqueue(i)        


        expected_result = 0

        #act
        test_result = pq.peek()

        #assert
        assert expected_result == test_result
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_dequeue_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        pq = PriorityQueueMin()
        numbers = [13, 5, 4, 9, 3, 14, 2, 10, 0, 1, 8, 7, 11, 6, 12]

        for i in numbers:
            pq.enqueue(i)        


        expected_results = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

        #act
        test_results = []
        for i in range(len(pq.queue.heap)):
            test_results.append(  pq.dequeue()  )


        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------   
    #------------------------------------------------------------------
    def test_is_empty_1(self):    
        #arrange
        pq = PriorityQueueMax()
        numbers = [13, 5, 4, 9, 3, 14, 2, 10, 0, 1, 8, 7, 11, 6, 12]

        for i in numbers:
            pq.enqueue(i)        


        expected_result_1 = False
        expected_result_2 = True

        #act
        test_result_1 = pq.is_empty()
        for i in range(len(pq.queue.heap)):
            pq.dequeue()
        
        test_result_2 = pq.is_empty()


        #assert
        assert expected_result_1 == test_result_1
        assert expected_result_2 == test_result_2
    #------------------------------------------------------------------       
#------------------------------------------------------------------

##################################
##
##  TESTS - END
##
##################################

class Node:
    def __init__(self, value) -> None:
        # self.left = None
        # self.right = None
        self.value = value
        self.parent = None
        self.height = 1


class BinaryTreeArray:
    def __init__(self):
        self.tree = []
        self.count = 0
        self.level = -1
        self.capacity = 0
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def add_capacity(self):
        # print('----------------')
        # print(f'Adding capacity   - current capacity: {self.capacity},\tlevel:{self.level}')
        initial_capacity = self.capacity
        self.level += 1
        self.capacity = 2 ** self.level + self.capacity

        loop_range = self.capacity - initial_capacity
        for _ in range(loop_range):
            self.tree.append(None)

        # print(f'Capacity expanded - current capacity: {self.capacity},\tlevel:{self.level},\tnew slots added:{self.capacity - initial_capacity}')
        # print('----------------')
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def insert(self, value):
        # print(f'adding: {value}')
        if self.count + 1 > self.capacity: self.add_capacity()

        parent_idx = 0
        idx = 0
        while True:
            if idx+1 > self.capacity:
                self.add_capacity()


            if self.tree[idx] == None: # spot found - add node here
                new_node = Node(value)
                new_node.parent = parent_idx
                self.tree[idx] = new_node
                self.count +=1 
                self.update_height_upstream(new_node)
                break

            elif value < self.tree[idx].value: #must go to the left side
                parent_idx = idx
                idx = idx*2 + 1

            else: # by exclusion: must go to the right side
                parent_idx = idx
                idx = idx*2 + 2
                
        
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def lookup(self, value):
        idx = 0
        while True:
            if idx+1 > self.capacity or self.tree[idx] == None:
                print('Item not found')
                return None
            
            elif value == self.tree[idx].value: #exact match
                return self.tree[idx] 
            elif value < self.tree[idx].value: #must go to the left side
                idx = idx*2 + 1
            else: # by exclusion: must go to the right side
                idx = idx*2 + 2

    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def values_to_array(self):
        #i.value if i is not None else None
        return_obj = [ i.value if i is not None else None for i in self.tree]
        return return_obj
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_parent_n(self, node):
        if node == None or node.parent < 0 or node.parent >= len(self.tree) or\
            self.tree[0] == node  : return None
        return self.tree[ node.parent ]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_node_index(self,node):
        if  node == None or \
            node.parent < 0 or \
            node.parent >= len(self.tree):
            return None

        if self.tree[0] == node: return 0

        parent_left_child_idx = node.parent*2 + 1
        parent_right_child_idx = node.parent*2 + 2
        if self.tree[ parent_left_child_idx ] == node: return parent_left_child_idx
        elif self.tree[ parent_right_child_idx ] == node : return parent_right_child_idx
        else:
            print(f'Error: Could not locate node index')
            return None
    #------------------------------------------------------------------
    #------------------------------------------------------------------    
    def get_left_n(self,node):
        node_idx = self.get_node_index(node)
        node_left_idx = node_idx*2 + 1
        if node_left_idx < node_idx or node_left_idx >= len(self.tree): return None
        
        return self.tree[node_left_idx]
    #------------------------------------------------------------------
    def get_right_n(self,node):
        node_idx = self.get_node_index(node)
        node_right_idx = node_idx*2 + 2
        if node_right_idx < node_idx or node_right_idx >= len(self.tree): return None
        
        return self.tree[node_right_idx]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_height(self, node):
        return 0 if not node else node.height
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def update_height_upstream(self, node):

        while node != None:
            left_n = self.get_left_n(node)
            right_n = self.get_right_n(node)
            node.height = max(  self.get_height(left_n) , self.get_height(right_n)  ) + 1
            
            node = self.get_parent_n(node)
    #------------------------------------------------------------------
    #------------------------------------------------------------------    
    def get_balance_factor(self, node):
        if not node:
            return 0
        else:
            node_left = self.get_left_n(node)
            node_right = self.get_right_n(node)
            return ( self.get_height(node_left) - self.get_height(node_right) )
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def right_rotate(self, node):
        # Algorithm explanation
        #
        #
        #        B             A                               A
        #     A    Z   -->   X   B                    -->    X   B
        #   X   Y                  Z  (Y) not linked            Y Z 
        #
        # Preserved Links:  A(left) -> X  ,  B(right)-> Z
        # New Links:        A(right)-> B  ,  B(left) -> Y

        #-------
        # saving the reference variables
        b = node
        a = self.get_left_n(b) if b is not None else None
        y = self.get_right_n(a) if a is not None else None
        #-------
        # if(self.root == b): self.root = a
        ############## ended here ###################

        if a: a.right = b
        if b: b.left = y

        if a: a.parent = b.parent if b is not None else None
        if b: b.parent = a 
        if y: y.parent = b

        if a != None and a.parent != None:
            if a.parent.right == b : a.parent.right = a
            elif a.parent.left == b : a.parent.left = a
            else: print ("Error - Cannot match parent with its child")
    
        if b: b.height = max(  self.get_height(b.left if b else None) , self.get_height(b.right if b else None)  ) + 1
        if a: a.height = max(  self.get_height(a.left if a else None) , self.get_height(a.right if a else None)  ) + 1
        
        self.update_upstream(b)

        return a
    #------------------------------------------------------------------    

#------------------------------------------------------------------------



#------------------------------------------------------------------------

class Test_BinaryTreeArray:
    def test_capacity_1(self):
        #arrange
        tree = BinaryTreeArray()

        #act
        expected_level = 0 #at the end of expansion the level is expected to be 1 level above the actual number
        tree.insert(1)
        measured_level = tree.level
        
        
        expected_capacity = 1 #Level 0 = 2^0 + previous_capacity = 2^0 + 0 = 1
        

        assert expected_capacity == tree.capacity
        assert expected_level == measured_level
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_capacity_7(self):
        #arrange
        tree = BinaryTreeArray()

        #act
        expected_level = 2 #at the end of expansion the level is expected to be 1 level above the actual number
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)        
        expected_capacity = 7 #Level 2 = 2^2 + previous_capacity = 2^2 + 3 = 4 + 3 = 7
        

        assert expected_capacity == tree.capacity
        assert expected_level == tree.level
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_capacity_15(self):
        #arrange
        tree = BinaryTreeArray()

        #act
        expected_level = 3 #at the end of expansion the level is expected to be 1 level above the actual number
        tree.insert(1) #lv0
        tree.insert(2) #lv1
        tree.insert(3) #lv2
        tree.insert(4) #lv3
        expected_capacity = 15 #Level 3 = 2^3 + previous_capacity = 2^3 + 7 = 8 + 7 = 15
        

        assert expected_capacity == tree.capacity
        assert expected_level == tree.level        
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_tree_insert_1_2_3_4_5(self):
        #arrange
        tree = BinaryTreeArray()
        tree.insert(1) 
        tree.insert(2) 
        tree.insert(3) 
        tree.insert(4) 
        tree.insert(5) 
        expected_list = [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5]


        #act
        result_list = tree.values_to_array()      


        #assert
        for i in range(len(result_list)):
            assert expected_list[i] == result_list[i]

        assert 1 == result_list[0]
        assert 2 == result_list[2]
        assert 3 == result_list[6]
        assert 4 == result_list[14]
        assert 5 == result_list[30]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_lookup_1_2_3_4_5_6_7_8_9_10_11_all_must_be_found(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [1,2,3,4,5,6,7,8,9,10,11]
        for i in numbers:
            tree.insert(i)

        lookup_result = []
        for i in numbers:
            temp = tree.lookup(i)
            lookup_result.append( temp.value if temp is not None else None )  

        #act
        for i in range(len(numbers)):
            assert numbers[i] == lookup_result[i]

    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_lookup_none_must_be_found(self):
        #arrange
        tree = BinaryTreeArray()
        numbers_to_insert = [1,2,3,5,6,7,8,9,10,11]
        numbers_not_to_be_found = [-1,0,12,4]
        for i in numbers_to_insert:
            tree.insert(i)

        #act
        lookup_results = []
        for i in numbers_not_to_be_found:
            temp = tree.lookup(i)
            lookup_results.append( temp.value if temp is not None else None )  


        #assert
        for i in range(len(numbers_not_to_be_found)):
            assert lookup_results[i] == None


    #------------------------------------------------------------------
    #------------------------------------------------------------------        
    def test_lookup_9_4_2_9_1_3_6_20_8_7_all_must_be_found(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        for i in numbers:
            tree.insert(i) 

        #act
        lookup_results = []

        for i in numbers:
            temp = tree.lookup(i)
            lookup_results.append( temp.value if temp is not None else None )              

        #assert
        for i in range(len(numbers)):
            assert numbers[i] == lookup_results[i]


    #------------------------------------------------------------------
    #------------------------------------------------------------------    
    def test_find_parents_9_4_2_9_1_3_6_20_8_7(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        for i in numbers:
            tree.insert(i) 

        find_parents_for = [4,  2, 3, 9, 6, 20, 8, 7, 1]
        parents_result   = [90, 4, 2, 4, 9, 9,  6, 8, 2]

        #act
        lookup_results = []
        for i in find_parents_for:
            local_node = tree.lookup(i)
            parent_idx = local_node.parent if local_node is not None else None
            parent = tree.tree[parent_idx] if parent_idx is not None else None
            parent_value = parent.value if parent is not None else None
            lookup_results.append( parent_value )

        #assert
        for i in range(len(parents_result)):
            assert parents_result[i] == lookup_results[i]

    #------------------------------------------------------------------
    #------------------------------------------------------------------    
    def test_find_parents_none_must_be_found(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        for i in numbers:
            tree.insert(i) 

        find_parents_for = [30,31,32,-1]
        parents_result   = [None, None, None, None]

        #act
        lookup_results = []
        for i in find_parents_for:
            local_node = tree.lookup(i)
            parent_idx = local_node.parent if local_node is not None else None
            parent = tree.tree[parent_idx] if parent_idx is not None else None
            parent_value = parent.value if parent is not None else None
            lookup_results.append( parent_value )

        #assert
        for i in range(len(parents_result)):
            assert parents_result[i] == lookup_results[i]

    #------------------------------------------------------------------    
    #------------------------------------------------------------------             
    def test_find_parents_9_4_2_9_1_3_6_20_8_7_using_get_parent_n(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        for i in numbers:
            tree.insert(i) 

        find_parents_for = [4,  2, 3, 9, 6, 20, 8, 7, 1]
        parents_result   = [90, 4, 2, 4, 9, 9,  6, 8, 2]

        #act
        lookup_results = []
        for i in find_parents_for:
            local_node = tree.lookup(i)
            parent = tree.get_parent_n(local_node)
            parent_value = parent.value if parent is not None else None
            lookup_results.append( parent_value )

        #assert
        for i in range(len(parents_result)):
            assert parents_result[i] == lookup_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------             
    def test_find_parents_using_get_parent_n_noneMustBeFound(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        for i in numbers:
            tree.insert(i) 
        
        find_parents_for = [30,31,32,-1]
        parents_result   = [None, None, None, None]        

        #act
        lookup_results = []
        for i in find_parents_for:
            local_node = tree.lookup(i)
            parent = tree.get_parent_n(local_node)
            parent_value = parent.value if parent is not None else None
            lookup_results.append( parent_value )

        #assert
        for i in range(len(parents_result)):
            assert parents_result[i] == lookup_results[i]
    #------------------------------------------------------------------    
    #------------------------------------------------------------------   
    def test_get_node_index(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        for i in numbers:
            tree.insert(i)         

        #act
        lookup_results = []
        for i in numbers:
            node = tree.lookup(i)
            node_idx = tree.get_node_index(node)
            lookup_results.append(node_idx)


        for i in range(len(numbers)):
            node = tree.tree[ lookup_results[i] ]
            assert node.value == numbers[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_find_left_children(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        for i in numbers:
            tree.insert(i)
            
        find_left_child_of = [90,4, 2, 9, 8, 6]
        expected_result =    [4, 2, 1, 6, 7, None] 
            
        #act
        lookup_results = []
        for i in find_left_child_of:
            node = tree.lookup(i)
            left_node = tree.get_left_n(node)
            left_node_value = left_node.value if left_node else None
            lookup_results.append(left_node_value) 
            
        #assert
        for i in range(len(expected_result)):
            assert expected_result[i] == lookup_results[i]  
           
 
    #------------------------------------------------------------------ 
    #------------------------------------------------------------------   
    def test_find_right_children(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        for i in numbers:
            tree.insert(i)
            
        find_left_child_of = [4, 2, 9,  6, 8]
        expected_result =    [9, 3, 20, 8, None] 
            
        #act
        lookup_results = []
        for i in find_left_child_of:
            node = tree.lookup(i)
            left_node = tree.get_right_n(node)
            left_node_value = left_node.value if left_node else None
            lookup_results.append(left_node_value) 
            
        #assert
        for i in range(len(expected_result)):
            assert expected_result[i] == lookup_results[i]    
    #------------------------------------------------------------------ 
    #------------------------------------------------------------------
    def test_node_height_update(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,20,8,7]
        
        expected_results = [ 
            {'insert': 90, 'check': None, 'height': None},  
            {'insert': None, 'check': 90, 'height': 1},  
            #----
            {'insert': 4, 'check': None, 'height': None},
            {'insert': None, 'check': 90, 'height': 2},
            {'insert': None, 'check': 4, 'height': 1},
            #----
            {'insert': 2, 'check': None, 'height': None},
            {'insert': None, 'check': 90, 'height': 3},
            {'insert': None, 'check': 4, 'height': 2},
            {'insert': None, 'check': 2, 'height': 1},
            #----
            {'insert': 1, 'check': None, 'height': None},
            {'insert': 3, 'check': None, 'height': None},
            {'insert': None, 'check': 90, 'height': 4},
            {'insert': None, 'check': 4, 'height': 3},    
            {'insert': None, 'check': 2, 'height': 2},       
            #----  
            {'insert': 9, 'check': None, 'height': None},
            {'insert': None, 'check': 90, 'height': 4},
            {'insert': None, 'check': 4, 'height': 3},    
            {'insert': None, 'check': 2, 'height': 2},   
            {'insert': None, 'check': 1, 'height': 1},  
            {'insert': None, 'check': 3, 'height': 1},               
            {'insert': None, 'check': 9, 'height': 1},  
            #----  
            {'insert': 6, 'check': None, 'height': None},
            {'insert': None, 'check': 90, 'height': 4},
            {'insert': None, 'check': 4, 'height': 3},    
            {'insert': None, 'check': 2, 'height': 2},   
            {'insert': None, 'check': 1, 'height': 1},  
            {'insert': None, 'check': 3, 'height': 1},               
            {'insert': None, 'check': 9, 'height': 2},
            #----  
            {'insert': 8, 'check': None, 'height': None},
            {'insert': None, 'check': 90, 'height': 5},
            {'insert': None, 'check': 4, 'height': 4},    
            {'insert': None, 'check': 2, 'height': 2},   
            {'insert': None, 'check': 1, 'height': 1},  
            {'insert': None, 'check': 3, 'height': 1},               
            {'insert': None, 'check': 9, 'height': 3},      
            {'insert': None, 'check': 6, 'height': 2},
            {'insert': None, 'check': 8, 'height': 1},
            #----  
            {'insert': 20, 'check': None, 'height': None},
            {'insert': None, 'check': 90, 'height': 5},
            {'insert': None, 'check': 4, 'height': 4},    
            {'insert': None, 'check': 2, 'height': 2},   
            {'insert': None, 'check': 1, 'height': 1},  
            {'insert': None, 'check': 3, 'height': 1},               
            {'insert': None, 'check': 9, 'height': 3},      
            {'insert': None, 'check': 6, 'height': 2},
            {'insert': None, 'check': 8, 'height': 1},
            {'insert': None, 'check': 20, 'height': 1},
            #----  
            {'insert': 7, 'check': None, 'height': None},
            {'insert': None, 'check': 90, 'height': 6},
            {'insert': None, 'check': 4, 'height': 5},    
            {'insert': None, 'check': 2, 'height': 2},   
            {'insert': None, 'check': 1, 'height': 1},  
            {'insert': None, 'check': 3, 'height': 1},               
            {'insert': None, 'check': 9, 'height': 4},      
            {'insert': None, 'check': 6, 'height': 3},
            {'insert': None, 'check': 8, 'height': 2},
            {'insert': None, 'check': 20, 'height': 1},
            {'insert': None, 'check': 7, 'height': 1},
        ]
        
        #act
        test_results = []
        for i in expected_results:
            insert_value = i['insert']
            check_for_this_value = i['check']
            expected_height = i['height']

            if insert_value: tree.insert(insert_value)
            if check_for_this_value:
                loop_node = tree.lookup(check_for_this_value)
                if loop_node: test_results.append({ 'node_height': loop_node.height, 'expected_height' : expected_height })
        
        
        #assert
        for i in test_results:
            node_height = i['node_height']
            expected_height = i['expected_height']
            assert node_height == expected_height
    
    #------------------------------------------------------------------
    def test_balance_factor_90_4_2_9_1_3_6_20_8_7(self):
        #arrange
        tree = BinaryTreeArray()
        numbers =          [90, 4, 2, 9, 1, 3,  6, 20, 8, 7]  
        expected_results = [5, -2, 0, 2, 0, 0, -2, 0,  1, 0] 
        for i in numbers:
            tree.insert(i)
        
        #act
        test_results = []
        for i in numbers:
            node = tree.lookup(i)
            balance = tree.get_balance_factor(node)
            test_results.append(balance)
            
        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]


    #------------------------------------------------------------------
    
#------------------------------------------------------------------     


tree = BinaryTreeArray()
numbers = [90,4,2,9,1,3,6,20,8,7]
for i in numbers:
    tree.insert(i)
    
for i in numbers:
    node = tree.lookup(i)
    balance = tree.get_balance_factor(node)
    print(f'node:{ node.value },\tbalance:{balance}')
        
        

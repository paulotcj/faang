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
                new_obj = Node(value)
                new_obj.parent = parent_idx
                self.tree[idx] = new_obj
                self.count +=1 
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
        if node == None or node.parent < 0 or node.parent >= len(self.tree) : return None
        return self.tree[ node.parent ]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_node_index(self,node):
        if node == None or node.parent < 0 or node.parent >= len(self.tree) : return None
        if node.parent == None or node.parent == 0 : return 0

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
    def update_height_upstream(self, node):

        while node != None:
            left_n = self.get_left_n(node)
            right_n = self.get_right_n(node)
            node.height = max(  self.get_height(left_n) , self.get_height(right_n)  ) + 1
            
            node = self.get_parent_n(node)



        
                

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




        
        

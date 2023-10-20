class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.height = 1


class BinaryTreeArray:
    def __init__(self):
        self.tree = []
        self.count = 0
        self.level = 0

    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def add_capacity(self):
        self.add_capacity_to_subtree(self.tree)
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def add_capacity_to_subtree(self, subtree):
        from math import log2

        if subtree == None: return

        initial_capacity = len(subtree)
        level = int(log2(initial_capacity+1))
        self.level = level

        target_capacity = int(2 ** level + len(subtree))

        loop_range = target_capacity - initial_capacity
        for _ in range(loop_range):
            subtree.append(None)
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def insert(self, value):
        # print(f'adding: {value}')
        if self.count + 1 > len(self.tree): self.add_capacity()

        parent_idx = 0
        idx = 0
        while True:
            if idx+1 > len(self.tree):
                self.add_capacity()


            if self.tree[idx] == None: # spot found - add node here
                new_node = Node(value)
                new_node.parent = parent_idx
                self.tree[idx] = new_node
                self.count +=1 
                self.update_height_upstream(new_node)
                return new_node
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
            if idx+1 > len(self.tree) or self.tree[idx] == None:
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
    def values_to_array_from_array(self, array):
        #i.value if i is not None else None
        return_obj = [ i.value if i is not None else None for i in array]
        return return_obj    
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_parent_n(self, node):
        if node == None or node.parent == None or node.parent < 0 or node.parent >= len(self.tree) or\
            self.tree[0] == node  : return None
        return self.tree[ node.parent ]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_node_index(self,node):
        
        #-------
        #base cases
        if  node == None: return None
        if self.tree[0] == node: return 0
        #-------

        #Fail-safe
        if  node.parent < 0 or \
            node.parent >= len(self.tree):
            return None        

        parent_left_child_idx = node.parent*2 + 1
        parent_right_child_idx = node.parent*2 + 2
        if self.tree[ parent_left_child_idx ] == node: return parent_left_child_idx
        elif self.tree[ parent_right_child_idx ] == node : return parent_right_child_idx
        else:
            print(f'Error: Could not locate node index')
            return None
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_left_idx(self,node):
        if node == None: return None

        node_idx = self.get_node_index(node)
        node_left_idx = node_idx*2 + 1
        if node_left_idx < node_idx or node_left_idx >= len(self.tree): return None
        return node_left_idx        
    #------------------------------------------------------------------
    #------------------------------------------------------------------   
    def get_left_n(self,node):
        node_left_idx = self.get_left_idx(node)
        if node_left_idx == None: return None
        return self.tree[node_left_idx]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_right_idx(self,node):
        if node == None: return None

        node_idx = self.get_node_index(node)
        node_right_idx = node_idx*2 + 2
        if node_right_idx < node_idx or node_right_idx >= len(self.tree): return None
        return node_right_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------    
    def get_right_n(self,node):
        node_right_idx = self.get_right_idx(node)
        if node_right_idx == None: return None
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
    def clear_subtree(self, subtree, subtree_idx):
        num_elements = 1
        num_to_skip = None
        #---
        current_list_len = len(subtree)
        return_list = []
        #---
        target_idx = subtree_idx
        upper_limit = target_idx + num_elements
        while target_idx < current_list_len: #we do not take the full range as it might be a problem if the tree is not full
            if target_idx >= upper_limit:
                num_elements *= 2
                #---
                if num_to_skip == None: 
                    num_to_skip = subtree_idx
                else: 
                    num_to_skip *= 2
                #---
                target_idx += num_to_skip
                upper_limit = target_idx + num_elements
                continue
            #---
            subtree[target_idx] = None
            target_idx += 1
            
        #---
        return return_list 
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_subtree(self, node_idx):
        if node_idx == None or node_idx < 0 or node_idx >= len(self.tree): return None

        num_elements = 1
        num_to_skip = None
        #---
        current_list_len = len(self.tree)
        return_list = []
        #---
        target_idx = node_idx
        upper_limit = target_idx + num_elements
        while target_idx < current_list_len: #we do not take the full range as it might be a problem if the tree is not full
            if target_idx >= upper_limit:
                num_elements *= 2
                #---
                if num_to_skip == None: 
                    num_to_skip = node_idx
                else: 
                    num_to_skip *= 2
                #---
                target_idx += num_to_skip
                upper_limit = target_idx + num_elements
                continue
            #---
            return_list.append( self.tree[target_idx] )
            target_idx += 1
            
        #---
        return return_list 
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def get_parent_idx(self,idx):
        # Given the binary tree below represented by their components indexes, 
        # give me the formula to find the parent index of any node
        #                              0,
        #               1,                           2,
        #       3,             4,             5,             6,
        #    7,     8,     9,     10,      11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        if idx == 0 : return None

        parent_index = (idx - 1) // 2  

        return parent_index
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def insert_subtree(self, from_subtree, to_subtree, to_subtree_idx):
        if from_subtree == None or \
            to_subtree == None or \
            not from_subtree or \
            to_subtree_idx >= len(to_subtree): 
                return

        self.clear_subtree(to_subtree,to_subtree_idx)
        #---
        num_elements = 1
        num_to_skip = None
        #---
        current_list_len = len(to_subtree)
        #---
        target_idx = to_subtree_idx
        upper_limit = target_idx + num_elements
        for i in from_subtree:
            # while target_idx < current_list_len:
                


            #---
            if target_idx >= upper_limit:
                num_elements *= 2
                #---
                if num_to_skip == None: 
                    num_to_skip = to_subtree_idx
                else: 
                    num_to_skip *= 2
                #---
                target_idx += num_to_skip
                upper_limit = target_idx + num_elements
                # continue
            #---
            if target_idx >= (current_list_len-1):
                while target_idx >= (current_list_len-1):
                    self.add_capacity_to_subtree(to_subtree)
                    current_list_len = len(to_subtree)
            #---
            # if target_idx == 15:
            #     print('here')            

            if i :  i.parent = self.get_parent_idx(target_idx)

            to_subtree[target_idx] = i
            target_idx += 1
    #------------------------------------------------------------------   
    #------------------------------------------------------------------
    def __all_empty(self,subtree,from_idx, to_idx):
        

        if from_idx < 0 or from_idx >= len(subtree): return
        if to_idx < 0 or to_idx >= len(subtree): return

        for i in range(from_idx, to_idx+1):
            if subtree[i] != None:
                return False

        return True
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def __is_level_empty(self,subtree,level):
        from_idx = 2**(level-1) - 1
        to_idx = (2**level - 1) - 1

        return self.__all_empty(subtree,from_idx,to_idx)
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def __clean_tree_level(self,tree,level):
        from_idx = (2**(level-1) - 1) - 1 #the loop needs to be adjusted by - 1
        to_idx =   (2**level - 1) - 1 #the loop needs to be adjusted by - 1

        for i in range(to_idx,from_idx , -1):
            tree.pop(i)
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def trim_tree(self,tree):
        from math import log2

        level = int(log2(len(tree)+1))
        list_capacity = len(tree)

        #---
        expected_capacity = (2**level - 1)
        if list_capacity != expected_capacity: 
            print(f'Error: List capacity is {list_capacity}, and expected capacity is {expected_capacity}')
            return
        #---

        while self.__is_level_empty(tree,level):
            self.__clean_tree_level(tree,level)
            level -= 1
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def right_rotate(self, idx):
        # Algorithm explanation
        #
        #        B             A                               A
        #     A    Z   -->   X   B                    -->    X   B
        #   X   Y                  Z  (Y) not linked            Y Z 
        #
        # Nodes: A, B
        # Substree: X, Y, Z
        #-------------------------------------------------------------------
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30             
        #--------------------------------------------------------------------
        # |0| 1|2| 3|4| 5|6|...   -> |0| 1|2| 3|4| 5|6|...
        # |B| A|Z| X|Y| -|-|...   -> |A| X|B| -|-| Y|Z|...
        #
        #
        
        b_idx = idx
        b = self.tree[b_idx]        
        a = self.get_left_n(b)

        if a == None: return

        subtree_z = self.get_subtree( self.get_right_idx(b)  )

        subtree_x = self.get_subtree( self.get_left_idx(a)   )
        subtree_y = self.get_subtree( self.get_right_idx(a)  )
        #--------------

        #              | 0  | 1  | 2  | 3  | 4  | 5  | 6  |
        temp_subtree = [None,None,None,None,None,None,None]

        #0
        temp_subtree[0] = a
        #1
        self.insert_subtree(from_subtree = subtree_x, to_subtree = temp_subtree, to_subtree_idx=1)
        #2
        temp_subtree[2] = b
        #3 - No action
        #4 - No action
        #5
        self.insert_subtree(from_subtree = subtree_y, to_subtree = temp_subtree, to_subtree_idx=5)
        #6
        self.insert_subtree(from_subtree = subtree_z, to_subtree = temp_subtree, to_subtree_idx=6)

        #----
        self.insert_subtree(from_subtree = temp_subtree, to_subtree = self.tree, to_subtree_idx=idx)
        self.update_height_upstream(b)
        self.trim_tree(self.tree)
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def left_rotate(self, idx):
        # Algorithm explanation
        #
        #      A                B                              B
        #    X   B    --->    A   Z                  --->    A   Z
        # 	    Y Z          X       (Y) not linked         X Y    
        #
        # Nodes: A, B
        # Substree: X, Y, Z
        #-------------------------------------------------------------------
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30             
        #--------------------------------------------------------------------
        # |0| 1|2| 3|4| 5|6|...   -> |0| 1|2| 3|4| 5|6|...
        # |A| X|B|  | | Y|Z|...   -> |B| A|Z| X|Y|  | |...
        #

        a_idx = idx
        a = self.tree[a_idx]
        b = self.get_right_n(a)
	
        if b == None: return
       
        subtree_x = self.get_subtree( self.get_left_idx(a)  )
        subtree_y = self.get_subtree( self.get_left_idx(b)  )
        subtree_z = self.get_subtree( self.get_right_idx(b) )

        #--------------

        #              | 0  | 1  | 2  | 3  | 4  | 5  | 6  |
        temp_subtree = [None,None,None,None,None,None,None]  
        #---
        #0
        temp_subtree[0] = b
        #1
        temp_subtree[1] = a
        #2
        self.insert_subtree(from_subtree = subtree_z, to_subtree = temp_subtree, to_subtree_idx=2)
        #3
        self.insert_subtree(from_subtree = subtree_x, to_subtree = temp_subtree, to_subtree_idx=3)
        #4
        self.insert_subtree(from_subtree = subtree_y, to_subtree = temp_subtree, to_subtree_idx=4)
        #5 - No action
        #6 - No action


        #----
        self.insert_subtree(from_subtree = temp_subtree, to_subtree = self.tree, to_subtree_idx=idx)
        self.update_height_upstream(a)
        self.trim_tree(self.tree)
    #------------------------------------------------------------------
    def check_node_unbalanced(self, node):
        if node == None: return None

        balance = self.get_balance_factor(node)
        if balance >= 2: #LEFT SIDE too heavy
            return -1 #left side
        elif balance <= -2: #RIGHT SIDE too heavy
            return 1 #right side
        else: #balanced
            return 0
    #------------------------------------------------------------------
    def insert_avl(self,value):
        new_node = self.insert(value)
        self.balance_avl(new_node)
    #------------------------------------------------------------------        
    #------------------------------------------------------------------
    def balance_avl(self, node):
        temp = node

        # print(self.values_to_array())


        while temp:
            # print(f"processing: {temp.value}")

            check_for_heavy_side = self.check_node_unbalanced(temp)

            if check_for_heavy_side == -1: #LEFT SIDE too heavy
                # print('LEFT SIDE too heavy')
                # This could be:
                #      A             A
                #    B      OR     B
                #  C                C
                
                a = temp
                a_idx = self.get_node_index(a)
                b = self.get_left_n(a)
                b_idx = self.get_node_index(b)
                c_right = self.get_right_n(b)
                c_left = self.get_left_n(b)

                if c_right != None and c_left == None:
                    self.left_rotate(b_idx)
                
                self.right_rotate(a_idx)

                # print('----')
                # debug_tree = self.get_subtree(a_idx)
                # array_debug = self.values_to_array_from_array(debug_tree)
                # print(f'    {array_debug}')
                # print('----')

                # print(self.values_to_array())

                continue

                
            elif check_for_heavy_side == 1: #RIGHT SIDE too heavy
                # print('RIGHT SIDE too heavy')

                # This could be:
                #  A             A
                #    B      OR     B
                #      C          C

                a = temp
                a_idx = self.get_node_index(a)
                b = self.get_right_n(a)
                b_idx = self.get_node_index(b)
                c_right = self.get_right_n(b)
                c_left = self.get_left_n(b)


                if c_left != None and c_right == None:
                    self.right_rotate(b_idx)


                self.left_rotate(a_idx)

                # print('----')
                # debug_tree = self.get_subtree(a_idx)
                # array_debug = self.values_to_array_from_array(debug_tree)
                # print(f'    {array_debug}')
                # print('----')

                # print(self.values_to_array())

                continue



            # else: #balanced
            #     print('BALANCED')

            if temp.parent != None and temp.parent >= 0 and temp.parent < len(self.tree) and \
            self.tree[0] != temp: 
                temp = self.tree[temp.parent]
            else:
                temp = None

        # end of while loop
        #----------------------------
    #------------------------------------------------------------------
#------------------------------------------------------------------------



#------------------------------------------------------------------------
class Test_BinaryTreeArray:
    #------------------------------------------------------------------
    def test_capacity_1(self):
        #arrange
        tree = BinaryTreeArray()

        #act
        expected_level = 0 #at the end of expansion the level is expected to be 1 level above the actual number
        tree.insert(1)
        measured_level = tree.level
        
        
        expected_capacity = 1 #Level 0 = 2^0 + previous_capacity = 2^0 + 0 = 1
        

        assert expected_capacity == len(tree.tree)
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
        

        assert expected_capacity == len(tree.tree)
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
        

        assert expected_capacity == len(tree.tree)
        assert expected_level == tree.level        
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_add_capacity_subtree_1(self):
        #arrange
        tree = BinaryTreeArray()
        subtree = []
        expected_results = [1,3,7,15,31,63,127,255,511,1023,2047]
        test_results = []

        #act
        for i in range(len(expected_results)):
            tree.add_capacity_to_subtree(subtree)
            test_results.append(len(subtree))

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
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
    def test_get_subtree_34(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [                   46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 
        
        expected_results = [34, 32, 39, 31, 33, 37, 41]

        for i in numbers:
            tree.insert(i)  

        #act
        node_idx = tree.get_node_index(tree.lookup(34))
        subtree = tree.get_subtree(node_idx)
        test_results = tree.values_to_array_from_array(subtree)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_subtree_28(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [                   46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 
        
        expected_results = [28, 14, 34, 8, 21, 32, 39, 6, 9, 17, 25, 31, 33, 37, 41]

        for i in numbers:
            tree.insert(i)  

        #act
        node_idx = tree.get_node_index(tree.lookup(28))
        subtree = tree.get_subtree(node_idx)
        test_results = tree.values_to_array_from_array(subtree)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------  
    #------------------------------------------------------------------
    def test_get_subtree_74(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [                   46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 
        
        expected_results = [74, 56, 91, 52, 62, 87, 94, 48, 53, 60, 70, 85, 89, 93, 99]

        for i in numbers:
            tree.insert(i)  

        #act
        node_idx = tree.get_node_index(tree.lookup(74))
        subtree = tree.get_subtree(node_idx)
        test_results = tree.values_to_array_from_array(subtree)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_subtree_56(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [                   46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 
        
        expected_results = [56, 52, 62, 48, 53, 60, 70]

        for i in numbers:
            tree.insert(i)  

        #act
        node_idx = tree.get_node_index(tree.lookup(56))
        subtree = tree.get_subtree(node_idx)
        test_results = tree.values_to_array_from_array(subtree)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_subtree_91(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [                   46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 
        
        expected_results = [91, 87, 94, 85, 89, 93, 99]

        for i in numbers:
            tree.insert(i)  

        #act
        node_idx = tree.get_node_index(tree.lookup(91))
        subtree = tree.get_subtree(node_idx)
        test_results = tree.values_to_array_from_array(subtree)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_subtree_14(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [                   46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 
        
        expected_results = [14, 8, 21, 6, 9, 17, 25]

        for i in numbers:
            tree.insert(i)  

        #act
        node_idx = tree.get_node_index(tree.lookup(14))
        subtree = tree.get_subtree(node_idx)
        test_results = tree.values_to_array_from_array(subtree)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------     
    #------------------------------------------------------------------
    def test_get_subtree_46(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [                   46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 
        
        expected_results = [              46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 

        for i in numbers:
            tree.insert(i)  

        #act
        node_idx = tree.get_node_index(tree.lookup(46))
        subtree = tree.get_subtree(node_idx)
        test_results = tree.values_to_array_from_array(subtree)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_parent_index(self):
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        tree = BinaryTreeArray()
        numbers = [                       46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 

        for i in numbers:
            tree.insert(i)  

        expected_results = [{'idx': 0, 'parent_idx': None},
            
                            {'idx': 1, 'parent_idx': 0},
                            {'idx': 2, 'parent_idx': 0},

                            {'idx': 3, 'parent_idx': 1},
                            {'idx': 4, 'parent_idx': 1},

                            {'idx': 5, 'parent_idx': 2},
                            {'idx': 6, 'parent_idx': 2},

                            {'idx': 7, 'parent_idx': 3},
                            {'idx': 8, 'parent_idx': 3},

                            {'idx': 9, 'parent_idx': 4},
                            {'idx': 10, 'parent_idx': 4},

                            {'idx': 11, 'parent_idx': 5},
                            {'idx': 12, 'parent_idx': 5},

                            {'idx': 13, 'parent_idx': 6},
                            {'idx': 14, 'parent_idx': 6},

                            {'idx': 15, 'parent_idx': 7},
                            {'idx': 16, 'parent_idx': 7},

                            {'idx': 17, 'parent_idx': 8},
                            {'idx': 18, 'parent_idx': 8},

                            {'idx': 19, 'parent_idx': 9},
                            {'idx': 20, 'parent_idx': 9},

                            {'idx': 21, 'parent_idx': 10},
                            {'idx': 22, 'parent_idx': 10},
                            
                            {'idx': 23, 'parent_idx': 11},
                            {'idx': 24, 'parent_idx': 11},

                            {'idx': 25, 'parent_idx': 12},
                            {'idx': 26, 'parent_idx': 12},

                            {'idx': 27, 'parent_idx': 13},
                            {'idx': 28, 'parent_idx': 13},

                            {'idx': 29, 'parent_idx': 14},
                            {'idx': 30, 'parent_idx': 14},
                            ]            

        #act
        test_results = []
        for i in expected_results:
            parent_idx = tree.get_parent_idx(i['idx'])
            temp = {'idx': i['idx'], 'parent_idx': parent_idx}
            test_results.append(temp)

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i]['idx'] == test_results[i]['idx']
            assert expected_results[i]['parent_idx'] == test_results[i]['parent_idx']
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_clear_subtree_5(self):
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        tree = BinaryTreeArray()
        numbers = [                       46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 

        for i in numbers:
            tree.insert(i)

        expected_result = [              46,  
                          28,                                74,  
                   14,           34,                None,                 91,  
                 8,   21,     32,    39,       None,    None,         87,    94,
                6,9, 17,25,  31,33, 37,41,   None,None, None,None,  85,89, 93,99]   
        
        #act
        tree.clear_subtree(tree.tree,5)
        test_result = tree.values_to_array()

        #assert
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_clear_subtree_2(self):
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        tree = BinaryTreeArray()
        numbers = [                       46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 

        for i in numbers:
            tree.insert(i)

        expected_result = [              46,  
                          28,                                None,  
                   14,           34,              None,            None,  
                 8,   21,     32,    39,       None,    None,    None,    None,
                6,9, 17,25,  31,33, 37,41,   None,None, None,None,  None,None, None,None] 
        
        #act
        tree.clear_subtree(tree.tree,2)
        test_result = tree.values_to_array()

        #assert
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_clear_subtree_11(self):
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        tree = BinaryTreeArray()
        numbers = [                       46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 

        for i in numbers:
            tree.insert(i)

        expected_result = [              46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       None,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   None,None, 60,70,  85,89, 93,99] 
        
        #act
        tree.clear_subtree(tree.tree,11)
        test_result = tree.values_to_array()

        #assert
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------ 
    #------------------------------------------------------------------ 
    def test_insert_subtree_4(self):
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        tree = BinaryTreeArray()
        numbers = [                       46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 

        for i in numbers:
            tree.insert(i) 

        expected_result = [               46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99]             

        #act
        subtree = tree.get_subtree(4)
        tree.clear_subtree(tree.tree,4)

        tree.insert_subtree(from_subtree = subtree, to_subtree = tree.tree, to_subtree_idx = 4)
        test_result = tree.values_to_array()

        #assert
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]                
    #------------------------------------------------------------------
    #------------------------------------------------------------------ 
    def test_insert_subtree_4_2(self):
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        tree = BinaryTreeArray()
        numbers = [                       46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 

        for i in numbers:
            tree.insert(i) 

        #---
        array_to_be_inserted = [0,  1,2,   3,4,5,6]
        subtree_to_be_inserted = []
        for i in array_to_be_inserted:
            temp = Node(i)
            subtree_to_be_inserted.append(temp)   
        #---       

        expected_result = [               46,  
                          28,                            74,  
                   14,           0,              56,            91,  
                 8,   21,     1,    2,       52,    62,    87,    94,
                6,9, 17,25,  3,4,    5,6,   48,53, 60,70,  85,89, 93,99]   



        #act
        # subtree = tree.get_subtree(4)
        tree.clear_subtree(tree.tree,4)
        
        tree.insert_subtree(from_subtree = subtree_to_be_inserted, to_subtree = tree.tree, to_subtree_idx = 4)
        test_result = tree.values_to_array()

        #assert
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]                
    #------------------------------------------------------------------
    #------------------------------------------------------------------ 
    def test_insert_subtree_4_2_check_parents(self):
        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30          
        #arrange
        tree = BinaryTreeArray()
        numbers = [                       46,  
                          28,                            74,  
                   14,           34,              56,            91,  
                 8,   21,     32,    39,       52,    62,    87,    94,
                6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 

        for i in numbers:
            tree.insert(i) 

        #---
        array_to_be_inserted = [0,  1,2,   3,4,5,6]
        subtree_to_be_inserted = []
        for i in array_to_be_inserted:
            temp = Node(i)
            subtree_to_be_inserted.append(temp)   
        #---       

        # expected_result = [               46,  
        #                   28,                            74,  
        #            14,           0,              56,            91,  
        #          8,   21,     1,    2,       52,    62,    87,    94,
        #         6,9, 17,25,  3,4,    5,6,   48,53, 60,70,  85,89, 93,99]   

        expected_result = [
            {'idx':1, 'parent_idx':0},

            {'idx':4, 'parent_idx':1},
            
            {'idx':9, 'parent_idx':4},
            {'idx':10, 'parent_idx':4},
            
            {'idx':19, 'parent_idx':9},
            {'idx':20, 'parent_idx':9},

            {'idx':21, 'parent_idx':10},
            {'idx':22, 'parent_idx':10},
        ]



        #act
        subtree = tree.get_subtree(4)
        tree.clear_subtree(tree.tree,4)
        
        tree.insert_subtree(from_subtree = subtree_to_be_inserted, to_subtree = tree.tree, to_subtree_idx = 4)


        #assert
        for i in range(len(expected_result)):
            idx = expected_result[i]['idx']
            parent_idx = expected_result[i]['parent_idx']

            assert tree.tree[idx].parent == parent_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_trim_1(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [                     46,  
                          28,                            74,  
                   14,           34,              56,            91,  
        ] 
        for i in numbers:
            tree.insert(i)

        expected_result = [46, 
                           28, 74, 
                           14, 34, 56, 91]

        #act
        tree.add_capacity()
        tree.add_capacity()
        tree.trim_tree(tree.tree)

        #assert
        assert len(tree.tree) == len(expected_result)
        for i in range(len(expected_result)):
            assert tree.tree[i].value == expected_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_right_rotate_simple_1(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [9,4,2]
        for i in numbers:
            tree.insert(i)

        expected_result = [4,2,9]
        #act
        tree.right_rotate(0)

        #assert
        for i in range(len(expected_result)):
            assert tree.tree[i].value == expected_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_right_rotate_simple_2(self):
        #arrange
        tree = BinaryTreeArray()
        #             9
        #       8            *
        #   7      *      *     *
        # 6  *    * *    * *   * *

        numbers = [9,8,7,6]
        for i in numbers:
            tree.insert(i)

        expected_result = [    9,
                            7,    None,
                           6,8, None,None]

        #act
        tree.right_rotate(1)

        #assert
        for i in range(len(expected_result)):
            temp = tree.tree[i].value if tree.tree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_right_rotate_simple_3(self):
        #arrange
        tree = BinaryTreeArray()
        #             9
        #       8            *
        #   7      *      *     *
        # 6  *    * *    * *   * *

        numbers = [9,8,7,6]
        for i in numbers:
            tree.insert(i)

        expected_result = [         8, 
                             7,            9, 
                           6, None,    None, None]

        #act
        tree.right_rotate(0)

        #assert
        for i in range(len(expected_result)):
            temp = tree.tree[i].value if tree.tree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------
    def test_right_rotate_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                                   46,  
                                   28,                            74,  
                            14,           34,              56,            91,  
                          8,   21,     32,    39,       52,    62,    87,    94,
                         6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)

        expected_result = [46, 28, 74, 8, 34, 56, 91, 6, 14, 32, 39, 52, 62, 87, 94, None, None, 9, 21, 31, 33, 37, 41, 48, 53, 60, 70, 85, 89, 93, 99, None, None, None, None, None, None, 17, 25, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        #act
        tree.right_rotate(3)

        #assert
        for i in range(len(expected_result)):
            temp = tree.tree[i].value if tree.tree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_right_rotate_2(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                      46,  
                     28,                              74,  
               14,            34,              56,           91,  
             8,   21,     32,    39,       52,    62,    87,    94,
            6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)
        target_idx = 8
        expected_result = [17, None, 21, None, None, None, 25]


        #act
        tree.right_rotate(target_idx)
        subtree = tree.get_subtree(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = subtree[i].value if subtree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_right_rotate_3(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                      46,  
                     28,                              74,  
               14,            34,              56,           91,  
             8,   21,     32,    39,       52,    62,    87,    94,
            6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)
        target_idx = 17
        expected_result = [17]


        #act
        tree.right_rotate(target_idx)
        subtree = tree.get_subtree(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = subtree[i].value if subtree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_right_rotate_4(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                      46,  
                     28,                              74,  
               14,            34,              56,           91,  
             8,   21,     32,    39,       52,    62,    87,    94,
            6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)
        target_idx = 4
        expected_result = [32, 31, 34, None, None, 33, 39, None, None, None, None, None, None, 37, 41]


        #act
        tree.right_rotate(target_idx)
        subtree = tree.get_subtree(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = subtree[i].value if subtree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------       
    #------------------------------------------------------------------
    def test_right_rotate_5(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                      46,  
                     28,                              74,  
               14,            34,              56,           91,  
             8,   21,     32,    39,       52,    62,    87,    94,
            6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)
        target_idx = 2
        expected_result = [56, 52, 74, 48, 53, 62, 91, None, None, None, None, 60, 70, 87, 94, None, None, None, None, None, None, None, None, None, None, None, None, 85, 89, 93, 99]


        #act
        tree.right_rotate(target_idx)
        subtree = tree.get_subtree(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = subtree[i].value if subtree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------
    def test_left_rotate_simple_1(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [50,60,70]
        for i in numbers:
            tree.insert(i)

        expected_result = [60, 50, 70]
        #act
        tree.left_rotate(0)

        #assert
        for i in range(len(expected_result)):
            assert tree.tree[i].value == expected_result[i]  
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_left_rotate_simple_2(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [50,60,70,80]
        for i in numbers:
            tree.insert(i)

        expected_result = [60, 50, 70, None, None, None, 80]
        #act
        tree.left_rotate(0)

        #assert
        for i in range(len(expected_result)):
            temp = tree.tree[i].value if tree.tree[i] else None
            assert temp == expected_result[i]  
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_left_rotate_simple_3(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [50,60,70,80]
        for i in numbers:
            tree.insert(i)

        expected_result = [50, None, 70, None, None, 60, 80]
        target_idx = 2
        #act
        tree.left_rotate(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = tree.tree[i].value if tree.tree[i] else None
            assert temp == expected_result[i]  
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_left_rotate_1(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                      46,  
                     28,                              74,  
               14,            34,              56,           91,  
             8,   21,     32,    39,       52,    62,    87,    94,
            6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)
        target_idx = 14
        expected_result = [99, 94, None, 93, None, None, None]


        #act
        tree.left_rotate(target_idx)
        subtree = tree.get_subtree(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = subtree[i].value if subtree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------  
    #------------------------------------------------------------------
    def test_left_rotate_2(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                      46,  
                     28,                              74,  
               14,            34,              56,           91,  
             8,   21,     32,    39,       52,    62,    87,    94,
            6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)
        target_idx = 10
        expected_result = [41, 39, None, 37, None, None, None]


        #act
        tree.left_rotate(target_idx)
        subtree = tree.get_subtree(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = subtree[i].value if subtree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------      
    #------------------------------------------------------------------
    def test_left_rotate_3(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                      46,  
                     28,                              74,  
               14,            34,              56,           91,  
             8,   21,     32,    39,       52,    62,    87,    94,
            6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)
        target_idx = 23
        expected_result = [48]


        #act
        tree.left_rotate(target_idx)
        subtree = tree.get_subtree(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = subtree[i].value if subtree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_left_rotate_4(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30                  
        #arrange
        tree = BinaryTreeArray()
        numbers = [                               
                                      46,  
                     28,                              74,  
               14,            34,              56,           91,  
             8,   21,     32,    39,       52,    62,    87,    94,
            6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
        ] 
        for i in numbers:
            tree.insert(i)
        target_idx = 2
        expected_result = [91, 74, 94, 56, 87, 93, 99, 52, 62, 85, 89, None, None, None, None, 48, 53, 60, 70, None, None, None, None, None, None, None, None, None, None, None, None]


        #act
        tree.left_rotate(target_idx)
        subtree = tree.get_subtree(target_idx)

        #assert
        for i in range(len(expected_result)):
            temp = subtree[i].value if subtree[i] else None
            assert temp == expected_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_check_node_unbalanced_using_straight_left(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,80,70,60]
        for i in numbers:
            tree.insert(i)

        expected_result = [ 
            {'idx':7, 'result':0},
            {'idx':3, 'result':0},
            {'idx':1, 'result':-1},
            {'idx':0, 'result':-1},
        ]
        test_result = []

        #act
        for i in expected_result:
            idx = i['idx']
            temp = tree.check_node_unbalanced(tree.tree[idx])
            test_result.append( {'idx':idx, 'result': temp} )

        #assert     
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            t_idx = test_result[i]['idx']
            e_result = expected_result[i]['result']
            t_result = test_result[i]['result']

            assert e_idx == t_idx
            assert e_result == t_result
    #------------------------------------------------------------------         
    #------------------------------------------------------------------
    def test_check_node_unbalanced_using_straight_right(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [60,70,80,90]
        for i in numbers:
            tree.insert(i)

        expected_result = [ 
            {'idx':14, 'result':0},
            {'idx':6, 'result':0},
            {'idx':2, 'result':1},
            {'idx':0, 'result':1},
        ]
        test_result = []

        #act
        for i in expected_result:
            idx = i['idx']
            temp = tree.check_node_unbalanced(tree.tree[idx])
            test_result.append( {'idx':idx, 'result': temp} )

        #assert     
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            t_idx = test_result[i]['idx']
            e_result = expected_result[i]['result']
            t_result = test_result[i]['result']

            assert e_idx == t_idx
            assert e_result == t_result
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_check_node_unbalanced_using_curved_right(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [4,9,6,8]
        for i in numbers:
            tree.insert(i)

        expected_result = [ 
            {'idx':12, 'result':0},
            {'idx':5, 'result':0},
            {'idx':2, 'result':-1},
            {'idx':0, 'result':1},
        ]
        test_result = []

        #act
        for i in expected_result:
            idx = i['idx']
            temp = tree.check_node_unbalanced(tree.tree[idx])
            test_result.append( {'idx':idx, 'result': temp} )

        #assert     
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            t_idx = test_result[i]['idx']
            e_result = expected_result[i]['result']
            t_result = test_result[i]['result']

            assert e_idx == t_idx
            assert e_result == t_result
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_check_node_unbalanced_using_curved_left(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [9,6,8,7]
        for i in numbers:
            tree.insert(i)

        expected_result = [ 
            {'idx':9, 'result':0},
            {'idx':4, 'result':0},
            {'idx':1, 'result':1},
            {'idx':0, 'result':-1},
        ]
        test_result = []

        #act
        for i in expected_result:
            idx = i['idx']
            temp = tree.check_node_unbalanced(tree.tree[idx])
            test_result.append( {'idx':idx, 'result': temp} )

        #assert     
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            t_idx = test_result[i]['idx']
            e_result = expected_result[i]['result']
            t_result = test_result[i]['result']

            assert e_idx == t_idx
            assert e_result == t_result
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_avl_balance_90_80_70(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,80,70]
        for i in numbers:
            tree.insert(i)


        expected_result = [80, 70, 90]

        #act
        last_node = tree.lookup(70)
        tree.balance_avl(last_node)
        test_result = tree.values_to_array()


        #assert     
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_avl_balance_70_80_90(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [70,80,90]
        for i in numbers:
            tree.insert(i)


        expected_result = [80, 70, 90]

        #act
        last_node = tree.lookup(90)
        tree.balance_avl(last_node)
        test_result = tree.values_to_array()


        #assert     
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_avl_balance_90_80_70_60(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,80,70,60]
        for i in numbers:
            tree.insert(i)


        expected_result = [70, 60, 90, None, None, 80, None]

        #act
        last_node = tree.lookup(60)
        tree.balance_avl(last_node)
        test_result = tree.values_to_array()


        #assert     
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_avl_balance_60_70_80_90(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [60,70,80,90]
        for i in numbers:
            tree.insert(i)


        expected_result = [80, 60, 90, None, 70, None, None]

        #act
        last_node = tree.lookup(90)
        tree.balance_avl(last_node)
        test_result = tree.values_to_array()


        #assert     
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------ 
    #------------------------------------------------------------------
    def test_avl_balance_9_6_8_7(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [9,6,8,7]
        for i in numbers:
            tree.insert(i)

        expected_result = [7, 6, 9, None, None, 8, None]

        #act
        last_node = tree.lookup(7)
        tree.balance_avl(last_node)
        test_result = tree.values_to_array()

        #assert     
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------     
    #------------------------------------------------------------------
    def test_avl_balance_4_9_6_8_7(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [4,9,6,8,7]
        for i in numbers:
            tree.insert(i)

        expected_result = [7, 4, 9, None, 6, 8, None]

        #act
        last_node = tree.lookup(7)
        tree.balance_avl(last_node)
        test_result = tree.values_to_array()

        #assert     
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_avl_balance_90_4_2_9_1_3_6_8_7(self):
        #arrange
        tree = BinaryTreeArray()
        numbers = [90,4,2,9,1,3,6,8,7]
        for i in numbers:
            tree.insert(i)

        expected_result = [4, 2, 7, 1, 3, 6, 9, None, None, None, None, None, None, 8, 90]

        #act
        last_node = tree.lookup(7)
        tree.balance_avl(last_node)
        test_result = tree.values_to_array()

        #assert     
        for i in range(len(expected_result)):
            assert expected_result[i] == test_result[i]
    #------------------------------------------------------------------  
    #------------------------------------------------------------------  
    def test_insert_avl_90_4_2_9_1_3_6_8_7(self):
        #arrange
        tree = BinaryTreeArray()
        
        expected_result = [
            {'num':90, 'result':[90]},
            {'num':4,  'result':[90, 4, None]},
            {'num':2,  'result':[4, 2, 90]},
            {'num':9,  'result':[4, 2, 90, None, None, 9, None]},
            {'num':1,  'result':[4, 2, 90, 1, None, 9, None]},
            {'num':3,  'result':[4, 2, 90, 1, 3, 9, None]},
            {'num':6,  'result':[4, 2, 9, 1, 3, 6, 90]},
            {'num':8,  'result':[4, 2, 9, 1, 3, 6, 90, None, None, None, None, None, 8, None, None]},
            {'num':7,  'result':[4, 2, 9, 1, 3, 7, 90, None, None, None, None, 6, 8, None, None]},
        ]
        test_result = []    

        #act
        for i in expected_result:
            num = i['num']
            tree.insert_avl(num)
            result = tree.values_to_array()
            test_result.append( {'num':num,'result':result}  )

        #assert
        for i in range(len(expected_result)):
            e_num = expected_result[i]['num']
            e_result = expected_result[i]['result']
            t_num = test_result[i]['num']
            t_result = test_result[i]['result']

            #numbers must match
            assert e_num == t_num

            #check for each value in each result
            for j in range(len(e_result)):
                assert e_result[j] == t_result[j]
    #------------------------------------------------------------------  

    
#end of Test_BinaryTreeArray
#------------------------------------------------------------------     


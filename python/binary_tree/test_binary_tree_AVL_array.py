from binary_tree_AVL_array import BinaryTreeArray

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
    
#end of Test_BinaryTreeArray
#------------------------------------------------------------------     

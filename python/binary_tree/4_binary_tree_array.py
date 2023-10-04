class BinaryTreeArray:
    def __init__(self):
        self.tree = []
        self.count = 0
        self.level = 0
        self.capacity = 0
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def add_capacity(self):
        print('----------------')
        print(f'Adding capacity   - current capacity: {self.capacity},\tlevel:{self.level}')
        initial_capacity = self.capacity
        self.capacity = 2 ** self.level + self.capacity
        self.level += 1

        loop_range = self.capacity - initial_capacity
        for _ in range(loop_range):
            self.tree.append(None)

        print(f'Capacity expanded - current capacity: {self.capacity},\tlevel:{self.level},\tnew slots added:{self.capacity - initial_capacity}')
        print('----------------')
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def insert(self, value):
        print(f'adding: {value}')
        if self.count + 1 > self.capacity: self.add_capacity()
        
  
        idx = 0
        while True:
            if idx+1 > self.capacity:
                # print('Errosr - Out of bound access attempt')
                self.add_capacity()
                # break

            if self.tree[idx] == None:
                self.tree[idx] = value
                self.count +=1 
                break

            elif value < self.tree[idx]: #must go to the left side
                idx = idx*2 + 1

            else: # by exclusion: must go to the right side
                idx = idx*2 + 2
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def lookup(self, value):
        idx = 0
        while True:
            if idx+1 > self.capacity or self.tree[idx] == None:
                print('Item not found')
                return None
            
            elif value == self.tree[idx]: #exact match
                return self.tree[idx] 
            elif value < self.tree[idx]: #must go to the left side
                idx = idx*2 + 1
            else: # by exclusion: must go to the right side
                idx = idx*2 + 2

        
                

#------------------------------------------------------------------------
# tree = BinaryTreeArray()
# tree.insert(1)

# tree.insert(2)
# tree.insert(3)

# tree.insert(4)

# tree.insert(5)
# print(tree.tree)

# lookup_result = tree.lookup(7)
# print(f'Look up result: {lookup_result}')


# tree = BinaryTreeArray()
# tree.insert(1) 
# tree.insert(2) 
# tree.insert(3) 
# # tree.insert(4)
# tree.insert(5)
# tree.insert(6)
# tree.insert(7)
# tree.insert(8)
# tree.insert(9)
# tree.insert(10)
# tree.insert(11)        


# lookup_result_1 = tree.lookup(-1)
# lookup_result_2 = tree.lookup(0)
# lookup_result_3 = tree.lookup(12)
# lookup_result_4 = tree.lookup(4)




class Test_BinaryTreeArray:
    def test_capacity_1(self):
        #arrange
        tree = BinaryTreeArray()

        #act
        expected_level = 1 #at the end of expansion the level is expected to be 1 level above the actual number
        tree.insert(1)
        measured_level = tree.level
        
        
        expected_capacity = 1 #Level 0 = 2^0 + previous_capacity = 2^0 + 0 = 1
        

        assert expected_capacity == tree.capacity
        assert expected_level == measured_level

    def test_capacity_7(self):
        #arrange
        tree = BinaryTreeArray()

        #act
        expected_level = 3 #at the end of expansion the level is expected to be 1 level above the actual number
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)        
        expected_capacity = 7 #Level 2 = 2^2 + previous_capacity = 2^2 + 3 = 4 + 3 = 7
        

        assert expected_capacity == tree.capacity
        assert expected_level == tree.level

    def test_capacity_15(self):
        #arrange
        tree = BinaryTreeArray()

        #act
        expected_level = 4 #at the end of expansion the level is expected to be 1 level above the actual number
        tree.insert(1) #lv0
        tree.insert(2) #lv1
        tree.insert(3) #lv2
        tree.insert(4) #lv3
        expected_capacity = 15 #Level 3 = 2^3 + previous_capacity = 2^3 + 7 = 8 + 7 = 15
        

        assert expected_capacity == tree.capacity
        assert expected_level == tree.level        


    def test_tree_insert_1_2_3_4_5(self):
        #arrange
        tree = BinaryTreeArray()

        #act
        tree.insert(1) 
        tree.insert(2) 
        tree.insert(3) 
        tree.insert(4) 
        tree.insert(5) 

        expected_list = [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5]

        for i in range(len(tree.tree)):
            assert expected_list[i] == tree.tree[i]

        assert 1 == tree.tree[0]
        assert 2 == tree.tree[2]
        assert 3 == tree.tree[6]
        assert 4 == tree.tree[14]
        assert 5 == tree.tree[30]


    def test_lookup_1_2_3_4_5_6_7_8_9_10_11_all_must_be_found(self):
        #arrange
        tree = BinaryTreeArray()
        tree.insert(1) 
        tree.insert(2) 
        tree.insert(3) 
        tree.insert(4)
        tree.insert(5)
        tree.insert(6)
        tree.insert(7)
        tree.insert(8)
        tree.insert(9)
        tree.insert(10)
        tree.insert(11)        


        #act
        lookup_result_1 = tree.lookup(1)
        lookup_result_2 = tree.lookup(2)
        lookup_result_3 = tree.lookup(3)
        lookup_result_4 = tree.lookup(4)
        lookup_result_5 = tree.lookup(5)
        lookup_result_6 = tree.lookup(6)
        lookup_result_7 = tree.lookup(7)
        lookup_result_8 = tree.lookup(8)
        lookup_result_9 = tree.lookup(9)
        lookup_result_10 = tree.lookup(10)
        lookup_result_11 = tree.lookup(11)


        assert lookup_result_1 == 1
        assert lookup_result_2 == 2
        assert lookup_result_3 == 3
        assert lookup_result_4 == 4
        assert lookup_result_5 == 5
        assert lookup_result_6 == 6
        assert lookup_result_7 == 7
        assert lookup_result_8 == 8
        assert lookup_result_9 == 9
        assert lookup_result_10 == 10
        assert lookup_result_11 == 11

    def test_lookup_none_must_be_found(self):
        #arrange
        tree = BinaryTreeArray()
        tree.insert(1) 
        tree.insert(2) 
        tree.insert(3) 
        # tree.insert(4)
        tree.insert(5)
        tree.insert(6)
        tree.insert(7)
        tree.insert(8)
        tree.insert(9)
        tree.insert(10)
        tree.insert(11)        


        #act
        lookup_result_1 = tree.lookup(-1)
        lookup_result_2 = tree.lookup(0)
        lookup_result_3 = tree.lookup(12)
        lookup_result_4 = tree.lookup(4)



        assert lookup_result_1 == None
        assert lookup_result_2 == None
        assert lookup_result_3 == None
        assert lookup_result_4 == None
        
        


        
        

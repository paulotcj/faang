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
        # self.capacity = 0
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def add_capacity(self):
        from math import log2

        initial_capacity = len(self.tree)
        self.level = int(log2(initial_capacity+1))

        target_capacity = int(2 ** self.level + len(self.tree))

        loop_range = target_capacity - initial_capacity
        for _ in range(loop_range):
            self.tree.append(None)

        # self.capacity = len(self.tree)


    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def add_capacity_to_subtree(self, subtree):
        from math import log2

        if subtree == None: return

        initial_capacity = len(subtree)
        level = int(log2(initial_capacity+1))

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
        if node == None or node.parent < 0 or node.parent >= len(self.tree) or\
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
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def insert_subtree(self, from_subtree, to_subtree, to_subtree_idx):
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
            if target_idx >= current_list_len:
                while current_list_len <= target_idx:
                    self.add_capacity()
                    current_list_len = len(to_subtree)
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

            if i :  i.parent = self.get_parent_idx(target_idx)

            to_subtree[target_idx] = i
            target_idx += 1
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


    #------------------------------------------------------------------
#------------------------------------------------------------------------



# tree = BinaryTreeArray()
# numbers = [50,40,70,30,45,60,90]
# for i in numbers:
#     tree.insert(i)     

# print( tree.values_to_array()  )


# tree = BinaryTreeArray()
# numbers = [40,30,50,45,70,60,90]
# for i in numbers:
#     tree.insert(i)     

# print( tree.values_to_array()  )

#-------------------------------

# tree = BinaryTreeArray()
# numbers = [9,6,8,7]
# for i in numbers:
#     tree.insert(i)     

# print( tree.values_to_array()  )

        #                              0,
        #               1,                           2,
        #       3,             4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30   

# tree = BinaryTreeArray()
# numbers = [                               46,  
#                           28,                            74,  
#                    14,           34,              56,            91,  
#                  8,   21,     32,    39,       52,    62,    87,    94,
#                 6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99] 
# for i in numbers:
#     tree.insert(i)  

# # print(f'parent at zero: parent: {tree.tree[0].value}, {tree.tree[0].parent}')   

# print( tree.values_to_array()  )
# print('---------')

# subtree = tree.get_subtree(5)
# array1 = tree.values_to_array_from_array(subtree)
# print(array1)

# tree.clear_subtree(5)
# print( tree.values_to_array()  )


# tree.insert_subtree(5,subtree)
# print( tree.values_to_array()  )


#-------------------------------

# tree = BinaryTreeArray()
# numbers = [ 90 , 4, 2,]
# for i in numbers:
#     tree.insert(i)

# print(tree.values_to_array())   

# tree.right_rotate(0)

# print(tree.values_to_array())   


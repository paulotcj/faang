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
        self.trim_tree(self.tree)
    #------------------------------------------------------------------
    def check_tree_unbalanced(self, node):
        
        balance = self.get_balance_factor(node)
        if balance >= 2: #LEFT SIDE too heavy
            return -1 #left side
        elif balance <= -2: #RIGHT SIDE too heavy
            return 1 #right side
        else: #balanced
            return 0


    #------------------------------------------------------------------
    def insert_avl(self,value):
        node = self.insert(value)
        if node.parent == None: return node
        self.balance_avl(node)
    #------------------------------------------------------------------        
    #------------------------------------------------------------------
    def balance_avl(self, node):
        temp = node
        temp_parent = self.get_parent_n(temp)

        while temp and temp_parent:

            balance = self.get_balance_factor(temp_parent)

            if balance >= 2: #LEFT SIDE too heavy
                print('LEFT SIDE too heavy')

                # actual logic disabled for testing - start
                # if temp.left:
                #     temp  = self.right_rotate(parent)
                # else:
                #     self.left_rotate(temp)
                #     # self.print()
                #     temp = temp.parent
                #     self.right_rotate(parent)
                #     # self.print()
                # actual logic disabled for testing - end


            elif balance <= -2: #RIGHT SIDE too heavy
                print('RIGHT SIDE too heavy')



                # actual logic disabled for testing - start
                # if temp.right:
                #     self.left_rotate(parent)
                # else:
                #     self.right_rotate(temp)

                #     temp = temp.parent
                #     self.left_rotate(parent)
                # actual logic disabled for testing - end


            temp = self.tree[temp.parent] if temp and temp.parent else None
            temp_parent = self.tree[temp.parent] if temp and temp.parent else None
        # end of while loop
        #----------------------------
    #------------------------------------------------------------------
#------------------------------------------------------------------------







# tree = BinaryTreeArray()

# numbers = [1,2,3,4]
# for i in numbers:
#     tree.insert(i)
# print(tree.values_to_array())
# # [                         1, 
# #            None,                      2, 
# #    None,         None,         None,         3, 
# #  None, None,   None, None,  None, None,   None, 4]

# tree.left_rotate(0)
# print(tree.values_to_array())


# #------------------------------------
#         #                              0,
#         #               1,                           2,
#         #        3,            4,              5,           6,
#         #    7,     8,     9,    10,       11,    12,    13,   14
#         #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30     
# tree = BinaryTreeArray()
# numbers = [                               
#                                  46,  
#                  28,                            74,  
#           14,           34,              56,            91,  
#         8,   21,     32,    39,       52,    62,    87,    94,
#        6,9, 17,25,  31,33, 37,41,   48,53, 60,70,  85,89, 93,99
# ] 
# for i in numbers:
#     tree.insert(i)

# target_idx = 2
# tree.left_rotate(target_idx)
# print(tree.values_to_array())

# subtree = tree.get_subtree(target_idx)
# print(tree.values_to_array_from_array(subtree))




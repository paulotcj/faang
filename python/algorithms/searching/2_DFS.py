#------------------------------------------------------------------
class Node:
    #------------------------------------------------------------------
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
    #------------------------------------------------------------------        
#------------------------------------------------------------------
#------------------------------------------------------------------
class BinaryTree:
    #------------------------------------------------------------------
    def __init__(self) -> None:
        self.root = None
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def insert(self, value):
        new_obj = Node(value)

        if self.root == None:
            self.root = new_obj
            return
        
        #---------------
        current_node = self.root
        while(True):
            if value < current_node.value: #must go to the left side
                if current_node.left == None: # found the right place - insert here
                    current_node.left = new_obj
                    return
                #----
                current_node = current_node.left #continue going to the left side
            else: #right insert
                if current_node.right == None: #found the right place - insert here
                    current_node.right = new_obj
                    return
                #----
                current_node = current_node.right
        #end of while
        #---------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def lookup(self, value):
        current = self.root
        if current == None : return None

        while(current):
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        #end of while
        #---------------
        return None
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def remove(self, value):
        print(f"-------------------------------------------")
        print(f"removing - start\n")
        lookup_result = self.lookup2(value)
        if lookup_result == None or lookup_result['current'] == None: return None
        current = lookup_result['current']
        parent = lookup_result['parent']

        is_current_left_side = True if parent == None or parent.left == current else False
        is_current_right_side = True if parent == None or parent.right == current else False

        # print(f"Removing function - is_current_left_side: {is_current_left_side} - is_current_right_side: {is_current_right_side}")

        if current.left == None and current.right == None: #no child
            print(f"No child detected")
            if parent == None: 
                print(f"This node is the root node. Root is set to None")
                self.root = None
            elif is_current_left_side:
                print(f"removing the left node from parent")
                parent.left = None
            elif is_current_right_side:
                print(f"removing the right node from parent")
                parent.right = None
            else:
                print(f"Error - something went wrong")

        elif current.right != None and current.left != None:
            print(f"current has 2 children")
            successor_dict = self.find_in_order_successor(current)
            succ_curr = successor_dict['current']
            succ_parent = successor_dict['parent']

            #-----  Lets rework the connections
            if succ_parent == current : #successor's parent is equal to the current target (current = the one being removed)
                if is_current_left_side: #parent connection
                    parent.left = succ_curr # (connection #1)
                else:
                    parent.right = succ_curr # (connection #1)

                succ_curr.left = current.left    #target to remove connection 1 (connection #2)
                
            else: #successor's parent is different than the current target (current = the one being removed)
                succ_parent.left = succ_curr.right   #successor connection bypass, 2 connections become 1 (connections #4 and #5)
                
                succ_curr.left = current.left    #target to remove connection 1 (connection #2)
                succ_curr.right = current.right  #target to remove connection 2 (connection #3)
                
                if is_current_left_side: #parent connection
                    parent.left = succ_curr # (connection #1)
                else:
                    parent.right = succ_curr # (connection #1)

            #-----

        else:
            print(f"Current has only one child - connect current's only child to current's parent")
            if parent == None: 
                print(f"Current is the root node.")
                if current.right: self.root = current.right
                else: self.root = current.left
            elif is_current_left_side:
                parent.left = current.left if current.left != None else current.right
                # print(f"Current: {current.value} - left: {current.left.value}")
            else: #right sided
                parent.right = current.left if current.left != None else current.right
                # print(f"Current: {current.value} - left: {current.right.value}")

        #---------
        current.left = None
        current.right = None
        return current
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def print(self):
        print(f"-------------------------------------------")
        node_list = []

        current = self.root
        while(current):
            left_summary = "None"
            right_summary = "None"
            if current.left:
                node_list.append(current.left)
                left_summary = current.left.value
            if current.right:
                node_list.append(current.right)
                right_summary = current.right.value

            print(f"Current value: {current.value}, current.left: {left_summary} , current.right: {right_summary}")

            current =  node_list.pop(0) if node_list else None 
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def DFS_InOrder(self):
        iterative = self.__DFS_in_order_iterative()
        recursive = self.__DFS_in_order_recursive(node = self.root, list = [] )
        if( iterative != recursive): 
            print(f"Error at DFS_InOrder - iterative: {iterative} - recursive: {recursive}")
            return None

        return iterative              
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def __DFS_in_order_iterative(self):
        #       9
        #    4      20
        #  1  6   15  170        
        #In-Order:  1,4,6,9,15,20,170   
        return_list = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            return_list.append(current.value)
            current = current.right

        return return_list
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def __DFS_in_order_recursive(self, node, list):
        if node.left: 
            self.__DFS_in_order_recursive(node.left, list) #go all the way to the left
        list.append(node.value)
        if node.right: 
            self.__DFS_in_order_recursive(node.right, list)
        return list
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def DFS_PreOrder(self):
        iterative =  self.__DFS_pre_order_iterative()
        recursive = self.__DFS_pre_order_recursive(node = self.root, list = [])
        if( iterative != recursive): 
            print(f"Error at DFS_PreOrder - iterative: {iterative} - recursive: {recursive}")
            return None

        return iterative        
    #------------------------------------------------------------------      
    #------------------------------------------------------------------
    def __DFS_pre_order_recursive(self, node, list):
        list.append(node.value)
        if node.left: 
            self.__DFS_pre_order_recursive(node.left, list)
        if node.right: 
            self.__DFS_pre_order_recursive(node.right, list)
        return list
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def __DFS_pre_order_iterative(self):
        #       9
        #    4      20
        #  1  6   15  170        
        #Pre-Order: 9,4,1,6,20,15,170
        stack = [self.root]
        return_list = []
        while stack:
            node = stack.pop()
            if node:
                return_list.append(node.value)
                stack.append(node.right)  # Note: Right child is pushed first
                stack.append(node.left)
        return return_list
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def DFS_PostOrder_Recursive(self):
        initial_list = []
        initial_node = self.root
        return self.__DFS_post_order(node = initial_node, list = initial_list )
    #------------------------------------------------------------------      
    #------------------------------------------------------------------
    def DFS_PostOrder(self):
        iterative = self.__DFS_post_order_iterative()
        recursive = self.__DFS_post_order_recursive(node = self.root, list = [])
        if( iterative != recursive): 
            print(f"Error at DFS_PostOrder - iterative: {iterative} - recursive: {recursive}")
            return None

        return iterative
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def __DFS_post_order_recursive(self, node, list):
        if node.left: 
            self.__DFS_post_order_recursive(node.left, list)
        if node.right: 
            self.__DFS_post_order_recursive(node.right, list)
        list.append(node.value)
        return list
    #------------------------------------------------------------------  
    #------------------------------------------------------------------
    def __DFS_post_order_iterative(self):
        #       9
        #    4      20
        #  1  6   15  170
        #Post-Order: 1,6,4,15,170,20,9          
        stack = [self.root]
        result_stack = []

        while stack:
            node = stack.pop()
            if node:
                result_stack.append(node.value)
                stack.append(node.left)
                stack.append(node.right)

        return_list = result_stack[::-1]
        return return_list

    #------------------------------------------------------------------     

        
#------------------------------------------------------------------

tree = BinaryTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

#       9
#    4      20
#  1  6   15  170

#Pre-Order: 9,4,1,6,20,15,170
#In-Order:  1,4,6,9,15,20,170
#Post-Order: 1,6,4,15,170,20,9

print('--------------------------')
x = tree.DFS_PostOrder()
expected_result = [1,6,4,15,170,20,9]
print(f"Tree DFS Post-Order: {x}")
print(f"Is the result correct? {x == expected_result}")

print('--------------------------')
x = tree.DFS_PreOrder()
expected_result = [9,4,1,6,20,15,170]
print(f"Tree DFS Pre-Order: {x}")
print(f"Is the result correct? {x == expected_result}")

print('--------------------------')
x = tree.DFS_InOrder()
expected_result = [1,4,6,9,15,20,170]
print(f"Tree DFS In-Order: {x}")
print(f"Is the result correct? {x == expected_result}")



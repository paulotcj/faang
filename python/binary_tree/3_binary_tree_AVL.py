class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
        self.parent = None
        self.height = 0

#--------

class BinaryTreeAVL:
    #------------------------------------------------------------------
    def __init__(self) -> None:
        self.root = None
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    # Standard tree insertion. Left = Value is lower than current node, Right = Value is greater than current node
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
                    new_obj.parent = current_node
                    break
                #----
                current_node = current_node.left #continue going to the left side
            else: #right insert
                if current_node.right == None: #found the right place - insert here
                    current_node.right = new_obj
                    new_obj.parent = current_node
                    break
                #----
                current_node = current_node.right
        #end of while


        self.update_upstream(new_obj)


        
        


    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def update_upstream(self,node):

        while node != None:
            node.height = max(  self.get_height(node.left) , self.get_height(node.right)  ) + 1

            # balance = self.get_balance_factor(parent_to_update)
            # print(f'Parent: {parent_to_update.value} -  Balance at insert: {balance}')

            node = node.parent


    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    # Find the node that matches the parameter value
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
    # Find the node that matches the parameter value plus its parent (Note: parent might be None)
    def lookup_with_parent(self, value):
        parent = None
        current = self.root
        if current == None : return None

        while(current):
            if value == current.value:
                return {'current': current, 'parent' : parent}
            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        #end of while
        #---------------
        return None
    #------------------------------------------------------------------   
    #------------------------------------------------------------------
    # Inorder Successor - the node with the 'smallest key' 'greater than' 'the key of the input node'
    def find_in_order_successor(self, param_node):
        if param_node == None or param_node.right == None: return None
        current = param_node.right
        parent = param_node
        while True:
            if current.left != None:
                parent = current
                current = current.left
            else:
                return {'current' : current, 'parent' : parent}

    #------------------------------------------------------------------   
    #------------------------------------------------------------------
    # Remove find the node matching the value and then removes it.
    #  It also handles node's relationships (parent, children)
    def remove(self, value):
        print(f"-------------------------------------------")
        print(f"removing - start\n")
        lookup_result = self.lookup_with_parent(value)
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
    def get_height(self, node):
        return 0 if not node else node.height
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
        a = b.left
        y = a.right
        #-------
        if(self.root == b): self.root = a

        a.right = b
        b.left = y

        a.parent = b.parent
        b.parent = a
        y.parent = b

        if a.parent != None:
            if a.parent.right == b : a.parent.right = a
            elif a.parent.left == b : a.parent.left = a
            else: print ("Error - Cannot match parent with its child")
    

        b.height = max(  self.get_height(b.left) , self.get_height(b.right)  ) + 1
        a.height = max(  self.get_height(a.left) , self.get_height(a.right)  ) + 1
        
        self.update_upstream(b)

        return a
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def left_rotate(self, node):
        # Algorithm explanation
        #
        #      A                B                              B
        #    X   B    --->    A   Z                  --->    A   Z
        # 	    Y Z          X       (Y) not linked         X Y    
        #
        # Preserved Links:  A(left) -> X  ,  B(right)-> Z
        # New Links:        A(right)-> Y  ,  B(left) -> A       
        
        #-------
        # saving the reference variables
        a = node
        b = node.right
        y  = b.left
        #-------
        
        if(self.root == a): self.root = b

        b.left = a
        a.right = y

        b.parent = a.parent
        a.parent = b
        y.parent = a
        
        
        if b.parent != None:
            if b.parent.right == a : b.parent.right = b
            elif b.parent.left == a : b.parent.left = b
            else: print ("Error - Cannot match parent with its child")


        a.height = max(  self.get_height(a.left) , self.get_height(a.right)  ) + 1
        b.height = max(  self.get_height(b.left) , self.get_height(b.right)  ) + 1

        self.update_upstream(a)

        return b
    #------------------------------------------------------------------    
    #------------------------------------------------------------------    
    def get_balance_factor(self, node):
        if not node:
            return 0
        else:
            return ( self.get_height(node.left) - self.get_height(node.right) ) 
    
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def print(self):
        print(f"-------------------------------------------")
        node_list = []

        current = self.root
        while(current):
            left_summary = "None"
            right_summary = "None"
            parent_summary = "None"
            if current.left:
                node_list.append(current.left)
                left_summary = current.left.value
            if current.right:
                node_list.append(current.right)
                right_summary = current.right.value
            if current.parent != None:
                parent_summary = current.parent.value
            balance_factor = self.get_balance_factor(current)

            print(f"curr v: {current.value},\tleft: {left_summary},\tright: {right_summary},\theight: {current.height},\tparent:{parent_summary},\tbalance:{balance_factor}")

            current =  node_list.pop(0) if node_list else None 
    #------------------------------------------------------------------
#------------------------------------------------------------------

#  50
#    75
#      100

# tree = BinaryTreeAVL()
# print('\n\n')
# tree.insert(50)
# tree.print()
# print('\n\n')
# tree.insert(75)
# tree.print()

# print('\n\n')
# tree.insert(60)
# tree.print()

# # print('\n\n')
# # tree.insert(100)
# # tree.print()

# # print('\n\n')
# # tree.print()
# exit()

#       50
#    25     75
#         60  100

# tree = BinaryTreeAVL()

# tree.insert(50)
# tree.insert(25)
# tree.insert(75)
# tree.insert(60)
# tree.insert(100)
# tree.print()

# print(f'-----------\nLeft Rotate')
# target = tree.lookup(50)
# tree.left_rotate(target)
# tree.print()
# print(f'-----------\nRight Rotate')
# target = tree.lookup(75)
# tree.right_rotate(target)
# tree.print()

# exit()


#--------    
#                 90
#            4     
#       2        9
#     1   3        20
#               


tree = BinaryTreeAVL()
tree.insert(90)
tree.insert(4)
tree.insert(2)
tree.insert(9)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(20)
tree.insert(8)
tree.insert(7)
tree.print()
# tree.remove(4)
target = tree.lookup(4)
tree.left_rotate(target)
tree.print()

target = tree.lookup(9)
tree.right_rotate(target)
tree.print()


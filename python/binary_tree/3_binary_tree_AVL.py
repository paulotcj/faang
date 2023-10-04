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
            return new_obj
        
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
        return new_obj

    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def insert_avl(self,value):
        node = self.insert(value)
        if node.parent == None: return node
        self.balance_avl(node)

        
    #------------------------------------------------------------------
    #------------------------------------------------------------------    
    def balance_avl(self, node):
        temp = node

        while temp and temp.parent:
            parent = temp.parent
            balance = self.get_balance_factor(temp.parent)
            # print(f'  Node: {temp.value} - Parent: {temp.parent.value} - Parent Balance: {balance}')

            if balance >= 2: #LEFT SIDE too heavy
                print('LEFT SIDE too heavy')
                # if temp.right != None and temp.left != None:
                #     print(f'Problem while balancing at {parent.value} - Both left and right nodes are occupied')
                # elif temp.left:


                if temp.left:
                    temp  = self.right_rotate(parent)
                else:
                    self.left_rotate(temp)
                    # self.print()
                    temp = temp.parent
                    self.right_rotate(parent)
                    # self.print()


            elif balance <= -2: #RIGHT SIDE too heavy
                print('RIGHT SIDE too heavy')
                # if temp.right != None and temp.left != None:
                #     print(f'Problem while balancing at {parent.value} - Both left and right nodes are occupied')
                #     self.left_rotate(parent)
                # elif temp.right:

                if temp.right:
                    self.left_rotate(parent)
                else:
                    self.right_rotate(temp)
                    # self.print()
                    temp = temp.parent
                    self.left_rotate(parent)
                    # self.print()

            temp = temp.parent

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
        a = b.left if b is not None else None
        y = a.right if a is not None else None
        #-------
        if(self.root == b): self.root = a

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
        b = a.right if a is not None else None
        y = b.left if b is not None else None
        #-------
        
        if(self.root == a): self.root = b

        if b: b.left = a
        if a: a.right = y

        if b: b.parent = a.parent
        if a: a.parent = b
        if y: y.parent = a
        
        
        if b != None and b.parent != None:
            if b.parent.right == a : b.parent.right = b
            elif b.parent.left == a : b.parent.left = b
            else: print ("Error - Cannot match parent with its child")


        if a: a.height = max(  self.get_height(a.left if a else None) , self.get_height(a.right if a else None)  ) + 1
        if b: b.height = max(  self.get_height(b.left if b else None) , self.get_height(b.right if b else None)  ) + 1

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
    def print_generate_strings(self):
        node_list = []
        return_obj = []

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

            # print(f"curr v: {current.value},\tleft: {left_summary},\tright: {right_summary},\theight: {current.height},\tparent:{parent_summary},\tbalance:{balance_factor}")
            add_to_return_list = f"curr v: {current.value},\tleft: {left_summary},\tright: {right_summary},\theight: {current.height},\tparent:{parent_summary},\tbalance:{balance_factor}"
            return_obj.append(add_to_return_list)
            

            current =  node_list.pop(0) if node_list else None 
        #end of while

        return return_obj
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def print(self):
        print(f"-------------------------------------------")
        generated_list = self.print_generate_strings()
        for i in generated_list:
            print(i)
    #------------------------------------------------------------------
#------------------------------------------------------------------


class Test_BinaryTreeAVL:
    #----------------
    # INSERT tests
    def test_insert_rightHeavy_straight(self):
        #  50
        #    75
        #      100

        #arrange
        tree = BinaryTreeAVL()

        assert_values = [
            'curr v: 50,\tleft: None,\tright: 75,\theight: 3,\tparent:None,\tbalance:-2',
            'curr v: 75,\tleft: None,\tright: 100,\theight: 2,\tparent:50,\tbalance:-1',
            'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0'
        ]    

        #act
        tree.insert(50)
        tree.insert(75)
        tree.insert(100)    
        result_list = tree.print_generate_strings()


        #assert
        assert assert_values[0] == result_list[0]
        assert assert_values[1] == result_list[1]
        assert assert_values[2] == result_list[2]

    def test_insert_leftHeavy_straight(self):
        #      50
        #    25
        #  10

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 50,\tleft: 25,\tright: None,\theight: 3,\tparent:None,\tbalance:2', 
                        'curr v: 25,\tleft: 10,\tright: None,\theight: 2,\tparent:50,\tbalance:1', 
                        'curr v: 10,\tleft: None,\tright: None,\theight: 1,\tparent:25,\tbalance:0']   

        #act
        tree.insert(50)
        tree.insert(25)
        tree.insert(10) 
        result_list = tree.print_generate_strings()

        #assert
        assert assert_values[0] == result_list[0]
        assert assert_values[1] == result_list[1]
        assert assert_values[2] == result_list[2]   

    def test_insert_rightHeavy_angled(self):
        #  50
        #    75
        #  60

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 50,\tleft: None,\tright: 75,\theight: 3,\tparent:None,\tbalance:-2', 
                        'curr v: 75,\tleft: 60,\tright: None,\theight: 2,\tparent:50,\tbalance:1', 
                        'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']  

        #act
        tree.insert(50)
        tree.insert(75)
        tree.insert(60) 
        result_list = tree.print_generate_strings()


        #assert
        assert assert_values[0] == result_list[0]
        assert assert_values[1] == result_list[1]
        assert assert_values[2] == result_list[2]

    def test_insert_leftHeavy_angled(self):
        #    50
        #  25
        #    30

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 50,\tleft: 25,\tright: None,\theight: 3,\tparent:None,\tbalance:2', 
                        'curr v: 25,\tleft: None,\tright: 30,\theight: 2,\tparent:50,\tbalance:-1', 
                        'curr v: 30,\tleft: None,\tright: None,\theight: 1,\tparent:25,\tbalance:0'] 

        #act
        tree.insert(50)
        tree.insert(25)
        tree.insert(30)
        result_list = tree.print_generate_strings()


        #assert
        assert assert_values[0] == result_list[0]
        assert assert_values[1] == result_list[1]
        assert assert_values[2] == result_list[2]

    def test_insert_tree_50_25_75_60_100(self):
        #       50
        #    25     75
        #         60  100   

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 50,\tleft: 25,\tright: 75,\theight: 3,\tparent:None,\tbalance:-1', 
                        'curr v: 25,\tleft: None,\tright: None,\theight: 1,\tparent:50,\tbalance:0', 
                        'curr v: 75,\tleft: 60,\tright: 100,\theight: 2,\tparent:50,\tbalance:0', 
                        'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']
        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(60)
        tree.insert(100)

        #act
        result_list = tree.print_generate_strings()


        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]

    #----------------
    #----------------
    # ROTATE TEST
    def test_rotate_left(self):
        #       50
        #    25     75
        #         60  100   

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 75,\tleft: 50,\tright: 100,\theight: 3,\tparent:None,\tbalance:1', 
                        'curr v: 50,\tleft: 25,\tright: 60,\theight: 2,\tparent:75,\tbalance:0', 
                        'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 25,\tleft: None,\tright: None,\theight: 1,\tparent:50,\tbalance:0', 
                        'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:50,\tbalance:0'] 

        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(60)
        tree.insert(100)   

        #act
        target = tree.lookup(50)
        tree.left_rotate(target)
        result_list = tree.print_generate_strings()

        #assert
        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]    

    def test_rotate_right(self):
        #       50
        #    25     75
        #         60  100   

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 25,\tleft: None,\tright: 50,\theight: 4,\tparent:None,\tbalance:-3', 
                        'curr v: 50,\tleft: None,\tright: 75,\theight: 3,\tparent:25,\tbalance:-2', 
                        'curr v: 75,\tleft: 60,\tright: 100,\theight: 2,\tparent:50,\tbalance:0', 
                        'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']

        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(60)
        tree.insert(100) 

        #act
        target = tree.lookup(50)
        tree.right_rotate(target)
        result_list = tree.print_generate_strings()

        #assert
        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]    

    def test_rotate_left_then_rotate_rigth(self):
        #       50                  75                 50
        #    25     75   ->     50      100   ->   25     75
        #         60  100     25  60                    60  100
        # 
        # left followed by a right rotation should reverse all changes
        # and the tree should be back to its original configuration 

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 50,\tleft: 25,\tright: 75,\theight: 3,\tparent:None,\tbalance:-1', 
                        'curr v: 25,\tleft: None,\tright: None,\theight: 1,\tparent:50,\tbalance:0', 
                        'curr v: 75,\tleft: 60,\tright: 100,\theight: 2,\tparent:50,\tbalance:0', 
                        'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']

        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(60)
        tree.insert(100)   

        #act
        #---------
        target = tree.lookup(50) #initial root node
        tree.left_rotate(target)

        target = tree.lookup(75) #new root node after rotating
        tree.right_rotate(target)  
        #---------  

        result_list = tree.print_generate_strings()

        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]      
    #----------------
    #----------------
    # BALANCE AVL tests
    def test_insert_rightHeavy_straight_balance_AVL(self):
        #  50
        #    75
        #      100

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 75,\tleft: 50,\tright: 100,\theight: 2,\tparent:None,\tbalance:0', 
                        'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']

        #act
        tree.insert(50)
        tree.insert(75)
        tree.insert(100)    
        target = tree.lookup(100)
        tree.balance_avl(target)
        result_list = tree.print_generate_strings()


        #assert
        assert assert_values[0] == result_list[0]
        assert assert_values[1] == result_list[1]
        assert assert_values[2] == result_list[2]

    def test_insert_leftHeavy_straight_balance_AVL(self):
        #      50
        #    25
        #  10

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 25,\tleft: 10,\tright: 50,\theight: 2,\tparent:None,\tbalance:0', 
                        'curr v: 10,\tleft: None,\tright: None,\theight: 1,\tparent:25,\tbalance:0', 
                        'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:25,\tbalance:0']  

        #act
        tree.insert(50)
        tree.insert(25)
        tree.insert(10) 
        target = tree.lookup(10)
        tree.balance_avl(target)
        result_list = tree.print_generate_strings()

        #assert
        assert assert_values[0] == result_list[0]
        assert assert_values[1] == result_list[1]
        assert assert_values[2] == result_list[2]   

    def test_insert_rightHeavy_angled_balance_AVL(self):
        #  50
        #    75
        #  60

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 60,\tleft: 50,\tright: 75,\theight: 2,\tparent:None,\tbalance:0', 
                        'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:60,\tbalance:0', 
                        'curr v: 75,\tleft: None,\tright: None,\theight: 1,\tparent:60,\tbalance:0'] 

        #act
        tree.insert(50)
        tree.insert(75)
        tree.insert(60) 
        target = tree.lookup(60)
        tree.balance_avl(target)    
        result_list = tree.print_generate_strings()


        #assert
        assert assert_values[0] == result_list[0]
        assert assert_values[1] == result_list[1]
        assert assert_values[2] == result_list[2]

    def test_insert_leftHeavy_angled_balance_AVL(self):

        #    50
        #  25
        #    30

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 30,\tleft: 25,\tright: 50,\theight: 2,\tparent:None,\tbalance:0', 
                        'curr v: 25,\tleft: None,\tright: None,\theight: 1,\tparent:30,\tbalance:0', 
                        'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:30,\tbalance:0']

        #act
        tree.insert(50)
        tree.insert(25)
        tree.insert(30)
        target = tree.lookup(30)
        tree.balance_avl(target)    
        result_list = tree.print_generate_strings()


        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]
    #----------------
    #----------------
    # INSERT AVL
    def test_insertAVL_90_4_2_9_1_3_6_20_8_7(self):
        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 4,\tleft: 2,\tright: 9,\theight: 4,\tparent:None,\tbalance:-1', 
                        'curr v: 2,\tleft: 1,\tright: 3,\theight: 2,\tparent:4,\tbalance:0', 
                        'curr v: 9,\tleft: 7,\tright: 90,\theight: 3,\tparent:4,\tbalance:0', 
                        'curr v: 1,\tleft: None,\tright: None,\theight: 1,\tparent:2,\tbalance:0', 
                        'curr v: 3,\tleft: None,\tright: None,\theight: 1,\tparent:2,\tbalance:0', 
                        'curr v: 7,\tleft: 6,\tright: 8,\theight: 2,\tparent:9,\tbalance:0', 
                        'curr v: 90,\tleft: 20,\tright: None,\theight: 2,\tparent:9,\tbalance:1', 
                        'curr v: 6,\tleft: None,\tright: None,\theight: 1,\tparent:7,\tbalance:0', 
                        'curr v: 8,\tleft: None,\tright: None,\theight: 1,\tparent:7,\tbalance:0', 
                        'curr v: 20,\tleft: None,\tright: None,\theight: 1,\tparent:90,\tbalance:0']
        
        tree.insert_avl(90)
        tree.insert_avl(4)
        tree.insert_avl(2)
        tree.insert_avl(9)
        tree.insert_avl(1)
        tree.insert_avl(3)
        tree.insert_avl(6)
        tree.insert_avl(20)
        tree.insert_avl(8)
        tree.insert_avl(7)

        #act
        result_list = tree.print_generate_strings()

        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]          

    def test_insertAVL_right_straight_1(self):

        #arrange
        tree = BinaryTreeAVL()

        assert_values = ['curr v: 75,\tleft: 50,\tright: 125,\theight: 3,\tparent:None,\tbalance:-1', 
                        'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 125,\tleft: 100,\tright: 150,\theight: 2,\tparent:75,\tbalance:0', 
                        'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:125,\tbalance:0', 
                        'curr v: 150,\tleft: None,\tright: None,\theight: 1,\tparent:125,\tbalance:0']
        

        tree.insert_avl(50)
        tree.insert_avl(75)
        tree.insert_avl(100)
        tree.insert_avl(125)
        tree.insert_avl(150)



        #act
        result_list = tree.print_generate_strings()


        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]    

    def test_insertAVL_right_straight_2(self):

        #arrange
        tree = BinaryTreeAVL()

        
        assert_values = ['curr v: 125,\tleft: 75,\tright: 225,\theight: 4,\tparent:None,\tbalance:-1', 
                        'curr v: 75,\tleft: 50,\tright: 100,\theight: 2,\tparent:125,\tbalance:0', 
                        'curr v: 225,\tleft: 175,\tright: 250,\theight: 3,\tparent:125,\tbalance:0', 
                        'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 175,\tleft: 150,\tright: 200,\theight: 2,\tparent:225,\tbalance:0', 
                        'curr v: 250,\tleft: None,\tright: 275,\theight: 2,\tparent:225,\tbalance:-1', 
                        'curr v: 150,\tleft: None,\tright: None,\theight: 1,\tparent:175,\tbalance:0', 
                        'curr v: 200,\tleft: None,\tright: None,\theight: 1,\tparent:175,\tbalance:0', 
                        'curr v: 275,\tleft: None,\tright: None,\theight: 1,\tparent:250,\tbalance:0']
        

        tree.insert_avl(50)
        tree.insert_avl(75)
        tree.insert_avl(100)
        tree.insert_avl(125)
        tree.insert_avl(150)
        tree.insert_avl(175)
        tree.insert_avl(200)
        tree.insert_avl(225)
        tree.insert_avl(250)
        tree.insert_avl(275)

        #act
        result_list = tree.print_generate_strings()


        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]

    def test_insertAVL_left_straight_1(self):

        #arrange
        tree = BinaryTreeAVL()

        
        assert_values = ['curr v: 200,\tleft: 100,\tright: 250,\theight: 4,\tparent:None,\tbalance:1', 
                        'curr v: 100,\tleft: 75,\tright: 150,\theight: 3,\tparent:200,\tbalance:0', 
                        'curr v: 250,\tleft: 225,\tright: 275,\theight: 2,\tparent:200,\tbalance:0', 
                        'curr v: 75,\tleft: 50,\tright: None,\theight: 2,\tparent:100,\tbalance:1', 
                        'curr v: 150,\tleft: 125,\tright: 175,\theight: 2,\tparent:100,\tbalance:0', 
                        'curr v: 225,\tleft: None,\tright: None,\theight: 1,\tparent:250,\tbalance:0', 
                        'curr v: 275,\tleft: None,\tright: None,\theight: 1,\tparent:250,\tbalance:0', 
                        'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                        'curr v: 125,\tleft: None,\tright: None,\theight: 1,\tparent:150,\tbalance:0', 
                        'curr v: 175,\tleft: None,\tright: None,\theight: 1,\tparent:150,\tbalance:0']
        

        tree.insert_avl(275)
        tree.insert_avl(250)
        tree.insert_avl(225)
        tree.insert_avl(200)
        tree.insert_avl(125)
        tree.insert_avl(150)
        tree.insert_avl(175)
        tree.insert_avl(100)
        tree.insert_avl(75)
        tree.insert_avl(50)

        #act
        result_list = tree.print_generate_strings()


        #assert
        for i in range(len(result_list)):
            assert assert_values[i] == result_list[i]   

    #----------------


    

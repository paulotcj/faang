class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

#--------

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
    def lookup2(self, value):
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



#--------    
#                 90
#            4     
#       2        9
#     1   3        20
#               
 



tree = BinaryTree()
tree.insert(90)
tree.insert(4)
tree.insert(2)
tree.insert(9)
tree.insert(1)
tree.insert(3)
tree.insert(20)
# tree.print() #this is ok
tree.remove(9)
tree.remove(90)
tree.print()
# exit()

#--------    
#                 90
#            4     
#       2        9
#     1   3    6   20
#               8
#              7 



tree = BinaryTree()
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
# tree.print()
tree.remove(4)
tree.print()
# exit(0)

#--------    
#      9
#   4     20
# 1  6  15  170

tree = BinaryTree()
tree.insert(9)
tree.print()

tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.print()
print(f"-------------------------------------------")
lookup = tree.lookup(9)
print(f"Look up result: {lookup.value if lookup != None else 'None'}")
lookup = tree.lookup(15)
print(f"Look up result: {lookup.value if lookup != None else 'None'}")
lookup = tree.lookup(20)
print(f"Look up result: {lookup.value if lookup != None else 'None'}")
lookup = tree.lookup(170)
print(f"Look up result: {lookup.value if lookup != None else 'None'}")
lookup = tree.lookup(6)
print(f"Look up result: {lookup.value if lookup != None else 'None'}")
lookup = tree.lookup(1)
print(f"Look up result: {lookup.value if lookup != None else 'None'}")
lookup = tree.lookup(4)
print(f"Look up result: {lookup.value if lookup != None else 'None'}")
lookup = tree.lookup(99)
print(f"Look up result: {lookup.value if lookup != None else 'None'}")

print(f"-------------------------------------------")
lookup = tree.lookup2(9)
print(f"Look up current: {lookup['current'].value if lookup != None else 'None'} , parent: {lookup['parent'].value if lookup != None and lookup['parent'] != None else 'None'}")
lookup = tree.lookup2(15)
print(f"Look up current: {lookup['current'].value if lookup != None else 'None'} , parent: {lookup['parent'].value if lookup != None and lookup['parent'] != None else 'None'}")
lookup = tree.lookup2(20)
print(f"Look up current: {lookup['current'].value if lookup != None else 'None'} , parent: {lookup['parent'].value if lookup != None and lookup['parent'] != None else 'None'}")
lookup = tree.lookup2(170)
print(f"Look up current: {lookup['current'].value if lookup != None else 'None'} , parent: {lookup['parent'].value if lookup != None and lookup['parent'] != None else 'None'}")
lookup = tree.lookup2(6)
print(f"Look up current: {lookup['current'].value if lookup != None else 'None'} , parent: {lookup['parent'].value if lookup != None and lookup['parent'] != None else 'None'}")
lookup = tree.lookup2(1)
print(f"Look up current: {lookup['current'].value if lookup != None else 'None'} , parent: {lookup['parent'].value if lookup != None and lookup['parent'] != None else 'None'}")
lookup = tree.lookup2(4)
print(f"Look up current: {lookup['current'].value if lookup != None else 'None'} , parent: {lookup['parent'].value if lookup != None and lookup['parent'] != None else 'None'}")
lookup = tree.lookup2(99)
print(f"Look up current: {lookup['current'].value if lookup != None else 'None'} , parent: {lookup['parent'].value if lookup != None and lookup['parent'] != None else 'None'}")

print(f"-------------------------------------------")
import random
tree = BinaryTree()
unique_random_list = random.sample(range(1, 10001), 1000)

for i in unique_random_list:
    tree.insert(i)


tree.print()
print(f"-------------------------------------------")
for i in unique_random_list:
    lookup = tree.lookup(i)
    if lookup == None: print(f"Error - Element {i} was not found in the tree.")
    elif lookup.value != i : print(f"Error - Element {i} does not match the lookup result: {lookup.value}")
    else: print(f"Sucess - Element {i} matches the lookup result: {lookup.value}")
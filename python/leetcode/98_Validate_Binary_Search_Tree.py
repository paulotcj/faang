# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

from typing import Optional
#------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#------------------------------------------------------------------

#------------------------------------------------------------------
class BinaryTree:
    #------------------------------------------------------------------
    def __init__(self) -> None:
        self.root = None
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def insert(self, value):
        new_obj = TreeNode(value)

        if self.root == None:
            self.root = new_obj
            return
        
        #---------------
        current_node = self.root
        while(True):
            if value < current_node.val: #must go to the left side
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
            if value == current.val:
                return current
            elif value < current.val:
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
            if value == current.val:
                return {'current': current, 'parent' : parent}
            elif value < current.val:
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
                # print(f"Current: {current.val} - left: {current.left.val}")
            else: #right sided
                parent.right = current.left if current.left != None else current.right
                # print(f"Current: {current.val} - left: {current.right.val}")

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
                left_summary = current.left.val
            if current.right:
                node_list.append(current.right)
                right_summary = current.right.val

            print(f"Current value: {current.val}, current.left: {left_summary} , current.right: {right_summary}")

            current =  node_list.pop(0) if node_list else None 
    #------------------------------------------------------------------
#------------------------------------------------------------------

#------------------------------------------------------------------
class Solution:
    #------------------------------------------------------------------
    #Optional[TreeNode] - indicating that a function or variable could either be of type TreeNode or it could be None.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,float("-inf"),float("inf"))
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def helper(self,root,min,max):
        if not root:
            return True
        if min>=root.val or max<=root.val:
            return False
        res = self.helper(root.left,min,root.val) and self.helper(root.right,root.val,max)
        return res
    #------------------------------------------------------------------
#------------------------------------------------------------------
    
tree = BinaryTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)

sol = Solution()
print(sol.isValidBST(tree.root))
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
    



sol = Solution()
print('-------------------------------------------')
tree_node_2 = TreeNode(2)
tree_node_1 = TreeNode(1)
tree_node_3 = TreeNode(3)
tree_node_2.left = tree_node_1
tree_node_2.right = tree_node_3
validation = sol.isValidBST(tree_node_2)
print(f"validation: {validation}")
print('-------------------------------------------')
# Input: root = [5,1,4,null,null,3,6]
# Output: false
tree_node_5 = TreeNode(5)
tree_node_1 = TreeNode(1)
tree_node_4 = TreeNode(4)
tree_node_3 = TreeNode(3)
tree_node_6 = TreeNode(6)
tree_node_5.left = tree_node_1
tree_node_5.right = tree_node_4
tree_node_4.left = tree_node_3
tree_node_4.right = tree_node_6
validation = sol.isValidBST(tree_node_5)
print(f"validation: {validation}")
print('-------------------------------------------')
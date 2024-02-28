from typing import List, Optional, Dict
# Definition for a binary tree node.

#-------------------------------------------------------------------------
class TreeNode:
    #-------------------------------------------------------------------------
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        stack : List[ TreeNode ] = [ root ]

        return_list = List[List[int]] = []
        current_level_list : List[int] = []
        level_identifier : TreeNode = stack[0]
        current: TreeNode


        while stack:
            current  = stack.pop()

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)




    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
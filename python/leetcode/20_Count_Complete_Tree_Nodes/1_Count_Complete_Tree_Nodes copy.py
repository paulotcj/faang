#problem: https://leetcode.com/problems/count-complete-tree-nodes/description/
from typing import Optional, List, Dict
#-------------------------------------------------------------------------
class CreateTree:
    #-------------------------------------------------------------------------
    def create_tree():
        root = TreeNode(3)
        
        root.left = TreeNode(9)
        root.right = TreeNode(20)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        return root
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        count : int = 0
        queue : List[TreeNode] = [root]

        while queue:
            current : TreeNode = queue.pop(0)
            count += 1

            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        
        return count
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
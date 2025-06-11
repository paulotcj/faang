#problem: https://leetcode.com/problems/validate-binary-search-tree
from typing import Optional, List, Dict
#-------------------------------------------------------------------------
class CreateTree:
    #-------------------------------------------------------------------------
    def create_tree():
        root : TreeNode = None
        #---
        #level 1
        root = TreeNode(12)
        #---
        #level 2
        root.left = TreeNode(7)
        root.right = TreeNode(18)
        #---
        #level 3
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(9)

        root.right.left = TreeNode(14)
        root.right.right = TreeNode(25)
        #---
        #level 4
        # root.left.left.left = TreeNode(8)
        # root.left.left.right = TreeNode(9)

        root.left.right.left = TreeNode(8)
        root.left.right.right = TreeNode(11)

        # root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(15)

        # root.right.right.left = TreeNode(14)
        # root.right.right.right = TreeNode(15)
        #---
        #level 5
        root.right.left.right.right = TreeNode(16)
        
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        current: TreeNode = root
        queue : List[ List[int, TreeNode, int] ] = [ [float("-inf"), current, float("inf") ] ]
        #-------------
        while queue:
            min , current, max = queue.pop(0)

            if current.val <= min or current.val >= max:
                return False
            
            if current.left: 
                queue.append([min, current.left, current.val])
            if current.right:
                queue.append([current.val, current.right, max])
        #-------------
        return True
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def helper(self,node:TreeNode, min: int,max: int):
        if not node: return True
        
        #node cannot be smalle or equal to min or node cannot be greater or equal to max
        if min >= node.val or max<=node.val:
            return False
        
        #investigate left and right subtrees
        res:bool = self.helper(node = node.left, min = min, max = node.val) and self.helper(node = node.right, min = node.val, max = max)
        
        return res
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
tree = CreateTree.create_tree()
sol = Solution()
# sol.exists(tree, 11)
result = sol.isValidBST(tree)
print(result)    
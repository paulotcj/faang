#problem: https://leetcode.com/problems/count-complete-tree-nodes/description/
from typing import Optional, List, Dict
#-------------------------------------------------------------------------
class CreateTree:
    #-------------------------------------------------------------------------
    def create_tree_1():
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
    def create_tree():
        root : TreeNode = None
        #---
        #level 1
        root = TreeNode(1)
        #---
        #level 2
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        #---
        #level 3
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        #---
        #level 4
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)

        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)

        root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(13)

        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        
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
    def getLeftHeight(self, root):
        ans = 0
        while root.left:
            ans += 1
            root = root.left if root.left else root.right
        return ans    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def getRightHeight(self, root):
        ans = 0
        while root.right:
            ans += 1
            root = root.right if root.right else root.left
        return ans    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dfs(self, root):
        if not root: return 0

        l = self.getLeftHeight(root)
        r = self.getRightHeight(root)
        
        if l == r:
            return 2**(l+1) - 1
        
        return self.dfs(root.left) + self.dfs(root.right) + 1    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
            
tree = CreateTree.create_tree()
sol = Solution()
# sol.exists(tree, 11)
result = sol.countNodes(tree)
print(result)
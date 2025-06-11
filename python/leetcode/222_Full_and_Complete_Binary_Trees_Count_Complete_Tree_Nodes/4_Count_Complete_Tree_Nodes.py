#problem: https://leetcode.com/problems/count-complete-tree-nodes/description/
from typing import Optional
from collections import deque
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
class BinaryTree: # don't care about this implementation
    #-------------------------------------------------------------------------
    @staticmethod
    def from_list(values: list[Optional[int]]) -> Optional[TreeNode]:
        if not values: return None

        root : TreeNode = TreeNode( val = values[0])
        queue: deque[TreeNode] = deque([root])

        #-----------------------------------
        i : int = 1
        while queue and i < len(values):
            curr_node : TreeNode = queue.popleft()
            if i < len(values) and values[i] is not None:
                curr_node.left = TreeNode(values[i])
                queue.append(curr_node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                curr_node.right = TreeNode(values[i])
                queue.append(curr_node.right)
            i += 1
        #-----------------------------------
        return root
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
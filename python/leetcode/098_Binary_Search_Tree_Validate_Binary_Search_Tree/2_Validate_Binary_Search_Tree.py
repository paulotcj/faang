#problem: https://leetcode.com/problems/validate-binary-search-tree
from typing import Optional, List, Dict
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
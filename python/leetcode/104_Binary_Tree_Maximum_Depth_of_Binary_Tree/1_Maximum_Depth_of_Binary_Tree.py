#problem: https://leetcode.com/problems/maximum-depth-of-binary-tree
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
        if not values:
            return None
        root = TreeNode(values[0])
        queue: deque[TreeNode] = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def maxDepth_recursive(self, root: TreeNode) -> int:
        
        if root is None: return 0
        return 1 + max( self.maxDepth_recursive(root = root.left), self.maxDepth_recursive(root = root.right) )
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return_val : int = self.maxDepth_recursive(root = root)
        return return_val
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('------------------')

input = [3,9,20,None,None,15,7]
binary_tree_root = BinaryTree.from_list(values = input)
expected = 3
sol = Solution()
result = sol.maxDepth(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { set(result) == set(expected)}')
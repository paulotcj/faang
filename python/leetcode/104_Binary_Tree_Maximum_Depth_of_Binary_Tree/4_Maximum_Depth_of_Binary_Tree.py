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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return_val : int = self.max_depth_dfs(root = root)
        return return_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def max_depth_dfs( self , root : Optional[TreeNode] ) -> int :
        if root is None : return 0 # if root is None the level is 0

        max_depth : int = 0
        current_depth : int = max_depth
        current : TreeNode = root
        stack : list[TreeNode] = []
        visited : dict[TreeNode, bool] = {}

        #-----------------------------------
        while current : 
            if current not in visited : 
                current_depth += 1
                max_depth = max( max_depth , current_depth )
                visited[current] = True
            
            if current.left and current.left not in visited : 
                stack.append(current)
                current = current.left
            elif current.right and current.right not in visited : 
                stack.append(current)
                current = current.right
            else: # left and right are None or they were visited already
                current = stack.pop() if stack else None # coming back after exploring one of its children
                current_depth -= 1

        #-----------------------------------
        return max_depth
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def max_depth_dfs2(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        #----
        max_depth : int = 1
        current_depth_level: int = 0
        current: TreeNode = root
        stack : list[TreeNode] = [] #backtrack my path
        visited : dict[TreeNode, bool] = {} #i also need to know which ones I visited
        #-----------------------------------
        while current:

            if current not in visited: # new node never visited
                current_depth_level += 1
                max_depth = max(max_depth, current_depth_level)
                visited[current] = True


            if current.left and current.left not in visited:
                stack.append(current) #backtrack my path
                current = current.left  
            elif current.right and current.right not in visited:
                stack.append(current) #backtrack my path
                current = current.right
            else:
                current = stack.pop() if stack else None
                current_depth_level -= 1

        #-----------------------------------
                
        return max_depth
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------')

input = [3,9,20,None,None,15,7]
binary_tree_root = BinaryTree.from_list(values = input)
expected = 3
sol = Solution()
result = sol.maxDepth(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }')


print('------------------')

input = [1,None,2]
binary_tree_root = BinaryTree.from_list(values = input)
expected = 2
sol = Solution()
result = sol.maxDepth(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }')
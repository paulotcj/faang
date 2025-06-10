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
        return_val : int = self.max_depth_dfs(curr_node = root)
        return return_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def max_depth_dfs( self , curr_node : Optional[TreeNode] ) -> int :
        if curr_node is None : return 0
        max_depth : int = 1 # as of right now we know it's at least 1

        stack : list[tuple[TreeNode, int]] = [ (curr_node, max_depth) ]

        #-----------------------------------
        while stack : 
            #-----
            temp_pop : tuple[TreeNode , int] = stack.pop()
            loop_node : TreeNode = temp_pop[0]
            current_level : int = temp_pop[1]
            #-----

            # if both children are None then the current level is correct already
            if loop_node.left is None and loop_node.right is None : continue

            current_level += 1 # at least one valid child, so we add 1 level

            max_depth = max( max_depth, current_level )

            if loop_node.left:
                stack.append( (loop_node.left, current_level) )
            if loop_node.right:
                stack.append( (loop_node.right, current_level) )
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
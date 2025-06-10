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
        if not curr_node : return 0

        max_depth : int = 1 # at this point we know this is the min depth of the tree
        stack : list[tuple[TreeNode, int]] = [ ( curr_node , max_depth ) ]

        #-----------------------------------
        while stack :
            node_loop , node_loop_depth = stack.pop()
            #-----
            if node_loop : # need to check, as this might be None from a non-existing child
                max_depth = max( max_depth , node_loop_depth ) # the node_loop_depth was not computed yet, it was pushed to the stack but not calculated
                # now schedule to check the left and right child
                stack.append( ( node_loop.left , node_loop_depth + 1 ) ) # we will only compute this added level if this node is not empty
                stack.append( ( node_loop.right, node_loop_depth + 1 ) ) # same here
            #-----
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
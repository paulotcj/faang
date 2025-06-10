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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return_val : int = self.max_depth_bfs(curr_node = root)
        return return_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def max_depth_bfs( sefl , curr_node : Optional[TreeNode] ) -> int :
        if not curr_node : return 0

        queue : deque[TreeNode] = deque( [curr_node] )
        max_depth : int = 0

        #-----------------------------------
        while queue : 
            queue_size : int =  len(queue)
            #-----------------------------------
            for _ in range(queue_size) : # process all nodes at the current level
                curr_node : TreeNode = queue.popleft()
                if curr_node.left  : queue.append( curr_node.left  )
                if curr_node.right : queue.append( curr_node.right )
            #-----------------------------------
            max_depth += 1 # after processing the current level, increase depth
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
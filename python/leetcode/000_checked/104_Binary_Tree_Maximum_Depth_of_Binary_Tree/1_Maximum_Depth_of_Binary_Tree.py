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
    ''' Depth First Search style - the idea here is that you go recursively dow the tree 
    until you reach the lowest possible node, this node will have its left and right 
    pointers as None, then they both will return 0 to its valid parent node. The parent 
    node will issue a max() function between the return levels of left and right, which
    will be max(0,0) = 0, but then it will also add + 1.
    Anf this bubbles up, the parent of this current node will receive current node
    level (1) and then add 1 resulting in 2.
    If the current node's sibling was None, then then the current node reports to its
    parent we would have: max(1, 0) = 1... 
    '''
    #-------------------------------------------------------------------------
    def max_depth_recusive_dfs( self , curr_node : TreeNode ) -> int :
        if curr_node is None : return 0

        return_result : int = 1 + max (
            self.max_depth_recusive_dfs( curr_node = curr_node.left ) ,
            self.max_depth_recusive_dfs( curr_node = curr_node.right)
        )
        return return_result
    #-------------------------------------------------------------------------  
    #-------------------------------------------------------------------------
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return_val : int = self.max_depth_recusive_dfs(curr_node = root)
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
print(f'Is the result correct? { result == expected }')


print('------------------')

input = [1,None,2]
binary_tree_root = BinaryTree.from_list(values = input)
expected = 2
sol = Solution()
result = sol.maxDepth(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }')
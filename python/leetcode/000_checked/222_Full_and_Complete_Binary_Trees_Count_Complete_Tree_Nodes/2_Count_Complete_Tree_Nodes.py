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
    def countNodes( self , root : Optional[TreeNode] ) -> int :
        if root is None : return 0

        count : int = 0
        stack : list[TreeNode] = [ root ]
        #-----------------------------------
        while stack : 
            curr : TreeNode = stack.pop()
            count += 1

            if curr.right : stack.append( curr.right )
            if curr.left : stack.append( curr.left ) 
        #-----------------------------------
        return count
    #-------------------------------------------------------------------------    
#-------------------------------------------------------------------------


print('------------------')
input = [1,2,3,4,5,6]
binary_tree_root = BinaryTree.from_list(values = input)
expected = 6
sol = Solution()
result = sol.countNodes(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 



print('------------------')
input = [1]
binary_tree_root = BinaryTree.from_list(values = input)
expected = 1
sol = Solution()
result = sol.countNodes(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 



print('------------------')
input = []
binary_tree_root = BinaryTree.from_list(values = input)
expected = 0
sol = Solution()
result = sol.countNodes(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 
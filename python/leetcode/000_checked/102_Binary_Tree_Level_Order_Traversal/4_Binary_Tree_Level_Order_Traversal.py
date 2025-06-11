#problem: https://leetcode.com/problems/binary-tree-level-order-traversal
from collections import deque
from typing import Optional
# Definition for a binary tree node.

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
    def levelOrder( self , root : Optional[TreeNode] ) -> list[list[int]] :
        if not root : return []

        result : list[list[int]] = []
        queue : deque[TreeNode] = deque( [root] )

        #-----------------------------------
        while queue :
            sibling_lvl : list[int] = []
            #-----------------------------------
            for _ in range(len(queue)) :
                curr_node : TreeNode = queue.popleft()
                sibling_lvl.append( curr_node.val )

                if curr_node.left  : queue.append( curr_node.left )
                if curr_node.right : queue.append( curr_node.right )
            #-----------------------------------
            result.append( sibling_lvl )
        #-----------------------------------

        return result
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    

print('------------------')
sol = Solution()
input = [3,9,20,None,None,15,7]
binary_tree_root = BinaryTree.from_list(values = input)
result = sol.levelOrder(binary_tree_root)
expected = [[3],[9,20],[15,7]]
print(f'result  : {result}')
print(f'expected: {expected}')
print(f'result == expected: {result == expected}')


print('------------------')
sol = Solution()
input = [1]
binary_tree_root = BinaryTree.from_list(values = input)
result = sol.levelOrder(binary_tree_root)
expected = [[1]]
print(f'result  : {result}')
print(f'expected: {expected}')
print(f'result == expected: {result == expected}')
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
    def levelOrder( self , root : Optional[TreeNode] ) -> list[list[int]] : # BFS style
        if root is None : return []

        queue : deque[TreeNode] = deque( [root] )
        count_down_siblings : int = 1 # because at the root level there's only 1 node
        return_list : list[ list[int] ] = [[]]

        #-----------------------------------
        while queue : 
            current : TreeNode = queue.popleft()
            count_down_siblings -= 1
            return_list[-1].append(current.val)

            if current.left  : queue.append(current.left)
            if current.right : queue.append(current.right)

            if count_down_siblings == 0 :
                count_down_siblings = len(queue) # some nodes only have 1 child, some have 2 children
                return_list.append( [] )
        #-----------------------------------

        return_list.pop() # remove the tail empty list added by default when a level is depleted

        return return_list
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
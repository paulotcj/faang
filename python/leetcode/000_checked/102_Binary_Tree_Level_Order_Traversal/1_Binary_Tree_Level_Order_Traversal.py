#problem: https://leetcode.com/problems/binary-tree-level-order-traversal
from collections import deque
from typing import Optional

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
    def levelOrder( self , root : Optional[TreeNode] ) -> list[list[int]] : # DFS style
        if root is None : return []

        stack : list[tuple[TreeNode,int]] = [ (root, 1) ]
        return_list : list[list[int]] = []
        #-----------------------------------
        while stack :
            current , current_level = stack.pop()

            if len(return_list) < current_level : return_list.append( [] ) # new level needs to be added

            return_list[current_level - 1].append(current.val)

            # the right side needs to be added first, as when the stack pops the left will be the first out
            if current.right : stack.append( (current.right , current_level + 1) ) 
            if current.left  : stack.append( (current.left  , current_level + 1) )
        #-----------------------------------
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
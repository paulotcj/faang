#problem: https://leetcode.com/problems/validate-binary-search-tree
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
    def isValidBST( self, root : Optional[TreeNode] ) -> bool : # BFS style
        if not root : return True # an empty tree is still valid

        queue : deque[tuple[TreeNode, int, int]] = deque( [ (root, float('-inf'), float('inf')) ] )

        #-----------------------------------
        while queue : 
            node , min_val , max_val = queue.popleft()

            if not node: continue # still a valid BST

            if not (min_val < node.val < max_val) : return False # invalid BST

            ''' the format is: min_val < node.val < max_val
            The left node is smaller than the curr_node, that doesn't tell us anything about the min_val
            but we now know that max_val should not be bigger than curr_node.val, so for the left node:
              (left_node, min_val, curr_node.val)
            The right node is bigger than curr_node, that doesn't tell us anything about the max_val but
              we now know that the min_val should not be smaller than curr_node.val, so:
              (right_node, curr_node.val, max_node)
            '''
            queue.append( ( node.left  , min_val  , node.val ) )
            queue.append( ( node.right , node.val , max_val  ) )

        #-----------------------------------
        return True # if no fault was found, the everything is alright
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
print('------------------')
input = [2,1,3]
binary_tree_root = BinaryTree.from_list(values = input)
expected = True
sol = Solution()
result = sol.isValidBST(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 



print('------------------')
input = [5,1,4,None,None,3,6]
binary_tree_root = BinaryTree.from_list(values = input)
expected = False
sol = Solution()
result = sol.isValidBST(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 



print('------------------')
input = [2,1,3]
binary_tree_root = BinaryTree.from_list(values = input)
expected = True
sol = Solution()
result = sol.isValidBST(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 
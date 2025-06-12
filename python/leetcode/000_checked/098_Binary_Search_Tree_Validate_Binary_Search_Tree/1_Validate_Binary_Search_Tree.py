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
    def isValidBST( self , root : Optional[TreeNode] ) -> bool :
        result : bool = self.helper( node = root, min = float('-inf'), max = float('inf') )
        return result
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def helper( self , node : TreeNode , min : int , max : int ) -> bool :
        if not node : return True # if this node is None then its subtree is valid

        if min >= node.val or max <= node.val : return False # invalid BST

        result : bool = self.helper( node = node.left, min = min, max = node.val ) \
                    and self.helper( node = node.right, min = node.val, max = max )
    
        return result
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
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
    def isValidBST( self , root : Optional[TreeNode] ) -> bool : # DFS style
        if not root : return True # an empty tree is still valid

        stack : list[tuple[TreeNode, int, int]] = [ (root, float('-inf'), float('inf')) ]

        #-----------------------------------
        while stack :
            node , min_val , max_val = stack.pop()
            if not node : continue # no issues here, still valid (node and subtree)

            if not ( min_val < node.val < max_val ) : return False # if this is not true then it breaks the rules of a valid BST

            ''' lets recap, left < curr_node < right. And the stack a tuple with this format:
            (node_to_stack, min_val, max_val).
            That means when we stack the left node, the min value continues to be whatever it was
              before, but the max value is now limited by the parent node, as we now have this info
            When we stack the the right node, the max_value continue to be whatever it was, but the min
              value now is the parent node's value, as now we have this info
            '''
            # format (node_to_stack, min_val, max_val)
            stack.append( (node.left, min_val, node.val) ) # the left node is smaller than the current node
            stack.append( (node.right, node.val, max_val) )
            
        #-----------------------------------

        return True
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
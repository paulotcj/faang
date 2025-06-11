#problem: https://leetcode.com/problems/binary-tree-right-side-view/description/
from typing import List, Dict, Optional
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        stack : List[ List[TreeNode, int] ] = [ [root,1] ]
        return_list : List[ int ] = []
        #---
        temp_l : List[TreeNode, int]
        current = TreeNode
        current_level : int

        #-----------------------------------
        while stack:
            temp_l  = stack.pop()
            current = temp_l[0]
            current_level = temp_l[1]

            #---
            if len(return_list) < current_level: #new level needs to be added
                return_list.append(current.val)
            else:
                return_list[current_level-1] = current.val
            #---
            if current.right: #the right side needs to be added first, because we will push to the stack and then when we pop this will be the last
                stack.append([current.right,current_level+1])
            if current.left:
                stack.append([current.left, current_level+1])
            #---
        #-----------------------------------
                
        return return_list
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
print('------------------')
input = [1,2,3,None,5,None,4]
binary_tree_root = BinaryTree.from_list(values = input)
expected = [1,3,4]
sol = Solution()
result = sol.rightSideView(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 


print('------------------')
input = [1,2,3,4,None,None,None,5]
binary_tree_root = BinaryTree.from_list(values = input)
expected = [1,3,4,5]
sol = Solution()
result = sol.rightSideView(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 
        


print('------------------')
input = [1,None,3]
binary_tree_root = BinaryTree.from_list(values = input)
expected = [1,3]
sol = Solution()
result = sol.rightSideView(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 


print('------------------')
input = []
binary_tree_root = BinaryTree.from_list(values = input)
expected = []
sol = Solution()
result = sol.rightSideView(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 
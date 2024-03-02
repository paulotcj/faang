#problem: https://leetcode.com/problems/binary-tree-level-order-traversal
from typing import List, Optional, Dict
# Definition for a binary tree node.

#-------------------------------------------------------------------------
class CreateTree:
    #-------------------------------------------------------------------------
    def create_tree():
        root = TreeNode(3)
        
        root.left = TreeNode(9)
        root.right = TreeNode(20)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        return root
    #-------------------------------------------------------------------------
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
class Solution:
    #-------------------------------------------------------------------------
    def levelOrder_original(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        stack : List[ List[TreeNode, int] ] = [ [root,1] ]
        return_list : List[List[int]] = []
        #---
        temp_l : List[TreeNode, int]
        current = TreeNode
        current_level : int

        #-------------
        while stack:
            temp_l  = stack.pop()
            current = temp_l[0]
            current_level = temp_l[1]

            #---
            if len(return_list) < current_level: #new level needs to be added
                return_list.append([current.val])
            else:
                return_list[current_level-1].append(current.val)
            #---
            if current.right: #the right side needs to be added first, because we will push to the stack and then when we pop this will be the last
                stack.append([current.right,current_level+1])
            if current.left:
                stack.append([current.left, current_level+1])
            #---
        #-------------
                
        return return_list
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        queue : List[int] = [root]
        count_down_level = 1
        return_list : List[ List[int] ] = [[]]

        #-------------
        while queue:
            current = queue.pop(0)
            count_down_level -= 1
            return_list[-1].append(current.val)


            if current.left:
                queue.append(current.left)       
            if current.right:
                queue.append(current.right)
         

            if count_down_level == 0:
                count_down_level = len(queue)
                return_list.append([])
        #-------------
                
        return_list.pop() #remove the last empty list
                
        return return_list

    #-------------------------------------------------------------------------    
#-------------------------------------------------------------------------
    
sol = Solution()
root = CreateTree.create_tree()
result = sol.levelOrder(root)
expected = [[3], [9, 20], [1, 4, 15, 7]]
print(f'result  : {result}')
print(f'expected: {expected}')
print(f'result == expected: {result == expected}')
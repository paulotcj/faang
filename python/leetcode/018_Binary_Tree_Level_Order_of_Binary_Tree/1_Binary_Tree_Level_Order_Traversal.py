#problem: https://leetcode.com/problems/binary-tree-level-order-traversal
from collections import deque
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
    def levelOrder_1(self, root: Optional[TreeNode]) -> List[List[int]]:
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
    def levelOrder_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        queue : List[int] = [root]
        count_down_level : int = 1
        return_list : List[ List[int] ] = [[]]

        #-------------
        while queue:
            current : TreeNode = queue.pop(0)
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
    #-------------------------------------------------------------------------
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        result : List[ List[int] ] = []
        queue : List[TreeNode] = [root]
        
        while queue:
            current_level : List[int] = []
            #-------------
            for _ in range(len(queue)):
                current : TreeNode = queue.pop(0)
                current_level.append(current.val)

                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            #-------------
            result.append(current_level)
        #-------------
        return result
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def levelOrder3(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        result : List[List[int]] = []
        queue : deque = deque([root])

        #-------------
        while queue:
            size_queue : int = len(queue)
            curr_level : List[int] = []
            #-------------
            for i in range(size_queue):
                node : TreeNode = queue.popleft() #dequeue
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #-------------
            result.append(curr_level)
        #-------------

        return result
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
sol = Solution()
root = CreateTree.create_tree()
result = sol.levelOrder(root)
expected = [[3], [9, 20], [1, 4, 15, 7]]
print(f'result  : {result}')
print(f'expected: {expected}')
print(f'result == expected: {result == expected}')
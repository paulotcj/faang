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
    def levelOrder_1(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None: return []

        stack : list[ list[TreeNode, int] ] = [ [root,1] ]
        return_list : list[list[int]] = []
        #---
        temp_l : list[TreeNode, int]
        current = TreeNode
        current_level : int

        #-----------------------------------
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
        #-----------------------------------
                
        return return_list
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def levelOrder_2(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None: return []

        queue : list[int] = [root]
        count_down_level : int = 1
        return_list : list[ list[int] ] = [[]]

        #-----------------------------------
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
        #-----------------------------------
                
        return_list.pop() #remove the last empty list
                
        return return_list
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root : return []
        result : list[ list[int] ] = []
        queue : list[TreeNode] = [root]
        
        #-----------------------------------
        while queue:
            current_level : list[int] = []
            #-----------------------------------
            for _ in range(len(queue)):
                current : TreeNode = queue.pop(0)
                current_level.append(current.val)

                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            #-----------------------------------
            result.append(current_level)
        #-----------------------------------
        return result
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def levelOrder3(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: return []
        
        result : list[list[int]] = []
        queue : deque = deque([root])

        #-----------------------------------
        while queue:
            size_queue : int = len(queue)
            curr_level : list[int] = []
            #-----------------------------------
            for i in range(size_queue):
                node : TreeNode = queue.popleft() #dequeue
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #-----------------------------------
            result.append(curr_level)
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
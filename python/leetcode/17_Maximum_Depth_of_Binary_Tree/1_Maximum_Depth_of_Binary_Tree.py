#problem: https://leetcode.com/problems/maximum-depth-of-binary-tree
from typing import List, Dict
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
    def maxDepth1(self, root: TreeNode) -> int:
        
        if root is None: return 0
        return 1 + max( self.maxDepth(root = root.left), self.maxDepth(root = root.right) )
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def maxDepth_beadth_first(self, root: TreeNode) -> int:
        if root is None: return 0
        max_depth : int = 1
        stack : List[ List[TreeNode, int] ] = [ [root, max_depth] ]

        #-------------
        while stack:
            temp_l : List[TreeNode, int] = stack.pop()
            temp: TreeNode = temp_l[0]
            current_level : int = temp_l[1]
            #---
            if temp.left is None and temp.right is None:
                continue
            current_level += 1
            max_depth = max(max_depth, current_level)
            #---
            if temp.left:
                stack.append([temp.left,current_level])
            if temp.right:
                stack.append([temp.right,current_level])
            #---
        #-------------
        
        return max_depth
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        max_depth : int = 0
        current = root
        depth_level = 0
        stack : List[TreeNode] = [] #backtrack my path
        visited : Dict[TreeNode, bool] = {} #i also need to know which ones I visited
        while current:

            if current not in visited: # new node never visited
                depth_level += 1
                max_depth = max(max_depth, depth_level)
                visited[current] = True


            if current.left and current.left not in visited:
                stack.append(current) #backtrack my path
                current = current.left  
            elif current.right and current.right not in visited:
                stack.append(current) #backtrack my path
                current = current.right
            else:
                current = stack.pop() if stack else None
                depth_level -= 1
            


            



    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
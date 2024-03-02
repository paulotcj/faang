#problem: https://leetcode.com/problems/count-complete-tree-nodes/description/
from typing import Optional, List, Dict
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
    def get_height(self, root: TreeNode) -> int:
        height : int = 0
        current : TreeNode = root
        while current:
            height += 1
            current = current.left

        return height
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def exists(self, root: TreeNode, target : int) -> bool:
        current : TreeNode = root
        current_count : int = 1
        
        while current:
            
            
        

    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        tree_height : int = self.get_height(root)
        potential_total_nodes : int = 2 ** tree_height - 1

        #now let's try to play with binary search
        last_level_possible_nodes : int = 2 ** (tree_height - 1) 
        left : int = 0
        right : int = last_level_possible_nodes - 1
        while left <= right:
            mid : int = left + (right - left) // 2

            # 0 + (7 - 0) // 2 = 3
            # nodes go: 0, 1, 2, 3, 4, 5, 6, 7
            #           1, 2, 3, 4, 5, 6, 7, 8
            #                    ^
            # so from a tree level 4 and total number of nodes = 15 
            # the last row is 15 - 4 = 11
            #           1
            #     2           3
            #  4    5      6      7
            # 8 9 10 11  12 13  14 15
            # 1 2 3  4   5  6   7  8

            target_node_num : int = potential_total_nodes - (mid + 1)





    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#problem: https://leetcode.com/problems/count-complete-tree-nodes/description/
from typing import Optional, List, Dict
#-------------------------------------------------------------------------
class CreateTree:
    #-------------------------------------------------------------------------
    def create_tree_1():
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
    def create_tree():
        #---
        #level 1
        root = TreeNode(1)
        #---
        #level 2
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        #---
        #level 3
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        #---
        #level 4
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)

        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)

        root.right.left.left = TreeNode(12)
        # root.right.left.right = TreeNode(13)

        # root.right.right.left = TreeNode(14)
        # root.right.right.right = TreeNode(15)
        
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
        path : List[str] = []
        while target > 1:
            if target % 2 == 0: path.append('L')
            else: path.append('R')

            target = target // 2

        path.reverse()

        curr : TreeNode = root

        for direction in path:
            if direction == 'L' and curr.left: 
                curr = curr.left
            elif direction == 'R' and curr.right: 
                curr = curr.right
            else: return False

        return True
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        tree_height : int = self.get_height(root)
        potential_total_nodes : int = 2 ** tree_height - 1

        #now let's try to play with binary search
        last_level_possible_nodes : int = 2 ** (tree_height - 1) 
        
        left : int = potential_total_nodes - last_level_possible_nodes + 1 #plus 1 because we know that at least the left most node must exists
        right : int = potential_total_nodes
        if self.exists(root, right): return potential_total_nodes

        while left <= right:
            mid : int = left + (right - left) // 2
            if self.exists(root, mid):
                left = mid + 1
            else:
                right = mid - 1

        return left - 1
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
            
tree = CreateTree.create_tree()
sol = Solution()
# sol.exists(tree, 11)
result = sol.countNodes(tree)
print(result)
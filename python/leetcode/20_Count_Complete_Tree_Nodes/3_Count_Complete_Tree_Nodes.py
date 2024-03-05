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
    def getLeftHeight(self, root : TreeNode) -> int:
        height: int = 1
        while root.left:
            height += 1
            if root.left: root = root.left
            else: root = root.right

        return height
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def getRightHeight(self, root: TreeNode) -> int:
        height : int = 1
        while root.right:
            height += 1
            if root.right: root = root.right
            else: root = root.left

        return height
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        queue : List[List[TreeNode, TreeNode, bool]] = [[root, None, False]] 
        result : Dict[TreeNode, List[TreeNode, int]] = {}
        #---------------
        while queue:
            temp : List[TreeNode, TreeNode] = queue.pop(0)
            current : TreeNode = temp[0]
            parent : TreeNode = temp[1]
            already_processed : int = temp[2]

            if already_processed:
                while parent:
                    result[parent][1] += result[current][1]
                    current = parent
                    parent = result[parent][0]
                continue


            left_hei = self.getLeftHeight(current)
            right_hei = self.getRightHeight(current)

            if left_hei != right_hei:
                result[current] = [parent, 1]
                if current.left: queue.append([current.left, current, False]) # false = not processed
                if current.right: queue.append([current.right, current, False])
                queue.append([current, parent, True]) # True = processed
            else:
                subtree_count: int = 2**left_hei - 1
                result[parent][1] += subtree_count
        #---------------

                
        ret_val : int = result[root][1]

        return ret_val
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
            
tree = CreateTree.create_tree()
sol = Solution()
# sol.exists(tree, 11)
result = sol.countNodes(tree)
print(result)
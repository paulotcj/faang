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
        root : TreeNode = None
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
        root.right.left.right = TreeNode(13)

        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        
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
class Res_Tracker:
    #-------------------------------------------------------------------------
    def __init__(self,  node: TreeNode, parent: TreeNode, subtree_count: int = 0):
        self.node = node
        self.parent = parent
        self.subtree_count = subtree_count
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Q_Tracker:
    #-------------------------------------------------------------------------
    def __init__(self,  node: TreeNode, parent: TreeNode):
        self.node = node
        self.parent = parent
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
    def update_upstream(self, result: Dict[TreeNode, Res_Tracker], current_node: TreeNode) -> None:
        current : Res_Tracker = result[current_node]
        added_subtree_count : int = current.subtree_count
        while current.parent:
            parent: Res_Tracker = result[current.parent]
            parent.subtree_count += added_subtree_count
            current = parent
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        queue : List[Q_Tracker] = [ Q_Tracker(node=root, parent=None)] 
        result : Dict[TreeNode, Res_Tracker] = {}
        #---------------
        while queue:
            current : Q_Tracker = queue.pop(0)
            if not current.node: continue

            left_hei : int = self.getLeftHeight(current.node)
            right_hei : int = self.getRightHeight(current.node)

            if left_hei == right_hei:
                result[current.node] = Res_Tracker(node = current.node, parent = current.parent, subtree_count = 2**left_hei - 1)
                self.update_upstream(result = result, current_node = current.node) #update upstream
            else:
                result[current.node] = Res_Tracker(node = current.node, parent = current.parent, subtree_count = 1)
                self.update_upstream(result = result, current_node = current.node) #update upstream
                if current.node.left: queue.append(Q_Tracker(node = current.node.left, parent = current.node))
                if current.node.right: queue.append(Q_Tracker(node = current.node.right, parent = current.node))
        #---------------

        tracker_root : Res_Tracker = result[root]        
        ret_val : int = tracker_root.subtree_count

        return ret_val
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
            
tree = CreateTree.create_tree()
sol = Solution()
# sol.exists(tree, 11)
result = sol.countNodes(tree)
print(result)
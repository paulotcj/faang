#problem: https://leetcode.com/problems/count-complete-tree-nodes/description/
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
    def update_upstream(self, result: dict[TreeNode, Res_Tracker], current_node: TreeNode) -> None:
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

        queue : list[Q_Tracker] = [ Q_Tracker(node=root, parent=None)] 
        result : dict[TreeNode, Res_Tracker] = {}
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
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
        path : list[str] = []
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
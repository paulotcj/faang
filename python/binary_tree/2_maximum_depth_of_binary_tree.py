# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, node: TreeNode) -> int:
        if node == None : return 0

        current_depth = 0

        q = [node]
        while q :
            #---------
            #we add the elements of the current level, but only once we exhausted the count of all the elements
            # currently in the queue, is that we increment the counter
            for _count_current_level in range(0, len(q)):
                curr = q.pop(0)
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)

            current_depth += 1
            #---------
        #---------
        return current_depth
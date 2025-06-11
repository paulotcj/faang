#problem: https://leetcode.com/problems/binary-tree-right-side-view/description/
from typing import List, Dict, Optional
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
    def rightSideView( self , root : Optional[TreeNode] ) -> List[int] :
        if not root : return []

        queue : deque[TreeNode] = deque( [root] )
        return_list : list[int] = []

        #-----------------------------------
        while queue : 
            return_list.append(None) #dummy value for the node which is about to pop
            #-----------------------------------
            for _ in range(len(queue)) : # loop through was added at this current level
                curr : TreeNode = queue.popleft()

                ''' the way this is set up: if a node has both children, the last one
                 will overwrite the previous one, and in this case we are popping left
                 first, meaning the right child might override left. Now if there's no
                 left right will be the default, no issues here. Similarly if we only
                 have a left side, this will be the default
                 '''
                return_list[-1] = curr.val

                if curr.left  : queue.append( curr.left )
                if curr.right : queue.append( curr.right )
            #-----------------------------------
        #-----------------------------------
        return return_list
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
print('------------------')
input = [1,2,3,None,5,None,4]
binary_tree_root = BinaryTree.from_list(values = input)
expected = [1,3,4]
sol = Solution()
result = sol.rightSideView(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 


print('------------------')
input = [1,2,3,4,None,None,None,5]
binary_tree_root = BinaryTree.from_list(values = input)
expected = [1,3,4,5]
sol = Solution()
result = sol.rightSideView(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 
        


print('------------------')
input = [1,None,3]
binary_tree_root = BinaryTree.from_list(values = input)
expected = [1,3]
sol = Solution()
result = sol.rightSideView(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 


print('------------------')
input = []
binary_tree_root = BinaryTree.from_list(values = input)
expected = []
sol = Solution()
result = sol.rightSideView(root = binary_tree_root)
print(f'result: {result}')
print(f'Is the result correct? { result == expected }') 
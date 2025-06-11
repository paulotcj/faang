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
        if root is None : return []

        stack : list[ list[TreeNode, int] ] = [ [root, 1] ]
        result : list[int] = []

        #-----------------------------------
        while stack : 
            curr , curr_lvl = stack.pop()

            if len(result) < curr_lvl : result.append( None ) # shortcut new level needs to be added
            
            ''' the reason to use  result[curr_lvl-1] instead of result[-1], is because this solution
            uses a stack, meaning, we go DFS, and we might be exploring a deep down level, say level 3
            and when we go back popping back the pending items from the stack, itens placed before will
            pop up later, meaning, we might find a new item from a previous level, say lvl 2, pending
            to be processed.'''
            result[curr_lvl-1] = curr.val
            
            # need to investigate this
            print(f'   curr_lvl-1       : {curr_lvl-1}')
            print(f'   result[-1] idx is: { len(result)-1 }')

            if curr.right : stack.append( (curr.right , curr_lvl + 1 )) #the right side needs to be added first, because we will push to the stack and then when we pop this will be the last
            if curr.left  : stack.append( (curr.left  , curr_lvl + 1 ))
        #-----------------------------------
        return result

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
exit()

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
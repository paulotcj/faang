#problem: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
#-------------------------------------------------------------------------
from typing import Optional, List
class Node:
    #-------------------------------------------------------------------------
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class ProcessList:
    def CreateFromArray(self, arr):
        nodes_list : List(Node) = []
        #-------
        for i,v in enumerate(arr):
            if v :
                temp : Node = Node(v, None, None, None)
                nodes_list.append(temp)
            else:
                nodes_list.append(None)
        #-------
        


#-------------------------------------------------------------------------
        


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pass
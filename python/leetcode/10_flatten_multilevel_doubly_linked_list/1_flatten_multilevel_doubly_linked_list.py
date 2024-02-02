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
    #-------------------------------------------------------------------------
    def CreateFromArray(self, arr):
        nodes_list : List(Node) = []
        #---------------
        for i,v in enumerate(arr):
            if v :
                temp : Node = Node(v, None, None, None)
                nodes_list.append(temp)
            else:
                nodes_list.append(None)
        #---------------
        prev : Node = None
        curr : Node = None
        next : Node = None
        for i,v in enumerate(nodes_list):
            if v is None:
                prev = None
                curr = None
                next = None
                continue
                
            curr = v
            curr.prev = prev
            if prev is not None:
                prev.next = curr

            prev = curr
        #---------------
        idx_header, step_count, i = 0, 0, 0
        while i < len(nodes_list):
            if nodes_list[i] is None:
                step_count = -1

                while nodes_list[i] is None and i < len(nodes_list):
                    step_count += 1
                    i += 1

                if nodes_list[i] is not None and i < len(nodes_list):
                    nodes_list[idx_header + step_count].child = nodes_list[i]
                    idx_header = i

            #------
            i += 1

        

        #---------------
            
        return nodes_list[0] if len(nodes_list) > 0 else None

    #-------------------------------------------------------------------------
        


#-------------------------------------------------------------------------
        


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pass


arr = [ 1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12 ]
head = ProcessList().CreateFromArray(arr)
print('hi')
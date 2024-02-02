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
    def CreateFromArray(arr: List[int]):
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
    def print_linked_list (head: Node, outputToScreen = False) -> List[int]:
        curr : Node = head
        list : List[int] = []
        while curr != None:
            list.append(curr.val)
            curr = curr.next

        if outputToScreen:
            print(list)
        return list 
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr: Node = head
        stack_pending_nodes : List[Node] = []

        prev : Node = None
        #-------------
        while curr:

            if curr.child: #if the node has a child start processing the child's list
                stack_pending_nodes.append(curr.next)
                #---
                curr.child.prev = curr
                curr.next = curr.child
                curr.child = None
                #---
                # curr = curr.next
                # continue

            prev = curr
            curr = curr.next
            while curr is None and len(stack_pending_nodes) > 0:
                curr = stack_pending_nodes.pop()
                prev.next = curr
                if curr:
                    curr.prev = prev

        #-------------

        return head
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('----------------------------')
sol = Solution()
arr = [1,2,3,4,5,6,None,None,None,7,8,None,None,11,12]
# 1,2,3,4,5,6
#     7,8
#       11,12
expected = [1,2,3,7,8,11,12,4,5,6]
# error generated: [1,2,3,7,8,11,12]
head = ProcessList.CreateFromArray(arr)


head = sol.flatten(head)
result = ProcessList.print_linked_list(head)
# print(f'result  : {result}')
# print(f'expected: {expected}')
print(f'Is the result correct? { result == expected}')
# exit()

print('----------------------------')
sol = Solution()
arr = [ 1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12 ]

expected = [1,2,3,7,8,11,12,9,10,4,5,6]
head = ProcessList.CreateFromArray(arr)


head = sol.flatten(head)
result = ProcessList.print_linked_list(head)
# print(f'result  : {result}')
# print(f'expected: {expected}')
print(f'Is the result correct? { result == expected}')
# exit()



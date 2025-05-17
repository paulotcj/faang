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
    def print_linked_list (head: Node) -> List[int]:
        curr : Node = head
        list : List[int] = []
        while curr != None:
            list.append(curr.val)
            curr = curr.next

        print(list)
        return list 
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr: Node = head
        list_nodes : List[Node] = []
        stack_pending_nodes : List[Node] = []

        #-------------
        while curr:

            list_nodes.append(curr)

            if curr.child: #if the node has a child start processing the child's list
                stack_pending_nodes.append(curr)
                curr = curr.child
                continue

            curr = curr.next
            while curr is None and len(stack_pending_nodes) > 0:
                curr = stack_pending_nodes.pop().next
        #-------------
                
        #-------------
        for i, v in enumerate(list_nodes):
            #curr - no need to change
            #prev
            if i > 0:
                list_nodes[i].prev = list_nodes[i-1]
            #next
            if i < (len(list_nodes) - 1): #must be less: eg: len = 10, len -1 = 9, so i must be less or equal to 8
                list_nodes[i].next = list_nodes[i+1]
            #child
            list_nodes[i].child = None
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
print(f'result  : {result}')
print(f'expected: {expected}')
print(f'Is the result correct? { result == expected}')
exit()

print('----------------------------')
sol = Solution()
arr = [ 1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12 ]

expected = [1,2,3,7,8,11,12,9,10,4,5,6]
head = ProcessList.CreateFromArray(arr)


head = sol.flatten(head)
result = ProcessList.print_linked_list(head)
print(f'result  : {result}')
print(f'expected: {expected}')
print(f'Is the result correct? { result == expected}')
# exit()


print('hi')
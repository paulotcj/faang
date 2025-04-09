#problem: https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional, List

#-------------------------------------------------------------------------
class ListNode:
    #-------------------------------------------------------------------------
    def __init__(self, x):
        self.val = x
        self.next = None
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class ProcessList:
    #-------------------------------------------------------------------------
    def create_from_array(arr, pos_to_link):
        head = None
        prev = None
        list = []
        for i, v in enumerate(arr):
            curr = ListNode(v)
            list.append(curr)
            if head is None:
                head = curr
            if prev:
                prev.next = curr

            prev = curr

        list[-1].next = list[pos_to_link]
        return head
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        di_temp : List[ListNode] = {}
        temp : ListNode = head

        while temp:
            if temp in di_temp:
                return temp
            else:
                di_temp[temp] = True

            temp = temp.next

        return None
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    

print('----------------------------')
arr = [3,2,0,-4]
pos = 1
head = ProcessList.create_from_array(arr, pos)

print('hi')


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
    # Using Floy's Tortoise and Hare algorithm - Cycle Detection
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        meeting_point : ListNode = self.find_meeting_point(head)
        if meeting_point is None:
            return None

        start_of_cycle : ListNode = self.find_start_of_cycle(head, meeting_point)

        return start_of_cycle
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def find_start_of_cycle(self, head: ListNode, meeting_point: ListNode) -> ListNode:
        start : ListNode = head
        mp_temp : ListNode = meeting_point
        while True:
            if start == mp_temp:
                return start
            start = start.next
            mp_temp = mp_temp.next
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def find_meeting_point(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return None
        
        tortoise : ListNode = head.next
        hare : ListNode = head.next.next

        while hare and hare.next and hare.next.next:
            if tortoise == hare:
                return tortoise

            tortoise = tortoise.next
            hare = hare.next.next

        return None
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('----------------------------')
arr = [1,2,3,4,5,6,7,8]
pos = 2
head = ProcessList.create_from_array(arr, pos)

sol = Solution()
result = sol.detectCycle(head)
exit()
print('hi')    

print('----------------------------')
arr = [3,2,0,-4]
pos = 1
head = ProcessList.create_from_array(arr, pos)

sol = Solution()
result = sol.detectCycle(head)
exit()
print('hi')


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
class ProcessList : 
    #-------------------------------------------------------------------------
    def create_from_array(arr, pos_to_link) : 
        head = None
        prev = None
        list = []
        
        #-----------------------------------
        for loop_idx , loop_val in enumerate(arr):
            curr = ListNode(x = loop_val)
            list.append(curr)
            if head is None :
                head = curr
            if prev : 
                prev.next = curr
                
            prev = curr
        #-----------------------------------
        
        # link the nodes that need to be linked
        list[-1].next = list[pos_to_link]
        
        return head, list[pos_to_link] , list
                
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

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        # First step: Determine if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected
                break
        else:
            # No cycle found
            return None

        # Second step: Find the start node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('----------------------------')
arr = [3,2,0,-4]
pos = 1
head , expected_link , list = ProcessList.create_from_array(arr = arr, pos_to_link=pos)

sol = Solution()
result = sol.detectCycle( head = head )

print(f'result: {result.val if result else result}')
print(f'is this the expected result: {result == expected_link}')



print('----------------------------')
arr = [1,2]
pos = 0
head , expected_link , list = ProcessList.create_from_array(arr = arr, pos_to_link=pos)

sol = Solution()
result = sol.detectCycle( head = head )

print(f'result: {result.val if result else result}')
print(f'is this the expected result: {result == expected_link}')


print('----------------------------')
arr = [1]
pos = -1
head , expected_link , list = ProcessList.create_from_array(arr = arr, pos_to_link=pos)

sol = Solution()
result = sol.detectCycle( head = head )

print(f'result: {result.val if result else result}')
print(f'is this the expected result: {result == expected_link}')




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
    def detectCycle( self, head : Optional[ListNode] ) -> Optional[ListNode] :
        # Floyd’s Tortoise and Hare Algorithm        
        slow : Optional[ListNode] = head # at this point they are the same so we need
        fast : Optional[ListNode] = head #  to start the cycle detection loop by moving them
        
        # First step: Determine if a cycle exists. If a cycle doesn't exist this loop will eventually end
        #-----------------------------------
        while fast and fast.next: # don't check for slow as either it was behind fast of at least the same
            slow = slow.next       # first thing - move the pointers
            fast = fast.next.next
            
            if slow == fast: break # cycle detected
        else: # unsual - python feature
            return None # no cycle, head was None    
        #-----------------------------------
        
        
        # Second step: Find the start node of the cycle
        ''' now we set one pointer at the head and we keep one pointer at the meeting point found
        previously. both pointers will move 1 step at the time, and eventually when they meet this
        will be the begining of the cycle. Check for the proof of Floyd's Hare and Tortoise algorithm
        (probably in this file)'''
        
        pointer_a : ListNode = head
        pointer_b : ListNode = slow
        #-----------------------------------
        while pointer_a is not pointer_b:
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
        #-----------------------------------
        # by exiting the loop the begining of the cycle was found
        return pointer_a
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




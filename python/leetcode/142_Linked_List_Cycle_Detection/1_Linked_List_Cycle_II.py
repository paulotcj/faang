#problem: https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional, List, Dict


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
        dict_nodes : Dict[ListNode] = {}
        curr : ListNode = head
        
        #-----------------------------------
        while curr :
            if curr in dict_nodes : 
                return curr
            else:
                dict_nodes[curr] = True
            
            curr = curr.next
        #-----------------------------------
            
        return None
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




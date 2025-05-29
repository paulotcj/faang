#problem: https://leetcode.com/problems/reverse-linked-list-ii/description/
from typing import Optional, List, Tuple
#-------------------------------------------------------------------------
class ListNode:
    #-------------------------------------------------------------------------
    def __init__( self, val : int = 0, next : 'ListNode' = None ):
        self.val = val
        self.next : 'ListNode' = next
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def create_linked_list(self, arr : List[int] ) -> Optional[ListNode] : 
        head : Optional[ListNode] = None
        curr : Optional[ListNode] = None
        prev : Optional[ListNode] = None
        
        #-----------------------------------
        for idx, val in enumerate(arr):
            curr = ListNode(val = val)
            if idx == 0 : # setting up the root node - there's no prev
                head  = curr
                prev = curr
            else:
            
            # curr is the current node, this is the newest node and we don't point next
            #   to anything, but we should keep track of the previous node, so it's next
            #   pointer can point to curr
                prev.next = curr
                prev = curr
        #-----------------------------------
        return head      
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def print_linked_list( self , head : Optional[ListNode] ) -> List[int] :
        curr : Optional[ListNode] = head
        return_list : List[int] = []
        #-----------------------------------
        while curr != None:
            return_list.append(curr.val)
            curr = curr.next
        #-----------------------------------
            
        return return_list
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseBetween2( self , head : Optional[ListNode] , left : int , right : int) -> Optional[ListNode] :
        # correct base 1 indexing to base 0
        left_idx  : int = left  - 1
        right_idx : int = right - 1
        
        # edge case, if the list is empty or no need to reverse
        if left_idx == right_idx or head == None :
            return head
        
        # dummy node to simplify edge cases as in reversing from head
        dummy_head : ListNode = ListNode(val = None , next = head)
        
        #-------
        one_before_left_target : ListNode = dummy_head # we will manipulate prev, but we need to keep track of dummy_head
        
        '''move one_before_left_target to the node before the 'left' position. if left_idx = 0, 
         then one_before_left_target is not updated. If left_idx = 1 then one_before_left_target
         moves 1 spot.
         remember that at this moment one_before_left_target is pointing at technically 
         position -1. So if left target is at idx 1, by moving 1 spot it will place 
         one_before_left_target at index 0'''
        
        for _ in range(left_idx) : 
            one_before_left_target = one_before_left_target.next
        #-------
        
        # start reversing from 'left_idx' to 'right_idx'
        temp_next : ListNode = None
        curr : ListNode = one_before_left_target.next
        prev : ListNode = one_before_left_target  #potentially this should be called one_before_left
        
        
        # for _ in range( right_idx - left_idx + 1 ) :
        #     temp_next : ListNode = 
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def reverseBetween( self , head : Optional[ListNode] , left : int , right : int) -> Optional[ListNode] :
        # correct base 1 indexing to base 0
        left_idx : int = left - 1
        right_idx : int = right - 1
        
        # Edge case: if the list is empty or no need to reverse
        if not head or left_idx == right_idx:
            return head

        # Create a dummy node to simplify edge cases (e.g., reversing from head)
        dummy_head: ListNode = ListNode(None, head)
        #-------
        
        one_before_left_target: ListNode = dummy_head
        # Move prev to the node before the 'left' position
        for _ in range(left_idx):
            one_before_left_target = one_before_left_target.next
            

        # Start reversing from 'left' to 'right_idx'
        prev: ListNode = one_before_left_target
        curr: ListNode = one_before_left_target.next
        prev_node: Optional[ListNode] = None
        temp_next : ListNode = None

        #-----------------------------------
        # Reverse the sublist
        for _ in range(right_idx - left_idx + 1):
            temp_next: Optional[ListNode] = curr.next # temporatily save this relationship
            curr.next = prev_node # that's what we want to do
            
            # now move 1 step to the right, prev receive curr, curr receives next
            prev_node = curr
            curr = temp_next
        #-----------------------------------

        # Connect the reversed sublist back to the list
        prev.next.next = curr  # Tail of reversed sublist points to the node after 'right_idx'
        prev.next = prev_node  # Node before 'left' points to new head of reversed sublist

        return dummy_head.next
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('----------------------------')
sol = Solution()
arr = [1,2,3,4,5]
left = 2
right = 4
expected = [1,4,3,2,5]    

head = sol.create_linked_list(arr)
_ = sol.print_linked_list(head)
result = sol.reverseBetween(head, left, right)
result = sol.print_linked_list(result)
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
# exit()



print('----------------------------')
sol = Solution()
arr = [3,5]
left = 1
right = 1
expected = [3,5] 

head = sol.create_linked_list(arr)
_ = sol.print_linked_list(head)
result = sol.reverseBetween(head, left, right)
result = sol.print_linked_list(result)
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
arr = [5]
left = 1
right = 1
expected = [5]  

head = sol.create_linked_list(arr)
_ = sol.print_linked_list(head)
result = sol.reverseBetween(head, left, right)
result = sol.print_linked_list(result)
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
arr = [3,5]
left = 1
right = 2
expected = [5,3]  

head = sol.create_linked_list(arr)
_ = sol.print_linked_list(head)
result = sol.reverseBetween(head, left, right)
result = sol.print_linked_list(result)
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
arr = [1,2,3,4,5]
left = 1
right = 4
expected = [4,3,2,1,5]    

head = sol.create_linked_list(arr)
_ = sol.print_linked_list(head)
result = sol.reverseBetween(head, left, right)
result = sol.print_linked_list(result)
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
arr = [1,2,3,4,5]
left = 1
right = 5
expected = [5,4,3,2,1]    

head = sol.create_linked_list(arr)
_ = sol.print_linked_list(head)
result = sol.reverseBetween(head, left, right)
result = sol.print_linked_list(result)
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
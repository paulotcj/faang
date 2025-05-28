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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # correct base 1 indexing to base 0
        left -= 1
        right -= 1
        left_idx : int = left
        right_idx : int = right
        
        #-----------
        one_before_left_target , left_target , right_target, one_after_right_target = self.get_left_in_position(
            head = head, left_idx = left_idx , right_idx = right_idx) # left end is the node before the left target

        self.revert(left_idx = left_idx, right_idx = right_idx, left_target = left_target)
        #-----------


        if one_before_left_target:
            one_before_left_target.next = right_target
        else:
            head = right_target

        if one_after_right_target:
            left_target.next = one_after_right_target
        else:
            left_target.next = None

        
        return head
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def get_left_in_position( self , head : ListNode , left_idx : int, right_idx : int ) -> Tuple[ListNode,ListNode, ListNode, ListNode] :
        curr                    : ListNode = head
        prev                    : ListNode = None
        one_before_left_target  : ListNode = None
        left_target             : ListNode = None
        one_after_right_target  : ListNode = None
        right_target            : ListNode = None

        #-----------------------------------
        for loop_idx in range(right_idx + 1): # plus 1 so we will make right_idx inclusive in the loop
            #-----
            if left_idx == loop_idx:
                one_before_left_target = prev
                left_target = curr
            elif right_idx == loop_idx:
                right_target = curr
                one_after_right_target = curr.next
            #-----

            prev = curr
            curr = curr.next # final loop command
        #-----------------------------------
        
        if right_target == None : 
            right_target = left_target
            one_after_right_target = right_target.next

            
        return (one_before_left_target, left_target , right_target, one_after_right_target)
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def revert( self, left_idx : int , right_idx : int , left_target : ListNode ) -> Tuple[ListNode, ListNode] :
        prev : ListNode = left_target
        curr : ListNode = left_target.next
        temp_next : ListNode = None
        
        #-----------------------------------
        for _ in range(right_idx - left_idx):
            temp_next = curr.next # temp storage
            curr.next = prev # that's what intuitively we want to do

            # now we need to ajust the pointers, it's easy if we think we are shifting things 1 step to the right
            #   so prev will be curr, curr will be next
            prev = curr
            curr = temp_next
        #-----------------------------------

        one_after_right_target : ListNode = curr
        right_target : ListNode = prev
        
        return (one_after_right_target, right_target)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



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
left = 2
right = 4
expected = [1,4,3,2,5]    

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
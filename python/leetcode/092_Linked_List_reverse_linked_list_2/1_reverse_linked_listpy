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
    def reverseBetween( self , head : Optional[ListNode] , left : int , right : int ) -> Optional[ListNode] :
        # correction from base 1 index to base 0 index
        left_idx : int = left - 1
        right_idx : int = right - 1
        
        self.list_arr : List[ListNode] = []
        curr : ListNode = head
        #-----------------------------------
        while curr :
            self.list_arr.append(curr)
            curr = curr.next
        #-----------------------------------        
        
        # this is a tad more complicated, let's have this logic placed into a separate method
        head = self.reverse_list( head = head , left_idx = left_idx , right_idx = right_idx )
        
        return head
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverse_list( self, head : ListNode , left_idx : int , right_idx : int ) -> ListNode :

        # the idea here is that you need to take 1 elements outside the target nodes in
        #   order to fix the links later
        one_before_left : ListNode = self.list_arr[left_idx -1]   if left_idx > 0 else None
        one_after_right : ListNode = self.list_arr[right_idx + 1] if right_idx < len(self.list_arr) - 1 else None
        left_target  : ListNode = self.list_arr[left_idx]
        right_target : ListNode = self.list_arr[right_idx]
                    
        curr        : ListNode = self.list_arr[left_idx]
        prev        : ListNode = one_after_right
        temp_next   : ListNode = None
        
        #-----------------------------------
        while curr is not None and curr is not one_after_right : 
            temp_next = curr.next # save this relationship, it will be necessary later
            curr.next = prev # intuitively that's what we want to do
            
            # now we start to reposition the pointers. think of it as moving
            #  everything 1 step to the right, prev assumes the value of curr
            #  curr assumes the value of temp_next
            prev = curr
            curr = temp_next
        #-----------------------------------
        
        if one_before_left : 
            one_before_left.next = right_target
        else:
            head = right_target
            
        return head
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
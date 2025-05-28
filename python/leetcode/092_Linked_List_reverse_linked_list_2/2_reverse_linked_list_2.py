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
    def reverseBetween2( self , head : Optional[ListNode] , left : int , right : int ) -> Optional[ListNode] :
        pass
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # correct base 1 indexing to base 0
        left -= 1
        right -= 1
        
        #-----------
        left_end , curr  = self.get_left_in_position(head, left)
        start : ListNode = curr #used to fix the final connection
        #-----------
        prev , curr = self.revert(left, right, curr)
        #-----------
        if left_end:
            left_end.next = prev
        else:
            head = prev

        start.next = curr
        #-----------
        return head
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def get_left_in_position( self , head : ListNode , left : int ) -> Tuple[ListNode , ListNode] :
        curr : ListNode = head
        left_end : ListNode = None
        
        #-----------------------------------
        for x in range( left ): # loop to find the right position for the left_end
            left_end = curr
            curr = curr.next
        #-----------------------------------
            
        return (left_end, curr)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def revert( self, left : int , right : int , curr : ListNode ) -> Tuple[ListNode, ListNode] :
        prev : ListNode = curr
        curr : ListNode = curr.next
        temp : ListNode = None
        
        #-----------------------------------
        for x in range(right - left):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #-----------------------------------
        return (prev, curr)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


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
# exit()

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
exit()

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
#problem: https://leetcode.com/problems/reverse-linked-list/
from typing import Optional, List, Tuple
#-------------------------------------------------------------------------
class ListNode:
    #-------------------------------------------------------------------------
    def __init__( self , value : int , next : Optional['ListNode'] = None ) -> None :
        self.value = value
        self.next = next
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
            curr = ListNode(value = val)
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
            return_list.append(curr.value)
            curr = curr.next
        #-----------------------------------
            
        return return_list
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseList( self, head : Optional[ListNode] ) -> Optional[ListNode] :
        prev : ListNode = None
        curr : ListNode = head
        
        buffer : Optional[Tuple[ListNode, ListNode, ListNode]] = None
        
        # curr.next is updated with prev
        # prev is updated with curr
        # curr is updated with curr.next
        #-----------------------------------
        while curr : 
            buffer = (prev, curr, curr.next)
            
            curr.next = buffer[0] # current.next points to prev
            curr = buffer[2]      # curr now assumes curr.next
            prev = buffer[1]      # prev assumes curr
        #-----------------------------------
        
        # at this point curr is None, meaning the actual pointer was last set to prev
        return prev
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('----------------------------')
sol = Solution()
input_arr = [1,2,3,4,5,6,7,8,9]
expected = [9,8,7,6,5,4,3,2,1]

linked_list_head = sol.create_linked_list(input_arr)

sol.print_linked_list(linked_list_head)

result = sol.reverseList(linked_list_head)
result = sol.print_linked_list(result)
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
input_arr = [1,2,3,4,5]
expected = [5,4,3,2,1]

linked_list_head = sol.create_linked_list(input_arr)

sol.print_linked_list(linked_list_head)

result = sol.reverseList(linked_list_head)
result = sol.print_linked_list(result)
print(f'Is the result correct? { result == expected}')









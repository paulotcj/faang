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
        self.list_arr = self.pre_process_list(head = head)
        # correction from base 1 index to base 0 index:
        left -= 1
        right -= 1
        
        head = self.reverse_list(head = head, idx_left = left, idx_right = right)
        return head
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pre_process_list( self , head : ListNode) -> List[ListNode] :
        list_arr : List[ListNode] = []
        curr : ListNode = head
        #-----------------------------------
        while curr:
            list_arr.append(curr)
            curr = curr.next
        #-----------------------------------
        return list_arr
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverse_list( self, head : ListNode, idx_left : int , idx_right : int ) -> ListNode :
        curr : ListNode = self.list_arr[idx_left]
        prev : ListNode = None
        temp_next : ListNode = None
        
        # the idea here is that you need to take 1 elements outside the target nodes in
        #   order to fix the links later
        node_left_minus_1 : ListNode = None
        node_right_plus_1 : ListNode = None
        
        if idx_left > 0 :
            node_left_minus_1 = self.list_arr[idx_left - 1]
            
        if idx_right < len( self.list_arr ) - 1 :
            node_right_plus_1 = self.list_arr[ idx_right + 1 ]
            prev = node_right_plus_1 # almost forgot - remember if we are going to flip this must be placed here
        
        #-----------------------------------
        while curr is not None and curr is not node_right_plus_1:
            temp_next = curr.next # save this relationship, it will be necessary later
            curr.next = prev # intuitively that's what we want to do
            
            # now we start to reposition the pointers. think of it as moving
            #  everything 1 step to the right, prev assumes the value of curr
            #  curr assumes the value of temp_next
            prev = curr 
            curr = temp_next
        #-----------------------------------
        
        if node_left_minus_1:
            node_left_minus_1.next = prev
        else: head = prev
            
        return head
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
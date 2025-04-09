#problem: https://leetcode.com/problems/reverse-linked-list-ii/description/
from typing import Optional, List, Tuple
#-------------------------------------------------------------------------
class ListNode:
    #-------------------------------------------------------------------------
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def create_linked_list(self, arr : List[int]) -> ListNode:
        head : ListNode = None
        curr : ListNode = None

        for i , v in enumerate(arr):
            if i == 0:
                head = ListNode(v)
                curr = head
            else:
                curr.next = ListNode(v)
                curr = curr.next
        return head
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def print_linked_list(self, head: ListNode) -> List[int]:
        curr : ListNode = head
        list : List[int] = []
        while curr != None:
            list.append(curr.val)
            curr = curr.next

        print(list)
        return list 
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def get_in_position(self, head: ListNode, left: int) -> (ListNode, ListNode):
        #-----------
        #Get in position - curr is always one node to the right of the left_end, even if it's None
        curr : ListNode = head
        prev : ListNode = None #this will always be one node to the left of curr, or in other words, (left - 1)

        for x in range(left-1):
            prev = curr
            curr = curr.next
        #-----------
        left_end : ListNode = prev
        starting_node : ListNode = curr
        return left_end, starting_node  
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def revert(self, left: int, right: int, left_end: ListNode, starting_node: ListNode)-> ListNode:
 
        prev : ListNode = None
        curr : ListNode = starting_node
        next : ListNode = curr.next

        for x in range(right - left + 1):
            curr.next = prev
            prev = curr
            curr = next
            if next: 
                next = next.next
        
        #----------
        # Imagine an list: [1 -> 2 -> 3 -> 4 -> 5], and we want to reverse from 2 to 4.
        # we start with: left_end = 1, head = 2
        # and at the end we have: left_end = 1, head = 2, prev = 4, curr = 5, next = None
        # we need to connect left_end (1) to prev (4), and head (2) to curr (5)
        #----------
        # making clear names
        new_head : ListNode = prev
        new_tail : ListNode = starting_node
        right_end : ListNode = curr
        #----------
        # fix the possible connection with left_end and the new_head
        if left_end:    
            left_end.next = new_head
        else:
            left_end = new_head
        #----------
        # fix the possible connection with the right_end and the new_tail
        new_tail.next = right_end
        #----------
            
        return left_end
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #-----------
        left_end, starting_node = self.get_in_position(head, left)
        #-----------
        new_left_end = self.revert(left, right, left_end, starting_node)
        #-----------
        #left_end is none when the left side of the selection start at the very beginning of the list
        if not left_end:
            head = new_left_end
        
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
# exit()

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
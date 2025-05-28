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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: if the list is empty or no need to reverse
        if not head or left == right:
            return head

        # Create a dummy node to simplify edge cases (e.g., reversing from head)
        dummy: ListNode = ListNode(0, head)
        prev: ListNode = dummy

        # Move prev to the node before the 'left' position
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing from 'left' to 'right'
        reverse_prev: ListNode = prev
        curr: ListNode = prev.next
        prev_node: Optional[ListNode] = None

        # Reverse the sublist
        for _ in range(right - left + 1):
            next_node: Optional[ListNode] = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        # Connect the reversed sublist back to the list
        reverse_prev.next.next = curr  # Tail of reversed sublist points to the node after 'right'
        reverse_prev.next = prev_node  # Node before 'left' points to new head of reversed sublist

        return dummy.next
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
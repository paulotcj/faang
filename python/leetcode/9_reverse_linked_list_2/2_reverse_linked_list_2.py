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
        left_end : ListNode = None #this will always be one node to the left of curr, or in other words, (left - 1)

        for x in range(left-1):
            left_end = curr
            curr = curr.next
        #-----------

        return curr, left_end        
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def revert(self, left: int, right: int, curr: ListNode)-> (ListNode, ListNode):
        prev : ListNode = curr
        curr = curr.next
        temp : ListNode = None
        #---
        for x in range(right - left):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #---
        return prev, curr
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #-----------
        curr, left_end = self.get_in_position(head, left)
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


# print('----------------------------')
# sol = Solution()
# arr = [3,5]
# left = 1
# right = 2
# expected = [5,3]  


# head = sol.create_linked_list(arr)
# _ = sol.print_linked_list(head)
# result = sol.reverseBetween(head, left, right)
# result = sol.print_linked_list(result)
# # print(f'result: {result}')
# print(f'Is the result correct? { result == expected}')
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
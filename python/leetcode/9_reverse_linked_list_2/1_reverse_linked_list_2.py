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
    def preProcessList(self, head: ListNode, left: int, right: int) -> None:
        list_arr : List[ListNode] = []

        curr: ListNode = head
        i = 0
        while curr != None:
            list_arr.append(curr)

            curr = curr.next
            i += 1

        return left - 1 , right - 1, list_arr
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseList(self, head: ListNode, idx_left: int, idx_right: int, list_arr: List[ListNode]) -> ListNode:
        curr: ListNode = list_arr[idx_left]
        prev: ListNode = None
        temp: ListNode = None

        left_end : ListNode = None
        right_end : ListNode = None

        if idx_left is not None and idx_left > 0:
            left_end = list_arr[idx_left - 1]
            
        
        if idx_right is not None and idx_right < len(list_arr) - 1:
            right_end = list_arr[idx_right + 1]
            prev = right_end

        while curr != None and curr != right_end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if left_end:
            left_end.next = prev
        else: head = prev

        return head
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx_left, idx_right, list_arr = self.preProcessList(head, left, right)
        head = self.reverseList(head, idx_left, idx_right, list_arr)
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
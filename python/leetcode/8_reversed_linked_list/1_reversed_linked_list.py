#problem: https://leetcode.com/problems/reverse-linked-list/
from typing import Optional, List
#-------------------------------------------------------------------------
class ListNode:
    #-------------------------------------------------------------------------
    def __init__(self, value: int, next: Optional['ListNode'] = None) -> None:
        self.value = value
        self.next = next
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
            list.append(curr.value)
            curr = curr.next

        print(list)
        return list 
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseList2(self, head: ListNode) -> ListNode:
        list_arr : List[ListNode] = []
        curr: ListNode = head

        while curr != None:
            list_arr.append(curr)
            curr = curr.next

        # this means loop from the (len - 1) to 0, with a step of -1.
        for i in range( (len(list_arr) -1) , -1, -1):
            if i == 0:
                list_arr[i].next = None
            else:
                list_arr[i].next = list_arr[i-1]

        if list_arr:
            head = list_arr[-1]
            return head
        else: return None
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseList3(self, head: ListNode) -> ListNode:
        curr: ListNode = head
        prev:ListNode = None
        temp:ListNode = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    #-------------------------------------------------------------------------
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev:ListNode = None
        curr:ListNode = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('----------------------------')
sol = Solution()
arr = [1,2,3,4,5,6,7,8,9]
expected = [9,8,7,6,5,4,3,2,1]
linked_list_head = sol.create_linked_list(arr)
sol.print_linked_list(linked_list_head)
result = sol.reverseList(linked_list_head)
result = sol.print_linked_list(result)
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')






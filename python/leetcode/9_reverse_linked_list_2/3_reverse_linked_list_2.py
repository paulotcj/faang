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

        return prev, curr     
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def revert(self, left: int, right: int, curr: ListNode)-> (ListNode, ListNode):
        if curr == None: return None, None
        prev : ListNode = None
        next : ListNode = None if curr == None else curr.next
        
        #---
        cnt_loop = right - left
        for x in range(cnt_loop):
            curr.next = prev
            prev = curr
            curr = next
            if next: 
                next = next.next            

        #---
        return prev, curr
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #-----------
        left_end, curr = self.get_in_position(head, left)
        start : ListNode = curr #used to fix the final connection
        #-----------
        prev , curr = self.revert(left, right, curr)
        #-----------
        if left_end:
            left_end.next = curr
        else:
            head = curr

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
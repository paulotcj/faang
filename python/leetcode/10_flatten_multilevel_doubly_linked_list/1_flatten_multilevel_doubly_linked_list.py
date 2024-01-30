#problem: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list

#-------------------------------------------------------------------------
from typing import Optional


class Node:
    #-------------------------------------------------------------------------
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
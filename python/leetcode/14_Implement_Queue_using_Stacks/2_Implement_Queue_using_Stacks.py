#problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
from typing import List, Dict

#-------------------------------------------------------------------------
class MyQueue:
    #-------------------------------------------------------------------------
    def __init__(self):
        self.s_in = []
        self.s_out = []
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def move_if_stack_out_is_empty(self):
        if not self.s_out:
            while self.s_in:
                self.s_out.append(self.s_in.pop())
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def push(self, x: int) -> None:
        self.s_in.append(x)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop(self) -> int:
        self.move_if_stack_out_is_empty()
        return self.s_out.pop()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def peek(self) -> int:
        self.move_if_stack_out_is_empty()
        return self.s_out[-1]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def empty(self) -> bool:
        if self.s_in or self.s_out:
            return False
        return True
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
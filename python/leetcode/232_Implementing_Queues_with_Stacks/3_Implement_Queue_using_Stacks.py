#problem: https://leetcode.com/problems/implement-queue-using-stacks/description/
from typing import List, Dict


#-------------------------------------------------------------------------
class MyQueue:
    #-------------------------------------------------------------------------
    def __init__(self) -> None:
        # stack_in is used for enqueue (push) operations
        # stack_out is used for dequeue (pop/peek) operations
        self.stack_in: list[int] = []
        self.stack_out: list[int] = []
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def push(self, x: int) -> None:
        # Always push new elements onto stack_in
        self.stack_in.append(x)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop(self) -> int:
        # If stack_out is empty, move all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Pop from stack_out, which represents the front of the queue
        return self.stack_out.pop()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def peek(self) -> int:
        # Ensure stack_out has the current front element
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Peek at the top of stack_out
        return self.stack_out[-1]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return not self.stack_in and not self.stack_out
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
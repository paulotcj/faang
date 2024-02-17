#problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        scheduled_for_removal = []
        for i, v in enumerate(s):
            if v == '(': #we don't know anything yet
                stack.append(i)
            elif v == ')': #when closing we need to check whether the stack is empty and if not try to close it
                if stack:
                    stack.pop()
                else:
                    scheduled_for_removal.append(i)

        #we need to remove the remaining elements in the stack
        scheduled_for_removal.extend(stack)
        while scheduled_for_removal:
            i = scheduled_for_removal.pop()
            s = s[:i] + s[i+1:] #this is: get the string from 0 to i (being i not included) and then from i+1 until the end
            
        return s
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
print('----------------------------')
sol = Solution()
input = ")ab(c)d"
expected = "ab(c)d"
result = sol.minRemoveToMakeValid(input)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')

print('----------------------------')
sol = Solution()
input = "))(("
expected = ""
result = sol.minRemoveToMakeValid(input)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')



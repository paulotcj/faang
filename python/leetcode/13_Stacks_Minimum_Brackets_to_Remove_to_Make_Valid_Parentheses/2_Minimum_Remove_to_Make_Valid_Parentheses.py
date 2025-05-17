#problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s) #convert to list to be able to modify it
        stack = []
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            elif v == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            i = stack.pop()
            s[i] = ''
            
        return ''.join(s)
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



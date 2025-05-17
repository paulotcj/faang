#problem: https://leetcode.com/problems/valid-parentheses/description/

from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValid(self, s: str) -> bool:
        char_stack : List[str] = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                char_stack.append(c)
            else:
                if not char_stack:
                    return False
                elif c == ')' and char_stack[-1] != '(':
                    return False
                elif c == '}' and char_stack[-1] != '{':
                    return False
                elif c == ']' and char_stack[-1] != '[':
                    return False
                else:
                    char_stack.pop()
        
        return True if not char_stack else False
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
print('----------------------------')
sol = Solution()
s = "()[]{}"
expected = True
result = sol.isValid(s)
# print(f'expected: {expected}')
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('----------------------------')
sol = Solution()
s = "()[{}"
expected = False
result = sol.isValid(s)
# print(f'expected: {expected}')
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')

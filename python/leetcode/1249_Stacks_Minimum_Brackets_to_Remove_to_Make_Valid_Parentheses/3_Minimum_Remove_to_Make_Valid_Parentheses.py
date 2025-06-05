#problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minRemoveToMakeValid(self, s: str) -> str:

        # First pass: Remove invalid ')'
        result: list[str] = []
        open_count: int = 0
        #-----------------------------------
        for char in s:
            #-----
            if char == '(':
                open_count += 1
                result.append(char)
            elif char == ')':
                #-----
                if open_count > 0:
                    open_count -= 1
                    result.append(char)
                # else: skip this ')'
                #-----
            else:
                result.append(char)
            #-----
        #-----------------------------------

        # Second pass: Remove extra '(' from the end
        final_result: list[str] = []
        open_to_remove: int = 0
        #-----------------------------------
        for char in reversed(result):
            #-----
            if char == '(' and open_count > 0:
                open_count -= 1  # Remove this unmatched '('
                continue
            #-----
            final_result.append(char)
        #-----------------------------------

        # The result is built in reverse order, so reverse it back
        return ''.join(reversed(final_result))
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


print('----------------------------')
sol = Solution()
input = ""
expected = ""
result = sol.minRemoveToMakeValid(input)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
input = "lee(t(c)o)de)"
expected = "lee(t(c)o)de"
result = sol.minRemoveToMakeValid(input)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')



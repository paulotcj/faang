#problem: https://leetcode.com/problems/valid-parentheses/description/

from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValid( self , s : str ) -> bool :
        stack : list[str] = []
        opening_brackets : dict[str,bool] = { '(': True, '{':True, '[':True}
        bracket_map : dict[str, str] = {')': '(', '}': '{', ']': '['}
        
        #-----------------------------------
        for c in s:
            #-----
            if c in opening_brackets: # it's an opening bracket char, push to the stack
                stack.append(c)
            elif c in bracket_map : # it's a closing bracket char, check for matching opening
                #-----
                if not stack or stack[-1] != bracket_map[c] : # stack is empty or the char does not match
                    return False
                #-----
                stack.pop()
            #-----
        #-----------------------------------
            
            
        # at this point everything is correct, check if the stack is empty and if so, return true
        return_result : bool = not stack
        return return_result
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

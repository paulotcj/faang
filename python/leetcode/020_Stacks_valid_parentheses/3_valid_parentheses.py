#problem: https://leetcode.com/problems/valid-parentheses/description/

from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValid2( self , s : str ) -> bool :
        stack : list[str] = []
        bracket_map : dict[str,str] = { ')':'(' , '}':'{' , ']':'[' }
        
        for c in s:
            #-----
            if c in bracket_map.values(): # it's an opening bracket char, push to the stack
                stack.append(c)
            elif c in bracket_map : # it's a closing bracket char, check for matching opening
                #-----
                if not stack or stack[-1] != bracket_map[c] : # stack is empty or the char does not match
                    return False
                
                stack.pop()
                #-----
            #-----
            
            
                    
        
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack : list[str] = []
        # Mapping of closing to opening brackets
        bracket_map : dict[str, str] = {')': '(', '}': '{', ']': '['}

        for char in s :
            if char in bracket_map.values():
                # If it's an opening bracket, push to stack
                stack.append(char)
            elif char in bracket_map:
                # If it's a closing bracket, check for matching opening
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # Invalid character (should not happen per constraints)
                return False

        # If stack is empty, all brackets matched correctly
        return not stack
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

#problem: https://leetcode.com/problems/valid-parentheses/description/

from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValid( self , s : str ) -> bool :
        char_stack : list[str] = []
        
        #-----------------------------------
        for curr_char in s:
            if curr_char == '(' or curr_char == '{' or curr_char == '[' :
                char_stack.append(curr_char)
            else:
                
                if not char_stack : return False # trying to pop an empty stack - return False
                elif curr_char == ')' and char_stack[-1] != '(' : return False # tring to close a parenthesis and the prev char in the stack is not an opening parenthesis - return false
                elif curr_char == ']' and char_stack[-1] != '[' : return False # tring to close a square brackets and the prev char in the stack is not an opening square brackets - return false
                elif curr_char == '}' and char_stack[-1] != '{' : return False # trying to close a curly brackets and the prev char in the stack is not an opening curly brackets - return false
                
                # else the char is correct therefore pop the stack
                char_stack.pop()
        #-----------------------------------
        
        # until now no mismatch was found, however it's possible that the stack still has
        #  chars in it. If so, the string did not matched all its parenthesis or brackets
        return_result : bool = False if char_stack else True
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

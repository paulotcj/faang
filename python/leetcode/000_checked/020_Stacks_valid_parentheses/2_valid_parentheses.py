#problem: https://leetcode.com/problems/valid-parentheses/description/

from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValid( self , s : str ) -> bool :
        char_stack : list[str] = []
        dict_opening : dict[str,str] = { '(':')' , '{':'}' , '[':']' }
        dict_closing : dict[str,str] = { ')':'(' , '}':'{' , ']':'[' }
        
        #-----------------------------------
        for c in s :
            #-----
            if c in dict_opening.keys() : 
                char_stack.append(c)
                continue
            elif not char_stack : return False # not an opening char, and if the stack is empty, return False
            #-----
            #-----
            # c is a closing char, then whatever is in the stack in order to be valid must be
            #   its opening counter part. if so, continue to process, if not return false
            check_if_valid_opening : str = char_stack[-1] 
            potential_closing_char : str = c
            if check_if_valid_opening == dict_closing[potential_closing_char] :
                char_stack.pop() # matching opening and closing chars. pop stack and continue to process
            else:
                return False # chars didn't match
            #-----
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

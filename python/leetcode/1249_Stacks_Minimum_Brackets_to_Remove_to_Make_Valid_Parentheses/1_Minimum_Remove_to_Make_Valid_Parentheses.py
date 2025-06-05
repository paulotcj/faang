#problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minRemoveToMakeValid( self , s : str ) -> str :
        stack_opening : list[str] = []
        scheduled_for_removal : list[str] = []
        #-----------------------------------
        for loop_idx , loop_val in enumerate(s) :
            #-----
            if loop_val == '(' : # we don't know anything yet, just push the char idx to the stack
                stack_opening.append(loop_idx)
            elif loop_val == ')' : # trying to close, check the stack
                #-----
                if stack_opening: stack_opening.pop()
                else: scheduled_for_removal.append(loop_idx)
                #-----
            #-----  
        #-----------------------------------
        '''at this point the scheduled_for_removal might be: '' , ( , or ((...
        And the stack_opening might be: '' , ) , or ))...
        All of these occurences are mismatching. And it's necessary to remove the least number of 
        parenthesis to make the string valid, so: remove them all'''
        
        scheduled_for_removal.extend(stack_opening) # merge them for easier manipulation
        
        #-----------------------------------
        while scheduled_for_removal:
            remove_idx : int = scheduled_for_removal.pop()
            s = s[0:remove_idx] + s[remove_idx+1:] #this is: get the string from 0 to remove_idx (being remove_idx not included) and then from remove_idx+1 until the end
        #-----------------------------------
     
        # string is now clean
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



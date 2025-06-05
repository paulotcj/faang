#problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minRemoveToMakeValid( self , s : str ) -> str :
        stack : list[str] = []
        schedule_for_removal : list[str] = []
        #-----------------------------------
        for loop_idx , loop_val in enumerate(s) :
            #-----
            if loop_val == '(' : # we don't know anything yet, just push the char idx to the stack
                stack.append(loop_idx)
            elif loop_val == ')' : # trying to close, check the stack
                #-----
                if stack: stack.pop()
                else: schedule_for_removal.append(loop_idx)
                #-----
            #-----  
        #-----------------------------------
        '''at this point the schedule_for_removal might be: empty, or with one or more closing
        parenthesis. And the stack might be: empty, or contain one or more opening parenthesis
        '''
        
        
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        scheduled_for_removal = []
        #-----------------------------------
        for i, v in enumerate(s):
            #-----
            if v == '(': #we don't know anything yet
                stack.append(i)
            elif v == ')': #when closing we need to check whether the stack is empty and if not try to close it
                #-----
                if stack: stack.pop()
                else: scheduled_for_removal.append(i)
                #-----
            #-----
        #-----------------------------------

        #we need to remove the remaining elements in the stack
        scheduled_for_removal.extend(stack)
        #-----------------------------------
        while scheduled_for_removal:
            i = scheduled_for_removal.pop()
            s = s[:i] + s[i+1:] #this is: get the string from 0 to i (being i not included) and then from i+1 until the end
        #----------------------------------- 
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



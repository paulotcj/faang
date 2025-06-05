#problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def minRemoveToMakeValid( self , s : str ) -> str :
        list_char : list[str] = list(s) #convert to list to be able to modify it
        stack : list[str] = []
        
        #-----------------------------------
        for loop_idx, loop_val in enumerate(list_char) :
            #-----
            if loop_val == '(' : stack.append(loop_idx)
            elif loop_val == ')':
                #-----
                if stack : stack.pop()
                else : # invalid closing parenthesis
                    list_char[loop_idx] = '' # no need to use lists to remember where to remove from, just remove it
                #-----
            # else : regular char, nothing to do
            #-----
        #-----------------------------------
        
        #-----------------------------------
        while stack:
            i = stack.pop()
            list_char[i] = ''
        #-----------------------------------
        
        return_string : str = ''.join(list_char)
        return return_string
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



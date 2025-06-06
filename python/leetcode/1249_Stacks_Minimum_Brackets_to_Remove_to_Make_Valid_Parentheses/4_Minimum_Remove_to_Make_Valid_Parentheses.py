#problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/


#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def minRemoveToMakeValid( self , s : str ) -> str :
        temp_result : list[str] = []
        open_count : int = 0
        
        # First pass: Remove invalid ')'
        #-----------------------------------
        for char in s:
            #-----
            if char == '(' :                # opening parenthesis - can't assume anything right now
                open_count += 1             # increase the counter and...
                temp_result.append(char)  # add the char to the temporary result list
            elif char == ')' :                 # closing char - at this time we can figure out certain things
                #-----
                if open_count > 0 :            # if we had at least one open parenthesis before, subtract it
                    open_count -= 1            # subtract it
                    temp_result.append(char) # and add the the list of valid chars
                else: #this char is a mismatched ) - just ignore it
                    pass
                #-----
            else: # regular chars - just append to the temporary solution
                temp_result.append(char)
            #-----
        #-----------------------------------
        
        ''' up to this point umatched closing parenthesis ')' were removed. but the temporary solution still
        may contain unmatched opening parenthesis '(' .  Another important tidbit is that, since the 
        parenthesis were being matched left to right, and at this point some opening parenthesis might still
        be unmatched, that means they are to the right of the string.'''
        
        # Second pass: Remove extra '(' from the end        
        #-----------------------------------
        for for_idx in range(len(temp_result) - 1, -1 , -1) : 
            if temp_result[for_idx] == '(' and open_count > 0 :
               temp_result[for_idx] = ''
               open_count -= 1
            elif open_count == 0: break 
        #-----------------------------------
        
        return_result : str = ''.join(temp_result)
        return return_result   
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

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
input = ")ab(c)d"
expected = "ab(c)d"
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



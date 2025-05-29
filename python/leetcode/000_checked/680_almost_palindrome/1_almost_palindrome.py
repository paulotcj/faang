#problem: https://leetcode.com/problems/valid-palindrome-ii/description/


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def validPalindrome( self , s : str ) -> bool :
        if s == s[::-1] : return True # simple palindrome
        
        # --- anything below here we know there's a mismatch somewhere in the string ---
        low_idx : int = 0
        high_idx : int = len(s) -1
        
        #-----------------------------------
        while low_idx < high_idx :
            #--------
            if s[low_idx] != s[high_idx] : # mismatched, need to check moving 1 from low and 1 from high
                
                # step 1 - the mismatch might be at the low_idx. in this case we simply remove the char
                #   at low_idx and compare against its reversed string, as if that the problematic char
                #   then it should be solved
                removed_char_at_low_idx : str = s[0:low_idx] + s[low_idx+1:] # copies the entire string but skip the char at low_idx
                if removed_char_at_low_idx == removed_char_at_low_idx[::-1] : return True # found the mismatching char, the string matches now, return true
                
                # step 2 -  potentially the mismatched char is at the high_idx side. let's remove it and
                #   compare the string against its reversed
                removed_char_at_high_idx : str = s[0:high_idx] + s[high_idx+1:] # same thing for high_idx
                if removed_char_at_high_idx == removed_char_at_high_idx[::-1] : return True # found the mismathing char, the string matches now, return true
                
                # from the original string, if you removed the char from low_idx, created a substring without
                #   that char, and it didn't match. Then you repeated the process using the original string
                #   again, but this time removing the char from high_idx, and it still doesn't match, it
                #   means we have more than 1 mismatch, so the string is not 'almost' palindrome.
                #   return false then
                return False
            #--------
            low_idx += 1
            high_idx -= 1
        #-----------------------------------
        # this point should not be reached
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('----------------------------')
sol = Solution()
s = "aba"
expected = True
result = sol.validPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "abca"
expected = True
result = sol.validPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "abc"
expected = False
result = sol.validPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



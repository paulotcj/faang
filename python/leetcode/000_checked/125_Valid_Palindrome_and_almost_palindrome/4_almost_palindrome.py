#problem: https://leetcode.com/problems/valid-palindrome-ii/description/


#-------------------------------------------------------------------------   
class Solution:
    #-------------------------------------------------------------------------
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: #valid palindrome
            return True
        else: #check for almost palindrome
            low_idx:int = 0
            high_idx:int = len(s) - 1

            while low_idx < high_idx:
                
                #---
                if s[low_idx] != s[high_idx]: #not matching
                    

                    str_skipping_low:str = s[0:low_idx] + s[low_idx+1:] #copies the entire string but skip the char at low_idx
                    str_skipping_high:str = s[0:high_idx] + s[high_idx+1:] #copies the entire string but skip the char at low_idx
                    
                    #now with 2 possible strings to check if they are palindromes we do the same procedure
                    # we compare the string with its reverse
                    if str_skipping_low == str_skipping_low[::-1] or str_skipping_high == str_skipping_high[::-1]: 
                        return True
                    else: 
                        return False
                #---
                
                #chars match, move to the next pair
                low_idx += 1
                high_idx -= 1 
            # end while
        # end if   
    #-------------------------------------------------------------------------

    
#-------------------------------------------------------------------------


print('----------------------------')
sol = Solution()
s = "abca"
expected = True
result = sol.validPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



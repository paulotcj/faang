#problem: https://leetcode.com/problems/valid-palindrome-ii/description/


        
        
class Solution:
    
    #-------------------------------------------------------------------------
    def isPalindrome(self, s: str, low_idx: int, high_idx: int) -> bool:
        while( low_idx < high_idx ):
            
            low_char = s[low_idx]
            high_char = s[high_idx]

            if low_char != high_char:
                return False
            
            low_idx += 1
            high_idx -= 1
        #-------------
        return True
    #-------------------------------------------------------------------------  
    
    #-------------------------------------------------------------------------
    def validPalindrome(self, s: str) -> bool:
        low_idx: int = 0
        high_idx: int = len(s) - 1

        while( low_idx < high_idx ):
            low_char = s[low_idx]
            high_char = s[high_idx]

            #---
            if low_char != high_char:
                test_low = self.isPalindrome(s, low_idx + 1, high_idx)
                if test_low: return True
                
                test_high = self.isPalindrome(s, low_idx, high_idx - 1)
                if test_high: return True
                
                return False
            #---
            low_idx += 1
            high_idx -= 1
        #-------------
        return True
    #-------------------------------------------------------------------------
    
#-------------------------------------------------------------------------


print('----------------------------')
sol = Solution()
s = "abca"
expected = True
result = sol.validPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



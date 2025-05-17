# problem: https://leetcode.com/problems/valid-palindrome/

#-------------------------------------------------------------------------
class Solution:

    #-------------------------------------------------------------------------
    def isPalindrome(self, s: str) -> bool:
        low_idx: int = 0
        high_idx: int = len(s) - 1

        while( low_idx < high_idx ):
            #---
            low_char = s[low_idx]
            if not low_char.isalnum():
                low_idx += 1
                continue
            low_char = low_char.lower()
            #---
            high_char = s[high_idx]
            if not high_char.isalnum():
                high_idx -= 1
                continue
            high_char = high_char.lower()
            #---
            if low_char != high_char:
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
s = "A man, a plan, a canal: Panama"
expected = True
result = sol.isPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



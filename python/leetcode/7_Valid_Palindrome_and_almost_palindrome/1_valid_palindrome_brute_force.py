# problem: https://leetcode.com/problems/valid-palindrome/

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isPalindrome(self, s: str) -> bool:

        s = ''.join( ch for ch in s if ch.isalnum() ).lower()
        new_str : str = s[::-1]

        if new_str == s:
            return True
        return False
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    



print('----------------------------')
sol = Solution()
s = "A man, a plan, a canal: Panama"
expected = True
result = sol.isPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



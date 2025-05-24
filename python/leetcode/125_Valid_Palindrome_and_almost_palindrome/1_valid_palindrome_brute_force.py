# https://leetcode.com/problems/valid-palindrome/

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isPalindrome( self, s : str ) -> bool :
        str_lower_case_alphanum : str = ''.join( 
            char.lower() 
            for char in s 
            if char.isalnum()
        )
        
        reversed_str : str = str_lower_case_alphanum[::-1]
        
        if reversed_str == str_lower_case_alphanum: return True
        else: return False
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    



print('----------------------------')
sol = Solution()
s = "A man, a plan, a canal: Panama"
expected = True
result = sol.isPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
s = "race a car"
expected = False
result = sol.isPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = " "
expected = True
result = sol.isPalindrome(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



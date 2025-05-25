# problem: https://leetcode.com/problems/valid-palindrome/

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isPalindrome( self, s : str ) -> bool :
        low_idx : int = 0
        high_idx : int = len(s) - 1
        
        #-----------------------------------
        while low_idx < high_idx :
            #---------------
            while low_idx < high_idx and s[low_idx].isalnum() == False :
                low_idx += 1
            #---------------
            while low_idx < high_idx and s[high_idx].isalnum() == False :
                high_idx -= 1
            #---------------
            
            if s[low_idx].lower() != s[high_idx].lower() : return False
            
            low_idx += 1
            high_idx -= 1
        #-----------------------------------
        
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






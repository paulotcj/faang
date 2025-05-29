#problem: https://leetcode.com/problems/valid-palindrome-ii/description/

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def validPalindrome( self , s : str ) -> bool :
        self.input_str : str = s
        low_idx : int = 0
        high_idx : int = len(s) - 1
        
        #-----------------------------------
        while low_idx < high_idx :
            
            #---------
            if s[low_idx] != s[high_idx] : # mismatch
                # skips the char at low_idx
                test_low_idx : bool = self.check_inside_palindrome( low_idx = low_idx + 1, high_idx = high_idx )
                if test_low_idx == True: return True
                
                # skips the char at high_idx
                test_high_idx : bool = self.check_inside_palindrome( low_idx = low_idx , high_idx = high_idx -1 )
                if test_high_idx == True : return True
                
                # None of them worked, so there's must be another mismatched char, return false
                return False
            #---------
                
            low_idx += 1
            high_idx -= 1
        #-----------------------------------
        
        # if this part is reached, that means it looped through the string, the mismatch if wasn't
        #   triggered, so no mismatch, therefore retur True
        return True
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def check_inside_palindrome( self, low_idx : int, high_idx : int ) -> bool :
        #-----------------------------------
        while low_idx < high_idx :
            if self.input_str[low_idx] != self.input_str[high_idx] : return False
            low_idx += 1
            high_idx -= 1
        #-----------------------------------
        return True
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



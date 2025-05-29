#problem: https://leetcode.com/problems/backspace-string-compare/description/


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def backspaceCompare(self, s : str , t : str) -> bool :
        idx_s : int = len(s) - 1
        idx_t : int = len(t) - 1
        
        #-----------------------------------
        while idx_s >= 0 or idx_t >= 0:
            idx_s : int = self.next_valid_char_index( input_str = s, idx = idx_s )
            idx_t : int = self.next_valid_char_index( input_str = t, idx = idx_t )
            
            if idx_s >= 0 and idx_t >= 0: # both strings have chars left to compare
                if s[idx_s] != t[idx_t] : 
                    return False # strings don't match
            elif idx_s >= 0 or idx_t >= 0: # one of the string still has chars to compare - so a mismatch
                '''one string has characters left, the other doesn't, so a mismatch, remember 
                  next_valid_char_index is supposed to give the next valid index, if we have a 
                  mismatch here, then it's a mismatch'''
                return False
            
            # move the indexes
            idx_s -= 1
            idx_t -= 1
        #-----------------------------------
        # if no mismatch has been found until this point, return True
        return True
        
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def next_valid_char_index(self, input_str : str , idx : int) -> int:
        backspace : int = 0
        
        #-----------------------------------
        while idx >= 0 :
            #------------------
            if input_str[idx] == '#': 
                backspace += 1
            else: # valid char
                if backspace > 0 :
                    backspace -= 1
                else:
                    return idx
            #------------------
            
            idx -= 1
        #-----------------------------------
        return idx
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('----------------------------')
sol = Solution()
s = "a##c"
t = "#a#c"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "a"
t = "aa#a#a#a#a#a#a#a#"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
s = "a"
t = "aa#a"
expected = False
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "nzp#o#g"
t = "b#nzp#o#g"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')  


print('----------------------------')
sol = Solution()
s = "bbbextm"
t = "bbb#extm"
expected = False
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')  



print('----------------------------')
sol = Solution()
s = "ab##"
t = "c#d#"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')  

print('----------------------------')
sol = Solution()
s = "ab#c"
t = "ad#c"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')    

print('----------------------------')
sol = Solution()
s = "a#c"
t = "b"
expected = False
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
s = "y#fo##f"
t = "y#f#o##f"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')





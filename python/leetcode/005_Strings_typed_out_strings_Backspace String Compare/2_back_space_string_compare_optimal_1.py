#problem: https://leetcode.com/problems/backspace-string-compare/description/

from typing import Tuple

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def backspaceCompare(self, s: str, t: str) -> bool:
        idx_s : int = len(s) - 1
        idx_t : int = len(t) - 1
        
        #-----------------------------------
        while idx_s >= 0 or idx_t >= 0:
            idx_s , s_char = self.get_next_char(input_str = s, idx = idx_s)
            idx_t , t_char = self.get_next_char(input_str = t, idx = idx_t)
            
            if s_char != t_char : return False
            
            # print(f's_char  : {s_char}\tt_char     :{t_char}')
            
            # if idx_s >= 0 and idx_t >= 0:
            #     print(f's[idx_s]: {s[idx_s]}\tt[idx_t] : {t[idx_t]}')
            #     print(f'idx_s:{idx_s}\t\tidx_t:{idx_t}')
            # print('---')
            
            idx_s -= 1
            idx_t -= 1
        #-----------------------------------
        
        return True
    #-------------------------------------------------------------------------  
    #------------------------------------------------------------------------- 
    def get_next_char(self, input_str : str, idx : int) -> Tuple[int, str]:
        
        # starting with 1 because we are always going back at least 1 char
        back_space_count : int = 1 
        
        #-----------------------------------
        while idx >= 0 and back_space_count > 0:
            if input_str[idx] == '#' : 
                back_space_count += 1
            else:
                back_space_count -= 1
                # we know it's a char but we might need to clear the backspace. If we
                # run out of chars and there's a pile of leftover backspaces, that's ok
                # but if we have lots of backspaces we need to clear all the available
                # chars
                if back_space_count == 0:
                    return (idx, input_str[idx])            
            idx -= 1
        #-----------------------------------
        
        # at this point we we might be at idx = -1
        return (idx, '')
    #-------------------------------------------------------------------------  

#-------------------------------------------------------------------------

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
s = "a##c"
t = "#a#c"
expected = True
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





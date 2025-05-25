#problem: https://leetcode.com/problems/backspace-string-compare/description/

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def backspaceCompare(self, s : str , t : str) -> bool :
        s_idx : int = len(s) - 1
        t_idx : int = len(t) - 1
        
        #-----------------------------------
        while s_idx >= 0 or t_idx >= 0:
            #-----
            s_idx : int = self.get_next_idx(input_str = s , idx = s_idx)
            t_idx : int = self.get_next_idx(input_str = t , idx = t_idx)
            s_char : str = '' if s_idx < 0 else s[s_idx]
            t_char : str = '' if t_idx < 0 else t[t_idx]
            #-----
            
            if s_char != t_char : return False
            
            s_idx -= 1
            t_idx -= 1
        #-----------------------------------
        
        # we compared everything so far and no mismatch was found, return True
        return True
            
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def get_next_idx(self, input_str : str, idx : int) -> int:
        backspaces : int = 1
        
        #-----------------------------------
        while idx >= 0 and backspaces > 0:
            #-----------------------------------
            if input_str[idx] == '#' : 
                backspaces += 1
            else: #regular char
                backspaces -= 1
                if backspaces == 0: return idx
            #-----------------------------------
            
            idx -= 1 
        #-----------------------------------
                
        return idx # at this point we haven't found a valid char, return the idx (-1)
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





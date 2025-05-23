#problem: https://leetcode.com/problems/backspace-string-compare/description/

from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s : str = self.build_string(str_input = s)
        new_t : str = self.build_string(str_input = t)
        
        result : bool = new_s == new_t
        return result
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def build_string(self, str_input : str) -> str:
        stack : List[str] = []
        
        #-----------------------------------
        for char in str_input:
            if char == '#': # note that we should separate both conditions from below
                if stack: stack.pop() # stack must not be empty to pop
                # else discard '#'
            else: stack.append(char)
        #-----------------------------------
        
        return_obj : str = ''.join(stack)
        return return_obj
        
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





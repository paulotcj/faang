class Solution:
    #-------------------------------------------------------------------------
    def get_next_idx(self, s:str, idx: int) -> int:
        #-----
        backspaces = 0
        while idx >= 0 and (s[idx] == '#' or backspaces > 0):
            backspaces += 1 if s[idx] == '#' else -1
            idx -= 1
        #-----        
        return idx
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_idx, t_idx = len(s) - 1, len(t) - 1

        while s_idx >= 0 or t_idx >= 0:
            #-----
            s_idx = self.get_next_idx(s, s_idx)
            t_idx = self.get_next_idx(t, t_idx)
            #-----
                
            if s_idx == -1 or t_idx == -1:
                return s_idx == -1 and t_idx == -1
            elif s[s_idx] != t[t_idx]:
                return False
            
            s_idx -= 1
            t_idx -= 1
        #--------------
        
        return True
#-------------------------------------------------------------------------


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

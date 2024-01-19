class Solution:
    #-------------------------------------------------------------------------
    def get_next_char(self, s:str, idx:int) -> (int, str):
        back_space_count = 1
        last_seen_char = None
        while back_space_count > 0 and idx >= 0:
            if s[idx] == '#':
                back_space_count += 1
            else:
                back_space_count -= 1
                if back_space_count == 0:
                    last_seen_char = s[idx]
            idx -= 1

        return idx, last_seen_char
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    def backspaceCompare(self, s: str, t: str) -> bool:
        idx_s = len(s) - 1
        idx_t = len(t) - 1

        #-----------
        while idx_s >= 0 or idx_t >= 0:
            idx_s, s_char = self.get_next_char(s, idx_s)
            idx_t, t_char = self.get_next_char(t, idx_t)

            if s_char != t_char:
                return False
        #-----------
        return True
    #-------------------------------------------------------------------------
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

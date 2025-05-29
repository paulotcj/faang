# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from typing import List, Dict, Tuple

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s : str ) -> int :
        begin_substr_idx : int = 0
        max_len : int = 0
        seen : Dict[str, int] = {}
        
        #-----------------------------------
        for curr_idx, curr_char in enumerate(s):
            
            if seen.get(curr_char, -1) >= begin_substr_idx:
                begin_substr_idx : int = seen[curr_char] + 1
                
            seen[curr_char] = curr_idx
            
            # suppose: begin_substr_idx = 2, curr_idx = 7.  Then 7 - 2 = 5
            #  and we want to include the values in the range at idx 2 and idx 7, so with that math
            #  the values selected would be: 2, 3, 4, 5, 6 -> length of 5 but we want to include 7 so
            #  we add +1 to avoid error by 1 and include all elements
            curr_len : int = curr_idx - begin_substr_idx + 1
            max_len : int = max(max_len, curr_len)
        #-----------------------------------
        
        return max_len
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
  
  

print('----------------------------')
sol = Solution()
s = "dvdf"
expected = 3
result = sol.lengthOfLongestSubstring(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}') 
    
print('----------------------------')
sol = Solution()
s = "tmmzuxt"
expected = 5
result = sol.lengthOfLongestSubstring(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "abcabcbb"
expected = 3
result = sol.lengthOfLongestSubstring(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "bbbbb"
expected = 1
result = sol.lengthOfLongestSubstring(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "pwwkew"
expected = 3
result = sol.lengthOfLongestSubstring(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')




        
        
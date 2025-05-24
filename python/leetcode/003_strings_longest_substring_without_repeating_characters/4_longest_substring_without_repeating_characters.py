# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from typing import List, Dict, Tuple

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_seen: dict[str, int] = {}
        max_length: int = 0
        begin_substr_idx: int = 0

        #-----------------------------------
        for curr_idx, curr_char in enumerate(s):
            # If the character is already in the window, move the start
            if curr_char in last_seen and last_seen[curr_char] >= begin_substr_idx:
                begin_substr_idx = last_seen[curr_char] + 1
                
            # Update the last seen index of the character
            last_seen[curr_char] = curr_idx
            # Update the maximum length found so far
            
            max_length = max(max_length, curr_idx - begin_substr_idx + 1)
        #-----------------------------------

        return max_length
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




        
        
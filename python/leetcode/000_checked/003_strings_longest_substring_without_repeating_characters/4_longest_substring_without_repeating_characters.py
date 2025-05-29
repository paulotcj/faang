# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from typing import Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring( self, s : str ) -> int :
        last_seen : Dict[str, int] = {}
        max_len : int = 0
        begin_substr_idx : int = 0
        
        #-----------------------------------
        for curr_idx, curr_char in enumerate(s):
            '''If the character is already in the window, move the start. take for instance: 
            s = 'dvdf'    last_seen = {'d': 0, 'v': 1}        curr:char = d , curr_idx = 2
            begin_substr_idx = 0
            That literally means that we seen this char before when we started to keep track
            of the substring
            '''
            if curr_char in last_seen and last_seen[curr_char] >= begin_substr_idx: 
                begin_substr_idx = last_seen[curr_char] + 1
                
            last_seen[curr_char] = curr_idx # Update the last seen index of the character
            
            curr_len : int = curr_idx - begin_substr_idx + 1
            max_len : int = max(max_len,curr_len)
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




        
        
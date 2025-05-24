# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from typing import Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s : str) -> int:
        self.input_str : str = s
        self.string_dict : Dict[str, int] = {}

        self.max_len : int = 0
        self.low_idx : int = 0
        #-----------------------------------
        for high_idx, _ in enumerate(self.input_str):
            self.have_we_seen_this_char(hight_idx = high_idx)
        #-----------------------------------
        return self.max_len
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def have_we_seen_this_char(self, high_idx: int) -> None:
        
        high_char : str = self.input_str[high_idx]

        #--------------
        if high_char in self.string_dict and self.string_dict[high_char] >= self.low_idx:

            self.low_idx : int = max(self.low_idx, self.string_dict[high_char] + 1)
            self.string_dict[high_char] = high_idx
            
        else:
            self.string_dict[high_char] = high_idx
            self.max_len : int = max(self.max_len, high_idx - self.low_idx + 1)
        #--------------

    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
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




        
        
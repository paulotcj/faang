#problem: https://leetcode.com/problems/backspace-string-compare/description/

from typing import List, Dict, Tuple

class Solution:

    #-------------------------------------------------------------------------
    def have_we_seen_this_char(self, s:str, string_dict: Dict[str, int], 
                               low_idx: int, high_idx: int, max_len: int)-> Tuple[int, int, int]:
        low_v, high_v = s[low_idx], s[high_idx]

        if high_v in string_dict and string_dict[high_v] >= low_idx:

            low_idx = max(low_idx, string_dict[high_v] + 1)
            string_dict[high_v] = high_idx
            
        else:
            string_dict[high_v] = high_idx
            max_len = max(max_len, high_idx - low_idx + 1)

        return low_idx, high_idx, max_len
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        string_dict = {}
        low_idx = 0

        #-------
        for high_idx, _ in enumerate(s):
            low_idx, high_idx, max_len = self.have_we_seen_this_char(s, string_dict, low_idx, high_idx, max_len)
        #-------
        return max_len
    #-------------------------------------------------------------------------

#-------------------------------------------------------------------------
    
print('----------------------------')
sol = Solution()
s = "tmmzuxt"
expected = 5
result = sol.lengthOfLongestSubstring(s)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


# print('----------------------------')
# sol = Solution()
# s = "abcabcbb"
# expected = 3
# result = sol.lengthOfLongestSubstring(s)
# print(f'result: {result}')
# print(f'Is the result correct? { result == expected}')


# print('----------------------------')
# sol = Solution()
# s = "bbbbb"
# expected = 1
# result = sol.lengthOfLongestSubstring(s)
# print(f'result: {result}')
# print(f'Is the result correct? { result == expected}')


# print('----------------------------')
# sol = Solution()
# s = "pwwkew"
# expected = 3
# result = sol.lengthOfLongestSubstring(s)
# print(f'result: {result}')
# print(f'Is the result correct? { result == expected}')




        
        
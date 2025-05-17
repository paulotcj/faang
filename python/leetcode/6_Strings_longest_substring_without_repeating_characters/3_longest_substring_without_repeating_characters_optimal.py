#problem: https://leetcode.com/problems/backspace-string-compare/description/

from typing import List, Dict, Tuple

class Solution:

    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s: str) -> int:

        low_idx = max_len = 0
        seen = {}

        for high_idx, high_v in enumerate(s):

            # If what we are accessing with high_v is in the dictionary and the index of this value
            #  is greater or equal to the low_idx, this means the char is repeated in the sequence.
            # Move low_idx to the next index of the repeated char, and start counting again.
            if seen.get(high_v, -1) >= low_idx:  # -1 is the default value if 'high_v' is not found
                low_idx = seen[high_v] + 1

            max_len = max(max_len, high_idx - low_idx + 1)
            seen[high_v] = high_idx

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




        
        
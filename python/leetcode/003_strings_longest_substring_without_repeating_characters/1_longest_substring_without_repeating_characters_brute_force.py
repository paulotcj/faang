# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from typing import Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s : str) -> int:
        max_len : int = 0
        substr_dict : Dict[str, int] = {}
        
        idx : int = 0            
        #-----------------------------------
        while idx < len(s):
            char : str = s[idx]
            #--------------
            if char in substr_dict: # substring broken - not unique chars in the substring
                max_len : int = max(max_len, len(substr_dict))
                idx : int = substr_dict[char] + 1 # idx needs to assume the next position because otherwise we know it will get stuck in a loop
                
                substr_dict : Dict[str,int] = {} # reset dict. do not add anything here
            else: # so far only unique chars
                substr_dict[char] = idx
                idx += 1
            #--------------
        #-----------------------------------
        
        # at this point we need to return the value of the max substring, but it might
        #   be the case where we didn't accumulate the values substr_dict, so we dot it now
        return_val : int = max(max_len, len(substr_dict))
        return return_val
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



    
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


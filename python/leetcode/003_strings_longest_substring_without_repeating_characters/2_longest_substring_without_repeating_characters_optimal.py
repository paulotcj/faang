# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from typing import Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s : str) -> int :
        input_str : str = s
        str_dict : Dict[str, int] = {}
        max_len : int = 0
        begin_substr_idx : int = 0
        
        #-----------------------------------
        for curr_idx , curr_char in enumerate(input_str):

            # breaking the substring condition - have we seen this char? and if so, is its index after
            #   our substring started?
            #--------------
            if curr_char in str_dict and str_dict[curr_char] >= begin_substr_idx:
                
                begin_substr_idx : int = max( begin_substr_idx, str_dict[curr_char] + 1 )
                
                if begin_substr_idx != curr_idx:
                    print('debug')
                
                # begin_substr_idx : int = curr_idx
                str_dict[curr_char] = curr_idx
                
            
            else: # first time seein this char
                str_dict[curr_char] = curr_idx
                
                # if we have a subsstring that is from low_idx = 2 and higher_idx = 4, we want to
                #   include indexes: 2, 3, 4. But using the subtraction we would have: 4 - 2 = 2
                #   therefore we need to add + 1
                curr_len : int = curr_idx - begin_substr_idx + 1
                max_len : int = max(max_len, curr_len)
        #--------------            
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
exit() 
    
    
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




        
        
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from typing import Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s : str) -> int :
        input_str : str = s
        str_dict  : Dict[str, int] = {}
        max_len   : int = 0
        curr_len  : int = 0
        begin_substr_idx : int = 0
        
        #-----------------------------------
        for curr_idx , curr_char in enumerate(input_str):

            #--------------
            # breaking the substring condition - have we seen this char? and if so, is its index after
            #   our substring started?
            if curr_char in str_dict and str_dict[curr_char] >= begin_substr_idx:
                
                max_len : int = max(max_len, curr_len) # before starting a new substring let's keep track of how long this one was
                
                # this get the index of the previous time we saw the repeated char and then skips 1 char ahead                
                begin_substr_idx : int = str_dict[curr_char] + 1
                
                str_dict[curr_char] = curr_idx # keep track where we last seen this char
                
            else: # first time seein this char
                str_dict[curr_char] = curr_idx # keep track where we last seen this char
                
                curr_len : int = curr_idx - begin_substr_idx + 1
        #--------------            
        #-----------------------------------
        
        max_len : int = max(max_len, curr_len) # we might need to update max_len here, as the last (few) loops might all be new unique chars only hitting the else condition from the loop
        
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




        
        
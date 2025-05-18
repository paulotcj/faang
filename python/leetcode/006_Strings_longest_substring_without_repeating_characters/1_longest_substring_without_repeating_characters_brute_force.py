#problem: https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    #-------------------------------------------------------------------------
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        string_dict = {}

        i = 0
        while i < len(s):
            v = s[i]

            if v in string_dict:
                max_len = max(max_len, len(string_dict))

                i = string_dict[v] + 1 # move i to the next index of the repeated character
                v = s[i]
               
                string_dict = {}
            else:
                string_dict[v] = i
                i += 1
        #-------
                
        return max(max_len, len(string_dict))
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




        
        
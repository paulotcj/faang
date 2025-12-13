from collections import Counter
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s: dict[str, int] = {}
        cnt_t: dict[str, int] = {}

        if len(s) != len(t): return False

        #--------------------------------------------------
        for char in s:
            # check if char exists in the dict if it does it returns the count of char, then adds 1. if it doesn't 
            #  we get 0 which is then added by 1
            cnt_s[char] = cnt_s.get(char, 0) + 1
        #--------------------------------------------------
        #--------------------------------------------------
        for char in t:
            cnt_t[char] = cnt_t.get(char, 0) + 1 # same logic here
        #--------------------------------------------------

        return cnt_s == cnt_t
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    

print('------------------------------------')
input1 = "racecar"
input2 = "carrace"
expected = True

sol = Solution()
result = sol.isAnagram(s=input1, t = input2)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
input1 = "jar"
input2 = "jam"
expected = False

sol = Solution()
result = sol.isAnagram(s=input1, t = input2)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
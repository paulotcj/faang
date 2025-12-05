from collections import Counter
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
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
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
input1 = "jar"
input2 = "jam"
expected = False

sol = Solution()
result = sol.isAnagram(s=input1, t = input2)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
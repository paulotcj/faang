#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValid(self, s: str) -> bool:
        return None
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = "[]"
expected = True

sol = Solution()
result = sol.isValid(s=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = "([{}])"
expected = True

sol = Solution()
result = sol.isValid(s=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = "[(])"
expected = False

sol = Solution()
result = sol.isValid(s=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


        
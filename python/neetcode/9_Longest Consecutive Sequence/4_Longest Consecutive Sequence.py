from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def longestConsecutive(self, nums: list[int]) -> int:


        #--------------------------------------------------

        #--------------------------------------------------
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
expected = 7

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

print('------------------------------------')
input = [2,20,4,10,3,4,5]
expected = 4

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [0,3,2,5,4,6,1,1]
expected = 7

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')





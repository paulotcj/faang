#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums: return 0

        num_set : set[int] = set(nums) # remove repeated nums, but remain unordered
        max_streak : int = 1

        #--------------------------------------------------
        for num in num_set:
            
            probing_num : int = num
            curr_streak : int = 1
            #--------------------------------------------------
            # Count consecutive numbers
            while probing_num + 1 in num_set:
                probing_num += 1
                curr_streak += 1
            #--------------------------------------------------

            max_streak = max(max_streak, curr_streak)
        #--------------------------------------------------

        return max_streak
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
expected = 7

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

print('------------------------------------')
input = [2,20,4,10,3,4,5]
expected = 4

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [0,3,2,5,4,6,1,1]
expected = 7

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')





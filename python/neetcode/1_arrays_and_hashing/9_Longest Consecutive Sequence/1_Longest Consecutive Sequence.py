#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0 : return 0
        nums.sort()
        conseq_cnt : int = 1
        max_conseq_cnt : int = 1
        prev : int = nums[0]
        print(nums)
        #--------------------------------------------------
        for idx , num in enumerate(nums):
            #-----
            if prev == num : continue
            elif (prev + 1) == num :
                conseq_cnt += 1
            else:
                max_conseq_cnt = max(max_conseq_cnt, conseq_cnt)
                conseq_cnt = 1
            #-----
            prev = num
        #--------------------------------------------------

        max_conseq_cnt = max(max_conseq_cnt, conseq_cnt)

        return max_conseq_cnt
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





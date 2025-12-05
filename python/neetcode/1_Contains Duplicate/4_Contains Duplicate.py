

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def hasDuplicate(self, nums: list[int]) -> bool:

        nums.sort() # sort in place

        #after sorting the array, any duplicate number will necessarily be next to each other
        #--------------------------------------------------
        for i in range(len(nums)-1): 
            if nums[i] == nums[i+1]:
                return True
        #--------------------------------------------------

        return False
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('------------------------------------')
input = [1, 2, 3, 4]
expected = False

sol = Solution()
result = sol.hasDuplicate(nums=input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = [1, 2, 3, 3]
expected = True

sol = Solution()
result = sol.hasDuplicate(nums=input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        #--------------------------------------------------
        for i in range(len(nums)) :
            #-----
            for j in range( i + 1 , len(nums) ) :
                if nums[i] + nums[j] == target: 
                    return [i,j]
            #-----
        #--------------------------------------------------

        return [] # no valid position, return empty array
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
        
print('------------------------------------')
input = [3,4,5,6]
target = 7
expected = [0,1]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [4,5,6]
target = 10
expected = [0,2]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = [5,5]
target = 10
expected = [0,1]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
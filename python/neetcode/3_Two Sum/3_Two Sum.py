#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        arr_map = {}

        #--------------------------------------------------

        #--------------------------------------------------

        #--------------------------------------------------

        #--------------------------------------------------

    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
        
print('------------------------------------')
input = [3,4,5,6]
target = 7
expected = [0,1]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [4,5,6]
target = 10
expected = [0,2]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = [5,5]
target = 10
expected = [0,1]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def hasDuplicate(self, nums: list[int]) -> bool:
        temp_set: set[int] = set(nums)
        return len(temp_set) != len(nums)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('------------------------------------')
input = [1, 2, 3, 4]
expected = False

sol = Solution()
result = sol.hasDuplicate(nums=input)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = [1, 2, 3, 3]
expected = True

sol = Solution()
result = sol.hasDuplicate(nums=input)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')
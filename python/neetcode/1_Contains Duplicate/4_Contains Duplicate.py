

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
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = [1, 2, 3, 3]
expected = True

sol = Solution()
result = sol.hasDuplicate(nums=input)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')
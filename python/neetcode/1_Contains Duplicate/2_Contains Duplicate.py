

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen: dict[int, int] = {}
        #--------------------------------------------------
        for num in nums :
            if num in seen :
                return True
            
            seen[num] = 1
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
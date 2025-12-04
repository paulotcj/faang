

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def hasDuplicate(self, nums: list[int]) -> bool:

        #--------------------------------------------------
        for i in range( len(nums) ) : # loop throuh the array, but anchor the comparisson at position i
            #-----
            for j in range(i+1, len(nums) ) : # now go checking for every new position after i
                if nums[i] == nums[j] : # found the same value
                    return True
            #-----
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
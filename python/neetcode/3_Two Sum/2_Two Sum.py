#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        indices: dict[int, int] = {}
        # build the num -> index dict
        #--------------------------------------------------
        for idx , val in enumerate(nums) : 
            indices[val] = idx
        #--------------------------------------------------

        #--------------------------------------------------
        for idx , val in enumerate(nums):
            
            # this basically means: do we have a solution for this number?
            diff: int = target - val 

            # check if we have a solution, and if the solution is different than the current number
            if (diff in indices) and indices[diff] != idx :
                return [ idx, indices[diff] ]
        #--------------------------------------------------

        return []
        

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
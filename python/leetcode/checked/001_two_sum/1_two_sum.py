# https://leetcode.com/problems/two-sum/

from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        #brute force
        #-----------------------------------
        for outer_i in range(len(nums)):
            for inner_i in range(outer_i+1,len(nums)):
                if nums[outer_i] + nums[inner_i] == target:
                    return [outer_i, inner_i]
        #-----------------------------------
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimized
        lookup : Dict[int, int] = {}
        
        # target = -90  and v = 5
        # diff = -90 - 5 ->  = -95 because now I need to find 95 in order to bring 
        # it back to -90 since we added 5
        
        #----------------------------------- 
        for idx, val in enumerate(nums):
            diff : int = target - val
            
            if diff in lookup:
                return [idx, lookup[diff]]
            
            lookup[val] = idx # this is the value and this is where to find it
        #-----------------------------------       
    #-------------------------------------------------------------------------        
#-------------------------------------------------------------------------



sol = Solution()
nums = [1,3,7,9,2]
target = 11
expected = [3,4]
result = sol.twoSum(nums, target)
print(f'result: {result}')
print(f'Is the result correct? { set(result) == set(expected)}')

print('------------------')
nums = [2,7,11,15]
target = 9
expected = [0,1]
result = sol.twoSum(nums, target)
print(f'result: {result}')
print(f'Is the result correct? { set(result) == set(expected)}')

print('------------------')
nums = [3,2,4]
target = 6
expected = [1,2]
result = sol.twoSum(nums, target)
print(f'result: {result}')
print(f'Is the result correct? { set(result) == set(expected)}')
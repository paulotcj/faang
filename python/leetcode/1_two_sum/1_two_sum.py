from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        #brute force
        if len(nums) < 2: return None

        for i, v in enumerate(nums):
            diff = target - v

            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i,j]
                
        return None

    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        #optimized
        lookup_dict : Dict[int] = {}

        for i, v in enumerate(nums):
            diff:int = target - v

            if diff in lookup_dict:
                return [lookup_dict[diff],i] #lookup_dict[diff] will store the first investigated indexes
            
            lookup_dict[v] = i
    #-------------------------------------------------------------------------      
    #-------------------------------------------------------------------------
    def twoSum(self, nums, target):
        #optimized
        lookup_dict = {}

        for i, v in enumerate(nums):
            diff = target - v

            if diff in lookup_dict:
                return [lookup_dict[diff],i] #lookup_dict[diff] will store the first investigated indexes
            
            lookup_dict[v] = i
    #-------------------------------------------------------------------------            
        
#-------------------------------------------------------------------------



sol = Solution()
nums = [1,3,7,9,2]
target = 11
expected = [3,4]
result = sol.twoSum(nums, target)
print(f'result: {result}')
print(f'Is the result correct? {sol.twoSum(nums, target) == expected}')

print('------------------')
nums = [2,7,11,15]
target = 9
expected = [0,1]
result = sol.twoSum(nums, target)
print(f'result: {result}')
print(f'Is the result correct? {sol.twoSum(nums, target) == expected}')

print('------------------')
nums = [3,2,4]
target = 6
expected = [1,2]
result = sol.twoSum(nums, target)
print(f'result: {result}')
print(f'Is the result correct? {sol.twoSum(nums, target) == expected}')
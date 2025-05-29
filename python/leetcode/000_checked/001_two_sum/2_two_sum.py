from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_to_index: dict[int, int] = {}
        
        # Iterate over the list with index and value
        for index, num in enumerate(nums):
            diff: int = target - num
            # Check if complement exists in the dictionary
            if diff in num_to_index:
                # Return indices of the two numbers
                return [num_to_index[diff], index]
            # Store the index of the current number
            num_to_index[num] = index
        
        return []
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
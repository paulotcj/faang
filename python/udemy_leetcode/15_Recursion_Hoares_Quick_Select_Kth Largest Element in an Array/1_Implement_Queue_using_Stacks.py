#problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List, Dict
#-------------------------------------------------------------------------

class Solution:
    #-------------------------------------------------------------------------
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k] 
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



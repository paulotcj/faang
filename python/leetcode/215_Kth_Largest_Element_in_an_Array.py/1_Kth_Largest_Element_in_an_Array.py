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



# sol = Solution()
# original_array = [3,2,3,1,2,4,5,5,6]

# expected = original_array.copy()
# expected.sort()
# result = sol.quicksort(original_array)
# # print(f'expected: {expected}')
# # print(f'result  : {result}')
# print(f'Is the result correct? { result == expected}')

# print('------------------')


# sol = Solution()
# original_array = [2,6,5,3,8]

# expected = original_array.copy()
# expected.sort()
# result = sol.quicksort(original_array)
# print(f'Is the result correct? { result == expected}')

# print('------------------')



# sol = Solution()
# original_array = [37, 12, 85, 64, 23, 7, 91, 56, 48, 19, 73, 2, 41, 88, 30, 60, 15, 99, 53, 27]

# expected = original_array.copy()
# expected.sort()
# result = sol.quicksort(original_array)
# print(f'Is the result correct? { result == expected}')

# print('------------------')



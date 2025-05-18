# https://leetcode.com/problems/container-with-most-water/

from typing import List

# 2 pointer array

#-------------------------------------------------------------------------
class Solution:
#-------------------------------------------------------------------------
    def maxArea(self, height: List[int]) -> int:

        left_border_idx: int = 0  # Start pointer at the beginning of the list
        right_border_idx: int = len(height) - 1  # End pointer at the end of the list
        max_area: int = 0  # Variable to keep track of the maximum area found

        #-----------------------------------
        while left_border_idx < right_border_idx:
            left_border_v : int = height[left_border_idx]
            right_border_v : int = height[right_border_idx]
            
            
            current_height: int = min(left_border_v, right_border_v)
            distance: int = right_border_idx - left_border_idx
            loop_area: int = current_height * distance


            max_area : int = max(max_area, loop_area)

            # Move the pointer pointing to the shorter line inward
            if left_border_v < right_border_v:
                left_border_idx += 1
            else:
                right_border_idx -= 1
        #-----------------------------------

        return max_area
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------




sol = Solution()
input = [1,8,6,2,5,4,8,3,7]
expected = 49
result = sol.maxArea(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')


sol = Solution()
input = [1,1]
expected = 1
result = sol.maxArea(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')
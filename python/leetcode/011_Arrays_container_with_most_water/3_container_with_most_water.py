# https://leetcode.com/problems/container-with-most-water/

from typing import List


#-------------------------------------------------------------------------
class Solution:
#-------------------------------------------------------------------------
    def maxArea(self, height: List[int]) -> int:

        left: int = 0  # Start pointer at the beginning of the list
        right: int = len(height) - 1  # End pointer at the end of the list
        max_area: int = 0  # Variable to keep track of the maximum area found

        #-----------------------------------
        while left < right:
            # Calculate the height and width for the current container
            current_height: int = min(height[left], height[right])
            current_width: int = right - left
            current_area: int = current_height * current_width

            # Update max_area if the current area is larger
            if current_area > max_area:
                max_area = current_area

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
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
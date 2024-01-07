#original problem: https://leetcode.com/problems/container-with-most-water/

from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def maxArea2(self, height: List[int]) -> int:
        max_area = 0

        for i, v_i in enumerate(height):
            for j in range(i+1, len(height)):
                v_j = height[j]
                area = min(v_i, v_j) * (j-i)
                max_area = max(max_area, area)
        #---
        return max_area
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def maxArea3(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        max_volume = 0 
        #------
        while left<right:
            new_volume = min(height[left],height[right]) * (right-left)
            max_volume = max(new_volume, max_volume)
            if height[left] < height[right]:
                left +=1
            else: 
                right -=1
        #------
        
        return max_volume    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def maxArea(self, height: List[int]) -> int:
        left_i , right_i = 0, len(height)-1
        max_volume = 0
        #------
        while left_i < right_i:
            new_volume = min(height[left_i], height[right_i]) * (right_i - left_i)
            max_volume = max(max_volume, new_volume)

            if height[left_i] < height[right_i]:
                left_i += 1
            else:
                right_i -= 1
        #------
        return max_volume
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
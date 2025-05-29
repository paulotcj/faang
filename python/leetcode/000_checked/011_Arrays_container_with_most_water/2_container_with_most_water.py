# https://leetcode.com/problems/container-with-most-water/

from typing import List


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def maxArea1(self, height: List[int]) -> int: # return max area found
        #sub optimal solution - we should start from the extremeties and close up
        
        max_area : int = 0
        #-----------------------------------
        for outer_i, outer_v in enumerate(height):
            for inner_i in range(outer_i+1, len(height)):
                inner_v : int = height[inner_i]
                
                min_height : int = min(outer_v, inner_v)
                dist : int = inner_i - outer_i
                loop_area : int = min_height * dist
                max_area = max(loop_area, max_area)
        #-----------------------------------
        
        return max_area
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def maxArea(self, height: List[int]) -> int:
        # smarter approach, we start from the extremeties
        max_area : int = 0
        
        left_border_idx : int = 0
        right_border_idx = len(height)-1

        # left needs to be smaller than right because at min if they were the same 
        #   the area would be zero
        #-----------------------------------
        while left_border_idx < right_border_idx : 
            left_border_v : int = height[left_border_idx]
            right_border_v : int = height[right_border_idx]
            
            min_height : int = min(left_border_v, right_border_v)
            distance : int = right_border_idx - left_border_idx
            
            loop_area : int = min_height * distance
            max_area : int = max(max_area, loop_area)
            
            # now let's move one border. We move whichever is the smallest, and if they are both equal we move left
            if left_border_v < right_border_v: left_border_idx += 1
            else: right_border_idx -= 1
                
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
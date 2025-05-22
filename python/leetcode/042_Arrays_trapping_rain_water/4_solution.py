# https://leetcode.com/problems/trapping-rain-water/
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def trap(self, height: List[int]) -> int:
        len_hei: int = len(height)
        
        if len_hei == 0: return 0

        left  : int = 0
        right : int = len_hei - 1
        left_max  : int = 0
        right_max : int = 0
        total_trapped_water : int = 0

        #-----------------------------------
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max : int = height[left]
                else:
                    total_trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max : int = height[right]
                else:
                    total_trapped_water += right_max - height[right]
                right -= 1
        #-----------------------------------

        return total_trapped_water
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


sol = Solution()
input = [0,1,2,1]
expected = 0
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')
# exit(0)
    
sol = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
expected = 6
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [4,2,0,3,2,5]
expected = 9
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [5,5,1,7,1,1,5,2,7,6]
expected = 23
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [9,2,1,1,6,4,0,4,4]
expected = 18
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')


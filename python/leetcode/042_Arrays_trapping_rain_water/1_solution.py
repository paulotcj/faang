# https://leetcode.com/problems/trapping-rain-water/
from typing import List

''' Here's how this problem logic works. You need to know how much water a specific
position can hold, and then repeat this procedure to every single position.
We are approaching from the principle that at each position we should calculate 
the water column above the whatever ground level is at spot 'i'.
And in order to calculate how much water location 'i' can hold above its 'ground level' 
we need to know the max gound level to the left and the max ground level to the right
and then identify the min between these 2. And then discont the ground level at spot 'i'

So for instance, spot 'i' is at height 5, the max level to the left is 10, the max level
to the right is 15, then we have that position 'i' can hold:
  min(10,15) = 10 (potential water units for spot 'i')
  10 - 5 (this is the ground level) = 5.

So location 'i' can hold 5 units of water
'''

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def __find_max_left(self, height: List[int], index: int) -> int:
        if index <= 0 or index >= len(height): return 0
        return max(height[:index])
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __find_max_right(self, height: List[int], index: int) -> int:
        index += 1
        if index < 0 or index >= len(height): return 0
        return max(height[index:])
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def trap(self, height: List[int]) -> int:
        total_water = 0

        for i, v in enumerate(height):
            max_left = self.__find_max_left(height, i)
            max_right = self.__find_max_right(height, i)

            current_water = min(max_left, max_right) - v

            if current_water > 0:
                total_water += current_water

        return total_water
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


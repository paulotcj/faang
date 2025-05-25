# https://leetcode.com/problems/trapping-rain-water/
from typing import List , Tuple

''' Here's how this problem logic works. You need to know how much water a specific
position can hold, and then repeat this procedure for every single position.
We are approaching from the principle that at each position we should calculate 
the water column above the whatever ground level is at spot 'i'.
And in order to calculate how much water location 'i' can hold above its 'ground level' 
we need to know the max ground level to the left and the max ground level to the right
and then identify the min between these 2. And then discount the ground level at spot 'i'

So for instance, spot 'i' is at height 5, the max level to the left is 10, the max level
to the right is 15, then we have that position 'i' can hold:
  min(10,15) = 10 (potential water units for spot 'i')
  10 - 5 (this is the ground level) = 5.

So location 'i' can hold 5 units of water
'''


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def _find_max_left(self, index : int) -> int:
        if index <= 0 or index >= len(self.height): return 0
        
        if index >= self.memo_left[0] and self.height[index] < self.memo_left[1]:
            return self.memo_left[1]  
             
        self.memo_left : Tuple[int,int] = (index, self.height[index])
        return self.height[index]
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def _find_max_right(self, index : int) -> int:
        index += 1 # to offset the non-inclusive nature of slicing
        if index <= 0 or index >= len(self.height) : return 0
        
        if index <= self.memo_right[0] and self.height[index] < self.memo_right[1]:
            return self.memo_right[1]

        max_val : int = max(self.height[index:])
        self.memo_right : Tuple[int,int] = (index , max_val)
        return max_val
    #------------------------------------------------------------------------- 
    #-------------------------------------------------------------------------
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0
        
        self.memo_left : Tuple[int,int] = (0,height[0]) # index, val
        self.memo_right : Tuple[int,int] = (len(height)-1, float('-inf')) # index, val
        
        
        total_water : int = 0
        self.height : List[int] = height
        
        #-----------------------------------
        for for_i, pos_gound_level in enumerate(self.height):
            max_hei_left : int = self._find_max_left( index = for_i)
            max_hei_right : int = self._find_max_right( index = for_i )
            
            position_height : int = min(max_hei_left, max_hei_right)
            current_water_level : int = position_height - pos_gound_level
            
            if current_water_level > 0 : total_water += current_water_level
        #-----------------------------------
        
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


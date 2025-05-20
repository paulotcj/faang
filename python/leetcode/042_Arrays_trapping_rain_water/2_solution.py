# https://leetcode.com/problems/trapping-rain-water/
from typing import List, Tuple

''' let's explore the logic here: suppose we have the array as [0,0,4,2,6,7,5,0,0]
the edges where we have 0 doesn't mean anything to us. So we need to check the first edges
with some 'height' which from the left will be idx=2 v=4, and right idx=6 v=5. And initially we
record these 2 as our max values to each side respectively. max_left=4, max_right=5
Since these 2 are our first edges, we can't calculate the water level with them so we need to move 
one pointer.
We will move the smallest pointer, in this case idx=2 v=2, which now will assume idx=3 v=2.
We now compare if this new value is smaller than the max_left. It is. That means we can calculate
the water level. We do min(max_left,max_right) -> min(4,5) -> 4 and this is because the water level
is limited by the lowest wall.
Now knowing the potential for water storage at idx=2 is 4 (as we saw in the previous step), we need
to discount the terrain level, so: potential_water - terrain_level = 4 - 2 = 2. And then we add 2
to the tally of total water accumulated. Note that no other walls can interfere with the amount of
water storage at idx=3, it doesn't matter how tall or how low the other walls are, at idx=3 we are
bounded by the left wall being the smallest.

Now if we were to have an array like this: [1,2,3,4,3,2,1], we obviously woudn't be able to store any
water, as the values keep increasing towards the center and there's no dip to form a 'pool'

If we were to have an array like this: [1,2,3,1,3,2,1], then it gets more interesting but still
straightforward, left and right pointers would move towards the center always increasing their
max_left and max_right, until: 
  left_idx  = 2 , left_v  = 3 , max_left  = 3 
  right_idx = 4 , right_v = 3 , max_right = 3
At which point one index has the move, and typically when the values are the same we move left for
simplicity and convenience. Now: left_idx  = 3 , left_v  = 1 , max_left  = 3
We do the potential water level: min(max_left, max_right) -> min(3,3) -> 3
And then: Water_level = potential_water_level - current_terrain_level = 3 - 1 = 2 (water level at idx 3)

'''
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def _find_first_left(self) -> Tuple[int,int]: # find the first occurence of a non zero height
        for idx, val in enumerate(self.height):
            if val > 0 : 
                ret_val : Tuple[int,int] = (idx,val)
                return ret_val
           
        # when all values are zero, this will skip any calculation effectively returning total water = 0 
        return (0,0) 
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _find_first_right(self) -> Tuple[int,int]: # find the first occurence of a non zero height from the right side 
        
        # you need eto convert the output of enumerate to a list as enumerate is not reversible
        #  so the logic is, get the idx and val from self.height via enumerate. convert it
        #  to a list as it's necessary, then reverse it.
        for idx, val in reversed(list(enumerate(self.height))):
            if val > 0:
                ret_val : Tuple[int,int] = (idx, val)
                return ret_val
        
        # when all values are zero, this will skip any calculation effectively returning total water = 0   
        return (0,0)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _calculate_water_level(self, terrain_height : int, left_side : bool = False, 
      right_side : bool = False) -> None:
        
        if (left_side == True and terrain_height < self.max_left ) or \
          (right_side == True and terrain_height < self.max_right ):
              
            potential_water_level : int = min(self.max_left, self.max_right)
            current_water_level : int = potential_water_level - terrain_height
            self.total_water += current_water_level
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def trap(self, height: list[int]) -> int:
        #---------------------
        # basic house keeping and setting up vars
        if len(height) < 3 : return 0 # you need at least a wall, a well, and a wall
        self.height : List[int] = height
        self.total_water : int = 0
        #---------------------
        # we are just looking to find the first non zero value of the left and right walls , and that's it
        left_i , self.max_left = self._find_first_left() # find the first occurence of a non zero height from the left side
        right_i, self.max_right = self._find_first_right() # find the first occurence of a non zero height from the right side
        #---------------------
        
        #-----------------------------------
        while left_i < right_i:
            left_v  : int = self.height[left_i]
            right_v : int = self.height[right_i]
            
            self.max_left  : int = max(self.max_left, left_v)
            self.max_right : int = max(self.max_right, right_v)            
            
            if left_v <= right_v:
                self._calculate_water_level(terrain_height=left_v, left_side=True)
                left_i += 1
            else:
                self._calculate_water_level(terrain_height=right_v, right_side=True)
                right_i -= 1
        #-----------------------------------
        return self.total_water
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
input = [0,1,2,1]
expected = 0
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')
# exit(0)
    
sol = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
expected = 6
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [4,2,0,3,2,5]
expected = 9
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [5,5,1,7,1,1,5,2,7,6]
expected = 23
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')



sol = Solution()
input = [9,2,1,1,6,4,0,4,4]
expected = 18
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')


sol = Solution()
input = [9,2,1,1,6,4,0,4,4,0,0,0]
expected = 18
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')


sol = Solution()
input = [0,0,0]
expected = 0
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')
